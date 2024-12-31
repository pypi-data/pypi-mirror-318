import io
import os

import cv2
import fitz
import pytesseract
from PIL import Image


class PDFTextExtractor:
    def __init__(self, pdf_path, image_dir):
        """Initialize with PDF path and image directory."""
        self.pdf_path = pdf_path
        self.image_dir = image_dir

    def __extract_images_from_pdf(self):
        """Extract images from the PDF and save them as PNG files."""
        doc = fitz.open(self.pdf_path)
        image_paths = []

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            img_list = page.get_images(full=True)

            for img_index, img in enumerate(img_list):
                xref = img[0]
                image = doc.extract_image(xref)
                image_bytes = image["image"]

                img = Image.open(io.BytesIO(image_bytes))
                img_filename = f"image_{page_num + 1}_{img_index + 1}.png"
                img_path = os.path.join(self.image_dir, img_filename)
                img.save(img_path)

                image_paths.append((page_num, img_path))  # Include page number for ordering

        return image_paths

    def __preprocess_image(self, image_path):
        """Preprocess image to improve OCR accuracy."""
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError(f"Image at path {image_path} could not be loaded.")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        contrast = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)
        _, binary = cv2.threshold(contrast, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        denoised = cv2.GaussianBlur(binary, (5, 5), 0)
        return denoised

    def __extract_text_from_image(self, image_path):
        """Extract text from an image using Tesseract OCR after preprocessing."""
        preprocessed_image = self.__preprocess_image(image_path)
        pil_image = Image.fromarray(preprocessed_image)
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -l eng'
        return pytesseract.image_to_string(pil_image, config=custom_config).strip()

    def process_and_extract_text(self):
        """Extract and process text from both PDF and images, returning a combined result."""
        if not os.path.exists(self.image_dir):
            os.makedirs(self.image_dir)

        doc = fitz.open(self.pdf_path)
        results = []

        # Extract text and images from each page
        for page_num in range(len(doc)):
            # Extract text from the current page
            page = doc.load_page(page_num)
            pdf_text = page.get_text("text").strip()
            if pdf_text:
                results.append({"text": pdf_text})

            # Extract and process images from the current page
            img_list = page.get_images(full=True)
            for img_index, img in enumerate(img_list):
                xref = img[0]
                image = doc.extract_image(xref)
                image_bytes = image["image"]

                img = Image.open(io.BytesIO(image_bytes))
                img_filename = f"image_{page_num + 1}_{img_index + 1}.png"
                img_path = os.path.join(self.image_dir, img_filename)
                img.save(img_path)

                # Extract text from the image
                try:
                    image_text = self.__extract_text_from_image(img_path)
                    if image_text:
                        results.append({"image_text": image_text})
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")
                    results.append({"image_text": ""})  # Append empty text if processing fails

        return results

import io
import os

import cv2
import fitz
import pytesseract
from PIL import Image


class PDFTextExtractor:
    def __init__(self, pdf_path, image_dir):
        """Initialize with PDF path and image directory."""
        self.__pdf_path = pdf_path
        self.__image_dir = image_dir

    def __extract_images_from_pdf(self):
        """Extract images from the PDF and save them as PNG files."""
        doc = fitz.open(self.__pdf_path)
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
                img_path = os.path.join(self.__image_dir, img_filename)
                img.save(img_path)

                image_paths.append((page_num, img_path))

        return image_paths

    @staticmethod
    def __preprocess_image(image_path):
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

    def process_and_extract_text(self, use_llm_for_image_text: bool = False, model: str = 'mistral:latest'):
        """
        Extract and process text from a PDF and its embedded images.

        Args:
            use_llm_for_image_text (bool): Refine OCR-extracted image text using a language model (default: False).
            model (str): Specify the LLM model for refinement (default: 'mistral:latest').

        Returns:
            list[dict]: Combined content, with 'text' for PDF text and 'image_text' for processed image text.
        """
        if not os.path.exists(self.__image_dir):
            os.makedirs(self.__image_dir)

        doc = fitz.open(self.__pdf_path)
        results = []

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pdf_text = page.get_text("text").strip()
            if pdf_text:
                results.append({"text": pdf_text})

            img_list = page.get_images(full=True)
            for img_index, img in enumerate(img_list):
                xref = img[0]
                image = doc.extract_image(xref)
                image_bytes = image["image"]

                img = Image.open(io.BytesIO(image_bytes))
                img_filename = f"image_{page_num + 1}_{img_index + 1}.png"
                img_path = os.path.join(self.__image_dir, img_filename)
                img.save(img_path)

                try:
                    image_text = self.__extract_text_from_image(img_path)
                    if image_text:
                        if use_llm_for_image_text:
                            results.append(
                                {"image_text": self.__rewrite_extracted_text_with_ollama_models(image_text, model)})
                        else:
                            results.append({"image_text": image_text})
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")
                    results.append({"image_text": ""})

        return results

    @staticmethod
    def __rewrite_extracted_text_with_ollama_models(image_text, model: str = 'mistral:latest'):
        from ollama import chat, ChatResponse

        response: ChatResponse = chat(model=model, messages=[
            {
                'role': 'user',
                'content': f'### Transform the following into a human-readable format, organizing it clearly:\n'
                           f'{image_text}',
            },
        ])

        return response['message']['content']

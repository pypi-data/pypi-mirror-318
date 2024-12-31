# PDFTextExtractor

A Python utility for extracting text and images from PDF files. The extracted text includes content from PDF pages and
OCR-processed text from images embedded in the PDF. Results are returned as a combined list of dictionaries, preserving
the order of appearance.

---

## Features

- Extract text directly from PDF pages.
- Extract and OCR-process images embedded in PDFs.
- Return results in a combined, ordered list of text and image content.
- Preprocess images to improve OCR accuracy.

---

## Requirements

### Python

- **Python Version**: 3.7 or higher
- **Required Libraries**:  
  Install dependencies via pip:

```shell
pip install opencv-python pillow PyMuPDF pytesseract
```

Tesseract OCR

- Tesseract Installation:  
  Install Tesseract OCR and ensure it is accessible via the system’s PATH.
  Follow the Tesseract Installation Guide for details.

---
Usage

Import and Initialize:

```python
from pdf_text_extractor import PDFTextExtractor

# Provide the PDF file path and image directory
pdf_path = "example.pdf"
image_dir = "output_images"

# Initialize the extractor
extractor = PDFTextExtractor(pdf_path, image_dir)

```

Process PDF and Extract Content

```python

# Extract text and image content
results = extractor.process_and_extract_text()

# Display extracted content
for item in results:
    if "text" in item:
        print("PDF Text:", item["text"])
    elif "image_text" in item:
        print("Image Text:", item["image_text"])

```

---
Output Format

The method process_and_extract_text() returns a list of dictionaries. Each dictionary contains either text or
image_text, corresponding to content from the PDF or OCR-processed images.

Example Output

```json

[
  {
    "text": "This is text from the first page of the PDF."
  },
  {
    "image_text": "Text extracted from an image on the first page."
  },
  {
    "text": "Another page of the PDF with textual content."
  },
  {
    "image_text": "Additional image-based text extracted."
  }
]
```

---

## How It Works

### Text Extraction

- Text from PDF pages is extracted using **PyMuPDF**.

### Image Extraction

- Embedded images are extracted and saved to the specified directory.
- Images are preprocessed before OCR.

### Image Preprocessing

- **Convert to Grayscale**: Converts the image to grayscale.
- **Enhance Contrast**: Increases contrast to make text stand out.
- **Binarization**: Uses Otsu’s thresholding to create a binary image.
- **Denoising**: Applies Gaussian blur to reduce noise.

### OCR

- Preprocessed images are processed with **Tesseract OCR** to extract text.

---

## Error Handling

- If an image fails to process, an empty `image_text` value is added to the results.
- **Example**:
```json
{
  "image_text": ""
}

```
---
## Methods

### `__init__(pdf_path, image_dir)`

**Parameters**:
- `pdf_path` (str): Path to the input PDF file.
- `image_dir` (str): Directory to save extracted images.

---

### `process_and_extract_text()`

**Description**: Processes the PDF to extract text and images.

**Returns**:
- A list of dictionaries containing extracted `text` or `image_text`.

---
## Contribution

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.
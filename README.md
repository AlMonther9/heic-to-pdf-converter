A lightweight Python script that converts directories of HEIC images (like those exported from an iPhone) and merges them into a single, highly-portable PDF file. It automatically reads timestamps encoded in the filenames to ensure the final PDF stays perfectly sorted in chronological order. Uses pillow-heif and fpdf2 for fast memory-efficient processing without losing image proportions.


# HEIC to PDF Converter 📄

A lightweight Python utility to batch convert HEIC images and merge them into a single PDF document. The script automatically sorts the images chronologically based on their filenames before merging them.

## Features
- **Batch Processing**: Converts multiple [.heic](cci:7://file:///k:/ECE/Second%20Semester/Modern%20Control/Book-20260423T094920Z-3-001/Book/20260423_112433.heic:0:0-0:0) files in a folder into a single PDF.
- **Chronological Sorting**: Automatically sorts images based on the filename (e.g., date-based names like [20260423_112247.heic](cci:7://file:///k:/ECE/Second%20Semester/Modern%20Control/Book-20260423T094920Z-3-001/Book/20260423_112247.heic:0:0-0:0)).
- **Aspect-Ratio Preserving**: Intelligently fits images to standard A4 PDF pages without distorting them.

## Requirements
To run this script, you will need Python installed along with the following packages:
```bash
pip install pillow-heif Pillow fpdf2

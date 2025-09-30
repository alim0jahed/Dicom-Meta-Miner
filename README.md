# DICOM Metadata Extractor

A Python tool to **extract and flatten DICOM metadata** into structured datasets.

This tool is useful for **medical imaging researchs, data preprocessing and PACS metadata mining**.

---

## Features

- Recursively processes folders containing DICOM files
- Extracts all headers, keywords, sequence elements in DICOM Metadata
- Outputs DICOM metadata as CSV
- Built with [pydicom](https://pydicom.github.io/) and [pandas](https://pandas.pydata.org/)

---

## Usage

Run  `main.py` and provide your `base_path` containing your DICOM files.

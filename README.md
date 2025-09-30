# 📦 DICOM Metadata Extractor

A Python tool to **extract and flatten DICOM metadata** into structured datasets.

This tool is useful for **medical imaging researchs, data preprocessing and PACS metadata mining**.

---

## ✨ Features

- 📂 Recursively processes folders containing DICOM files
- 🧩 Extracts all headers, keywords, sequence elements in DICOM Metadata
- 💾 Outputs DICOM metadata as CSV
- 🧪 Built with [pydicom](https://pydicom.github.io/) and [pandas](https://pandas.pydata.org/)

---

## ⚡️Usage

Run  `main.py` and provide your `base_path` containing your DICOM files.

Example `base_path` folder structure :
```
Src/
  sample/
    patient1/
      file1.dcm
    patient2/
      file2.dcm
    patient3/
      file3.dcm
```

---

📚 References

[DICOM Standard (NEMA)](https://dicom.nema.org/medical/dicom/current/output/chtml/part06/chapter_6.html?utm_source=chatgpt.com)

[Innolitics DICOM Browser](https://dicom.innolitics.com/ciods)

[pydicom Documentation](https://pydicom.github.io/)

---
🤝 Contribution
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

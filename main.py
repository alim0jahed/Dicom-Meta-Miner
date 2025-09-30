from Modules import data
import pandas as pd
import pydicom as dc
from pathlib import Path


# ---------- Batch process ----------
def process_dicom_folder(base_path: str):
    """
    Iterate all DICOM files under base_path recursively
    and return a DataFrame with one row per file.
    """
    base = Path(base_path)
    all_rows = []
    all_keywords = None  # use first file as reference

    for file in base.rglob("*"):
        if file.is_file():
            try:
                ds = dc.dcmread(file, force=True)

                # Extract headers (first file defines structure)
                keywords = data.extract_headers(ds)
                if all_keywords is None:
                    all_keywords = keywords

                # Extract values
                values = data.extract_values(ds)

                # Convert to DataFrame row
                df_row = data.dicom_to_dataframe(all_keywords, values)
                df_row.insert(0, "FilePath", str(file))  # track file origin
                all_rows.append(df_row)

            except Exception as e:
                print(f"⚠️ Skipping {file}: {e}")

    # Combine all rows
    if all_rows:
        final_df = pd.concat(all_rows, ignore_index=True)
        return final_df
    else:
        return pd.DataFrame(columns=(["FilePath"] + (all_keywords or [])))


def run(path):
    df = process_dicom_folder(path)
    df.to_csv("MetaData.csv", index=False)



user_path = input('Enter the base path containing DICOM Files :')
run(user_path)




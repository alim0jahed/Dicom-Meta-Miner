import pydicom
import pandas as pd
from pathlib import Path

def extract_headers(ds, parent_path=""):
    """
    Return a flat list of hierarchical keywords (works for sequences).
    Example: ReferencedSeriesSequence[0].SeriesInstanceUID
    """
    keywords = []

    for elem in ds:
        key = f"{parent_path}.{elem.keyword}" if parent_path else elem.keyword
        keywords.append(key)

        if elem.VR == "SQ":  # Sequence
            for i, item in enumerate(elem.value):
                seq_prefix = f"{key}[{i}]"
                child_keywords = extract_headers(item, parent_path=seq_prefix)
                keywords.extend(child_keywords)

    return keywords

def extract_values(ds, parent_path=""):
    """
    Return a dict {hierarchical_keyword: value}, aligned with extract_headers.
    """
    values = {}

    for elem in ds:
        key = f"{parent_path}.{elem.keyword}" if parent_path else elem.keyword

        if elem.VR == "SQ":
            values[key] = f"<Sequence with {len(elem.value)} item(s)>"
            for i, item in enumerate(elem.value):
                seq_prefix = f"{key}[{i}]"
                child_values = extract_values(item, parent_path=seq_prefix)
                values.update(child_values)
        else:
            val = elem.value
            if isinstance(val, bytes):
                val = f"<Binary length={len(val)}>"
            elif isinstance(val, list) and len(val) > 10:
                val = f"<List length={len(val)}>"
            values[key] = val

    return values

def dicom_to_dataframe(keywords, values):
    row = {key: values.get(key, None) for key in keywords}
    return pd.DataFrame([row])



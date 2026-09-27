import re
import numpy as np
import pandas as pd
def to_seconds(val):
    """Convert timedelta string like '0 days 00:01:29.385000' to float seconds."""
    if val == 0:
        val = "100:00:00.000000"  # Assign a large value for missing times
    if pd.isna(val):
        val = "0:00:00.000000"  # Assign zero for NaN values
    match = re.search(r'(\d+):(\d+):(\d+\.?\d*)', str(val))
    if match:
        h, m, s = match.groups()
        return int(h) * 3600 + int(m) * 60 + float(s)
    return np.nan
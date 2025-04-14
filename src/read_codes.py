import pandas as pd

import src.log_config as log
from src.defines import INPUT_EXCEL


def read_codes():
    """Read the codes in 'code' column from a Excel (xlsx) file."""
    try:
        df = pd.read_excel(INPUT_EXCEL)
        if 'code' not in df.columns:
            raise ValueError("There is no 'code' column in the Excel file.")
        return df['code'].astype(str).tolist()
    except Exception as e:
        log.logger.error(f'Error in read xlsx: {str(e)}')
        raise

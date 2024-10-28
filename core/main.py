import sys
import os
myDir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(myDir, '..'))
import pandas as pd
from gui import atGUI
from helpers.constants import XLSX_PATH

def read_excel_file() -> pd.DataFrame:
    """Read Excel file and return DataFrame."""
    # Read Excel file
    df = pd.read_excel(XLSX_PATH)

    # Format part number
    df['PART NUMBER'] = df['PART NUMBER'].apply(lambda x: f"{x:06d}" if isinstance(x, int) else x)

    return df


atGUI.display_table(read_excel_file())

# if __name__ == '__main__':
#     gui.display_table()
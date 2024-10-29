import pandas as pd
from gui import atGUI
from helpers.constants import XLSX_PATH, COLUMN_RENAME_DIC, COLUMN_WIDTHS

def read_excel_file(path_to_xlsx: str = XLSX_PATH) ->  pd.DataFrame:
    """Read Excel file and return DataFrame."""
    # Read Excel file
    df = pd.read_excel(path_to_xlsx)

    # Format part number
    df['PART NUMBER'] = df['PART NUMBER'].apply(lambda x: f"{x:06d}" if isinstance(x, int) else x)
    
    df.rename(columns = COLUMN_RENAME_DIC, inplace = True)

    formatDataFrameValues(df)
    
    return df

def formatDataFrameValues(df):
    df['No'] = df['No'].map(str)
    df['Dsk'] = df['Dsk'].map(str)
    df['Qty'] = df['Qty'].astype(int)
    df['Thk'] = df['Thk'].map(str)
    df['Proc'] = df['Proc'].map(str)
    df['File'] = df['File'].map(str)
    

dataFrame = read_excel_file(XLSX_PATH)
atGUI.displayForm(dataFrame, COLUMN_WIDTHS)

if __name__ == '__main__':
    import sys
    read_excel_file(sys.argv[1])
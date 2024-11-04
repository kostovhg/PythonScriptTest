# constants.py

XLSX_NAME = '08_Milling_OT.xlsx'
XLSX_DIR = './'
XLSX_PATH = XLSX_DIR + XLSX_NAME
COLUMN_RENAME_DIC = {'PART NUMBER': 'No', 'DESCRIPTION': 'Dsk', 'QTY.': 'Qty', 'Material': 'Mat', 'Sheeet metal \nthickness': 'Thk', 'CAD_length/mm': 'L', 'Surface \narea/m2': 'S' , 'Cad_perimeter/mm': 'P', 'Processing': 'Proc', 'Files': 'File', 'Material 1': 'Mat1', 'CAD_length 1/mm': 'L1', 'Material 2': 'M2', 'CAD_length 2/mm': 'L2', 'Material 3': 'M3', 'CAD_length 3/mm': 'L3', 'TETAMAT code': 'TCode', 'Producer': 'Prod', 'Producer code': 'ProdCode', 'Supplier': 'Sup', 'CAD_ZONE ': 'CADz', 'Cad weight/g': 'Weight', 'Общи дължини на профили/мм': 'Total L', 'Общи площи/м2': 'Total S', 'Unnamed: 24': '24', 'Row Labels': 'Rlabels', 'Sum of Общи площи/м2': 'Total P', 'Sum of Общи дължини на профили/мм': 'TTotal L'}
COLUMN_WIDTHS = {'No': 80,  'Dsk': 120, 'Qty': 40,  'Mat': 60, 'Thk': 40,  'L': 60,  'S' : 40, 'P': 40, 'Proc' : 80, 'File': 80, 'Mat1': 0, 'L1':0,  'M2': 0, 'L2':0, 'M3':0, 'L3':0,  'TCode':0,'Prod':0, 'ProdCode':0,  'Sup':0, 'CADz':0, 'Weight':0,'Total L':0, 'Total S':0, '24':0, 'Rlabels':0, 'Total P':0, 'TTotal L':0}

import openpyxl

book = openpyxl.load_workbook("Planilha de Compras.xlsx")
frutas_page = book["Frutas"]


# imprimindo os dados de cada linha
for rows in frutas_page.iter_rows(min_row=1,max_row=6):
   print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}')
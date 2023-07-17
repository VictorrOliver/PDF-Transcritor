import tabula
import os

def extract_tables_from_pdf(file, table_path, encoding):
    pdf_path = file
    path_dest = table_path
    encoding = 'ISO-8859-1'

    os.makedirs(path_dest, exist_ok=True)

    dfs = tabula.read_pdf(pdf_path, pages='all', encoding=encoding, multiple_tables=True)
    print(len(dfs))
    for i in range(len(dfs)):
        print(f"Table {i}:")
        print(dfs[i])
        output_file = os.path.join(path_dest, f"table_{i}.csv")
        dfs[i].to_csv(output_file)
        print("--------------------------------------------------")


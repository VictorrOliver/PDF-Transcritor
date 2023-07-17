import extract_text_from_pdf
import extract_images_from_pdf
import extract_tables_from_pdf

file = 'arquivo.pdf'
output_file = 'texto_extraido.txt'

print("Extraindo texto...")
extracted_text = extract_text_from_pdf.extract_text_from_pdf(file)
with open(output_file, 'w', encoding='utf-8') as output_file:
    output_file.write(extracted_text)
print("Texto extraído")

print("Extraindo imagens...")
images_path = 'images/'
extract_images_from_pdf.extract_images_from_pdf(file, images_path)
print("Imagens extraídas")

print("Extraindo tabelas...")
tables_path = "tables"
extract_tables_from_pdf.extract_tables_from_pdf(file, tables_path, 'ISO-8859-1')
print("Tabelas extraídas")


from tabula import convert_into
from tabula import read_pdf
df=read_pdf("sample.pdf",pages=2,multiple_table=True)

print(df)
convert_into("sample.pdf","sample.json",pages=2,output_format="json")
convert_into("sample.pdf","sample.tsv" ,pages=2,output_format="tsv")
convert_into("sample.pdf","sample.csv" ,pages=2,output_format="csv")

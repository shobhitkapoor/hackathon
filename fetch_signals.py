from tabula import convert_into
from tabula import read_pdf
df=read_pdf("ARM_AMBA3_APB.pdf",pages=32)

print(df)
convert_into("ARM_AMBA3_APB.pdf","test.json",pages=32,output_format="json")
convert_into("ARM_AMBA3_APB.pdf","test.tsv" ,pages=32,output_format="tsv")
convert_into("ARM_AMBA3_APB.pdf","test.csv" ,pages=32,output_format="csv")

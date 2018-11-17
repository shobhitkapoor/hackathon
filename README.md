#Hackthon

Installing tabula.py to extract table from PDF

Using ARM AMBA APB3 for Initial trial

Following command will install tabula
sudo pip install tabula-py

usage of tabula-py:

	from tabula import read_pdf
	df = read_pdf(data.pdf)

you can also extract tables in json format
read_pdf(data.pdf, output_format=json)

refrence taken from following url:

https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302
_____________________________________

PyPDF2 to Convert Simple, Text-Based PDF file into text readable by Python

textract to convert non-trivial, scanned PDF  PDF file into text readable by Python

ntlk to clean and convert phrases into keywords

sudo pip install PyPDF2
sudo pip install textract
sudo pip install nltk

refrence taken from following url:

https://medium.com/@rqaiserr/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f
_____________________________________

APB PROTOCOL PDF DOWNLOADED FORM

http://web.eecs.umich.edu/~prabal/teaching/eecs373-f12/readings/ARM_AMBA3_APB.pdf

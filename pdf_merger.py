from pypdf import PdfWriter

merger=PdfWriter()

n=int(input("enter the no of pdf files you want to merge"))
pdf_files=[]
for i in range(0,n):
    pdf=input("enter the path of pdf file you want to merge with '.pdf' extension")
    pdf_files.append(pdf)
    i+=1
for pdffile in pdf_files:
    merger.append(pdffile)
merged_file=input("Enetr the nmae of the merged file")
merger.write(merged_file)
merger.close

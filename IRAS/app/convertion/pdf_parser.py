import pdfplumber

def convert_pdf_to_txt(pdf_path):
    texts =""
    with pdfplumber.open(pdf_path) as pdf:
        # page = pdf.pages[0]   # 第一页的信息
        # text = page.extract_text()
        for page in pdf.pages:
            texts+=page.extract_text()
    return texts

if __name__ == "__main__":
    pdf_path = "D:/myWorkspace/IRAS/footprint/dataset_pdf/27.pdf"
    print(convert_pdf_to_txt(pdf_path))
import pdfplumber
import re
def convert_pdf_to_txt(pdf_path):
    texts =""
    with pdfplumber.open(pdf_path) as pdf:
        # page = pdf.pages[0]   # 第一页的信息
        # text = page.extract_text()
        for page in pdf.pages:
            texts+=page.extract_text()
    texts = texts.replace(' ', '').replace('\t', '')
    texts = re.sub(r'\n+', '\n', texts)
    return texts

if __name__ == "__main__":
    pdf_path = r"D:\QQ Download\测试数据及说明\data\pdf\103.pdf"
    print(convert_pdf_to_txt(pdf_path))
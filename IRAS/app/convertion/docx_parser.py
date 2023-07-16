from docx import Document
from docx.shared import Inches
import docx2txt
import re

#传入文件路径，返回文件信息
def convert_docx_to_txt(path):
    # 读取docx文件并去除空格和制表符
    row_text = docx2txt.process(path).replace(' ', '').replace('\t', '')
    # 将多个换行符替换为一个换行符
    row_text = re.sub(r'\n+', '\n', row_text).split('\n')
    # 按照换行符分割并去重
    seen = set()
    text_list = []
    for row in row_text:
        if row not in seen:
            text_list.append(row.strip())
            seen.add(row)
    text = '\n'.join(text_list)
    return text

if __name__ == '__main__':
    result = convert_docx_to_txt('D:/myWorkspace/IRAS/footprint/dataset_docx/4.docx')
    print(result)

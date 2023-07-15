from docx import Document
from docx.shared import Inches

#传入文件路径，返回文件信息
def convert_docx_to_txt(path):
    document = Document(path)
    # 提取表格内容
    cell_text = ""
    for table in document.tables:
        for row in table.rows:
            temp = []
            for cell in row.cells:
                if cell.text not in temp:
                    temp.append(cell.text)
            for t in temp:
                cell_text += t + '\n'

    # 提取段落内容
    paragraphs_text = ""
    for paragraph in document.paragraphs:
        if paragraph.text not in paragraphs_text:
            paragraphs_text += paragraph.text + "\n"

    # 提取文本框，艺术字内容
    children = document.element.body.iter()
    child_iters = []
    tags = []
    for child in children:
        # 通过类型判断目录
        if child.tag.endswith('textbox'):
            for ci in child.iter():
                tags.append(ci.tag)
                if ci.tag.endswith(('main}r', 'main}pPr')):
                    child_iters.append(ci)
    text = ['']
    for ci in child_iters:
        # print(ci.text)
        if ci.tag.endswith('main}pPr'):
            text.append('')
        else:
            text[-1] += ci.text
        ci.text = ''
    text_box = ""
    for t in text:
        text_box += t + '\n'
    return cell_text+paragraphs_text+text_box

if __name__ == '__main__':
    result = convert_docx_to_txt('D:/myWorkspace/IRAS/footprint/dataset_docx/4.docx')
    print(result)

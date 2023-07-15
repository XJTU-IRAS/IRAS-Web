import os
from .convertion import pdf_parser,docx_parser
from .modules.item import Item
def pdf_process(file_path,output_path):
    print("using pdf_process...")
      # file_name = time.time()
    with open(output_path, 'w',encoding='utf-8') as f:
        f.write(pdf_parser.convert_pdf_to_txt(file_path))
    print("pdf_process finished")
    
def png_process(file_path,output_path):
    print("using png_process...")
    # file_name = time.time()
    cur_item = Item(file_path)
    cur_item.write_itemstrings(output_path)
    print("png_process finished")

def docx_process(file_path,output_path):
    print("using docx_process...")
    # file_name = time.time()
    with open(output_path, 'w',encoding='utf-8') as f:
        f.write(docx_parser.convert_docx_to_txt(file_path))
    print("docx_process finished")

def txt_process(file_path,output_path):
    print("using txt_process...")
    # file_name = time.time()
    with open(file_path,'r',encoding='utf-8') as input:
        with open(output_path, 'w',encoding='utf-8') as output:
            output.write(input.read())
    print("txt_process finished")

import tempfile
import os
def handle_uploaded_file(file,file_name):
    type = file_name.split('.')[-1]
    output_file = tempfile.NamedTemporaryFile(delete=False)
    output_path = output_file.name
    input_file = tempfile.NamedTemporaryFile(delete=False)
    input_path = input_file.name
    input_file.write(file.read())
    try:
        if type =='png':
             png_process(input_path,output_path)
        elif type == 'pdf':
             pdf_process(input_path,output_path)
        elif type == 'docx':
             docx_process(input_path,output_path)
        elif type =='txt':
             txt_process(input_path,output_path)
        else:
             raise Exception('Unknown type: %s' % type)
            # 如果文件类型有误，则会报错
    except Exception as e:
         print(e)
    text = ""
    with open(output_path, 'r',encoding='utf-8') as f:
        text=f.read()
    output_file.close()
    os.remove(output_path)
    input_file.close()
    os.remove(input_path)
    return text
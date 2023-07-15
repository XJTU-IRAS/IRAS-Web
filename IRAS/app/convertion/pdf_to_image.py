from pdf2image import convert_from_path
import os
import tempfile
# The core function calls pdf2image to convert pdf s to png s
# and save the png s in the specified directory
def convert_pdf_to_png(pdf_path,output_path):
    try:
       if not os.path.exists(pdf_path):
            raise IOError("No Such Path: {}".format(pdf_path))
    except IOError as e:
        print (e.message)
    # os.walk(path) returns a three-tuple
    for dir_path,dir_list,file_list in os.walk(pdf_path):
        for file_name in file_list:
            #use tempfile as output_folder to avoid memory usage issues
            with tempfile.TemporaryDirectory() as path:
                images = convert_from_path(os.path.join(pdf_path,file_name),#absolute_pdf_path
                                            output_folder=path, 
                                            dpi=200,# quality of output_image
                                            fmt='png',# the format of the output
                                            thread_count=5# allowed usage of thread
                                            )
                for image in images:
                    if not os.path.exists(output_path):
                        os.makedirs(output_path)

                    prefix = file_name.split('.')[0]
                    # get prefix of the file_name
                    # example: myfile.pdf --> myfile
                    new_path = os.path.join(output_path,prefix)

                    if not os.path.exists(new_path):
                        os.makedirs(new_path)
                        # if path already exists,make directory method will fail and throw error
                    image.save(new_path+'/'+'%s.png' % str(images.index(image)+1), 'PNG')

if __name__ == "__main__":
    # pdf_path ="D:/myWorkspace/IRAS/footprint/dataset_pdf"
    # image_path ="dataset_png"
    pdf_path=""
    output_path =""
    convert_pdf_to_png(pdf_path,output_path)
    
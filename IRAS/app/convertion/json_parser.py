import json 
import os
def get_str_and_coords(input_text):
    # read json file or response_text(String ) from ocrClient
    # return string and coordinates
    try:
        if isinstance(input_text,str):
            json_text = json.loads(input_text.replace("'",'"'))
            # load text from a string
        else:
            json_text = json.load(input_text)
            # load text from a json file 
    except Exception as e:
        raise IOError("get_str_and_coords() method can only receive json file or string")
   
    strs =[]
    coords =[]
    try:
        for item in json_text['items']:
            strs.append(item['itemstring'])
            coords.append(item['itemcoord'])
    except Exception as e:
        if isinstance(e,KeyError):
            print(input_text)
            raise KeyError

    return strs,coords


if __name__ == '__main__':   
    json_path = 'json/1.json'
    try:
        if not os.path.exists(json_path):
            raise IOError("Could not find json file")
    except IOError as e:
        print(e.message)

    json_file = open(json_path,'r',encoding='utf-8')
    get_str_and_coords(json_file)

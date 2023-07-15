from app.convertion.ocr_request import get_response
from app.convertion.json_parser import get_str_and_coords
from app.cluster import cluster
import os
class Item:
    def __str__(self):
        return "Item number: %s" % self.item_num
    def __init__ (self,filepath):
            response = get_response(filepath)
            self.strs,self.coords = get_str_and_coords(response.text)
            self.item_num =len(self.strs)
            self.eig_list,self.eig_num= cluster.get_eig_list_by_coords(self.coords)

    #获得string
    def get_strs(self):
        return self.strs
    
    #获得coords
    def get_coords(self):
        return self.coords
    
    #获得特征值列表，即划分后的组别
    def get_eig_list(self):
        return self.eig_list
    
    def write_itemstrings(self,file_path):
        with open(file_path,"w",encoding='utf=8')as file:
            for i in range(self.eig_num):
                for j in range(self.item_num):
                    if self.eig_list[j]==i:
                        file.write(self.strs[j]+"\n")
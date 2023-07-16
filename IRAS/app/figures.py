from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
import hashlib,time
# 打开文本
def generate_hash(data):
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    return sha256_hash[:24]
def generate_cloud(s):
# 中文分词
    text = ' '.join(jieba.cut(s))
# 生成对象
    wc = WordCloud(font_path="msyh.ttc",
               width=1000,
               height=700,
               background_color='white',
               max_words=200).generate(text)
    filename = generate_hash((str)((int)(time.time())%72637))+".png";
    output_path = r"app/static/app/images/"+filename
    wc.to_file(output_path)
    return filename
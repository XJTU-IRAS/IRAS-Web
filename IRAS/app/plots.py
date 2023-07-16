import matplotlib.pyplot as plt
import pandas as pd
import hashlib,time
# 打开文本
def generate_hash(data):
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    return sha256_hash[:24]
def plot(query_result1):
    df = pd.DataFrame(query_result1, columns=['NUM','EDUCATION'])
    data=df.to_dict('records')
    echarts_data = [{'name': row['EDUCATION'],'value':row['NUM']} for row in data]
    #echarts_data_jason=json.dumps(echarts_data)
    print(echarts_data)
   # print(echarts_data_jason)
    name_data = [item['name'] for item in echarts_data]
    value_data = [item['value'] for item in echarts_data]
    print(name_data)
    print(value_data)
    #print("################################################################")
    # plt.subplot(1,2,1)
    plt.pie(value_data,labels=name_data,autopct='%1.1f%%')
    filename1 = generate_hash((str)((int)(time.time())-232))+".png"
    print(filename1)
    path1 = r"app/static/app/images/"+filename1
    plt.savefig(path1)
    plt.close()
    return filename1

def plot2(query_result2):
    df2=pd.DataFrame(query_result2,columns=['NUM','AGE'])
    data2=df2.to_dict('records')
    echarts_data2 = [{'name': row['AGE'],'value':row['NUM']} for row in data2]
    name_data2 = [item['name'] for item in echarts_data2]
    value_data2 = [item['value'] for item in echarts_data2]
    x=range(len(value_data2))
    # plt.subplot(1,2,2)
    plt.bar(x,value_data2)
    plt.xticks(x,name_data2)
    filename2 = generate_hash((str)((int)(time.time())+32))+".png"
    print(filename2)
    path2 = r"app/static/app/images/"+filename2
    plt.savefig(path2)
    # plt.show()
    plt.close()
    return filename2
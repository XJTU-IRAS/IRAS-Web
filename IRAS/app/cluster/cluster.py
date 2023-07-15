import math 
# from .visualizer import visualize

class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        
    def find(self, k):
        if self.root[k] == k:
            return k
        return self.find(self.root[k])
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x <y:
            self.root[y] = x
        elif x>y:
            self.root[x] = y
        return 
def get_eig_lsit_by_coords_line(coords):
    return 

def get_eig_list_by_coords(coords):
    # coords:{x:12,y:23,width:34,height:65};
    num = len(coords)
    dsu = DSU(num)
    cx=[]
    cy=[]
    diag=[]
    x_list =[]
    y_list =[]
    width_list =[]
    height_list =[]
    
    for coord in coords:
        x = coord['x']
        y = coord['y']
        width = coord['width']
        height = coord['height']
        x_list.append(x)
        y_list.append(y)
        width_list.append(width)
        height_list.append(height)
        cx.append((x+width)/2)
        cy.append((y+height)/2)
        diag.append(math.sqrt(width*width+height*height))
    
    for i in range(num):
        for j in range(i+1,num):
            ref_x = 0.35*min(width_list[i],width_list[j])
            #水平参考量
            ref_y = 1.7*(height_list[i]+height_list[j])//2;
            #竖直参考量 1.7倍平均行距
            nxd = 0 #nearest x distance
            #水平距离，默认水平重合
            nyd = 0
            #竖直距离，默认竖直重合

            #计算水平最近距离
            if x_list[i]<x_list[j]:
                if x_list[i]+width_list[i]<x_list[j]:
                    nxd = x_list[j]-(x_list[i]+width_list[i])
            else:
                if x_list[j]+width_list[j]<x_list[i]:
                    nxd = x_list[i]-(x_list[j]+width_list[j])
             #计算竖直最近距离
            if y_list[i]<y_list[j]:
                if y_list[i]+height_list[i]<y_list[j]:
                    nyd = y_list[j]-(y_list[i]+height_list[i])
            else:
                if y_list[j]+height_list[j]<y_list[i]:
                    nyd = y_list[i]-(y_list[j]+height_list[j])

            # already unioned
            if dsu.find(i)==dsu.find(j):
                continue 
            # check whether the two items can be unioned
          
            if  nyd <ref_y and nxd <ref_x:#在横纵参考量范围内，就认为可以合并
                dsu.union(i,j)
    
    # 在聚类结果中，离散的单点很可能是需要被二次聚类的，把他们归进最近的行
    # 主要考虑到这些单点可能会是标签
    dis_num = 2
    temp =  [dsu.find(i) for i in range(num)] 
    single_items = [i for i in temp if temp.count(i) <=dis_num]
    # print("检测到可疑离群点总数",len(single_items),single_items,sep=' ')
    for i in single_items :
        min_x = 1000000
        code = i 
        for j in range(num):
            if dsu.find(i)==dsu.find(j):
                continue
            else:
                # 计算行间距
                nxd = 0 #nearest x distance
            #水平距离，默认水平重合
                nyd = 0
            #竖直距离，默认竖直重合

            #计算水平最近距离
                if x_list[i]<x_list[j]:
                    if x_list[i]+width_list[i]<x_list[j]:
                        nxd = x_list[j]-(x_list[i]+width_list[i])
                else:
                    if x_list[j]+width_list[j]<x_list[i]:
                        nxd = x_list[i]-(x_list[j]+width_list[j])
             #计算竖直最近距离
                if y_list[i]<y_list[j]:
                    if y_list[i]+height_list[i]<y_list[j]:
                        nyd = y_list[j]-(y_list[i]+height_list[i])
                else:
                    if y_list[j]+height_list[j]<y_list[i]:
                        nyd = y_list[i]-(y_list[j]+height_list[j])
                if nyd > 0.2*height_list[i]:
                    continue
                else :
                    if nxd < min_x and nxd <0.3*max([x_list[i]+width_list[i] for i in range(num)]):
                        min_x = nxd
                        code =j 
        dsu.union(i,code)
    temp =  [dsu.find(i) for i in range(num)] 
    single_items = [i for i in temp if temp.count(i) <=dis_num]
    # print("再次聚类后，剩余离散点总数",len(single_items),single_items,sep=' ')

    #这部分操作是为了使分类总数为5的情况下，用于区分各类的数字在0~4之间
    # get the eig_list after the union process
    eig_list = [dsu.find(i) for i in range(num)] 
    # get the order of all the eigs
    eig_ordered = [i for i in range(num) if i in set(dsu.find(j) for j in range(num))]
    # eig_list normalized to 0~n-1
    for i in range(num):
        eig_list[i] = eig_ordered.index(eig_list[i])
   
    # print("Eig_list: " , len(eig_ordered))
    # print(eig_list)

    # visualize the cluster of items
    # print("Eig_list: " , len(eig_ordered))
    # print(eig_list)

    # visualize(x_list,width_list,y_list,height_list,eig_list)
    egi_num = len(eig_ordered)
    return eig_list,egi_num
    # 返回的是 并查集结果和分类总数
    # e.g. num = 5时
    # eig_list = [0,1,2,2,1]
    # 
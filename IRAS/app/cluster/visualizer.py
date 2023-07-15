import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import time
# Get a List of coordinates and colors 
# Then plot them with the specified colors in one picture 
output_path = "./output_images"
def visualize(x,width,y,height,cols):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')
    for  i in range(len(x)):
        # col = cols[i]/len(x)
        # print(x,width,y,height,sep=' ')
        ax1.add_patch(
            patches.Rectangle(
            (x[i]/2500, y[i]/2500),   # (x,y)
        width[i]/2500,          # width
        height[i]/2500,          # height
        color="C"+str(cols[i])
        )
        )
    now = time.time() #获取时间戳
    fig1.savefig((output_path+'/cluster_output_%s.png'%str(now)), dpi=500, bbox_inches='tight')
from add import *
from set import *




# 示例使用
if __name__ == '__main__':

    fig = plt.figure(figsize=(10, 5))
    proj = ccrs.PlateCarree()
    ax = fig.add_subplot(1, 1, 1, projection=proj)

    # 设置地图的范围
    axism(ax, [70, 140, 15, 55], proj)

    # 设置 x 轴和 y 轴刻度
    xticks(ax, [70, 90, 110, 130], visible=True, loc='bottom', fontname='Arial', fontsize=12)
    yticks(ax, [20, 30, 40, 50], visible=True, loc='left', fontname='Arial', fontsize=12)

    # 读取shp
    china = shaperead(r"D:\Comp_MI\MeteoInfo\map\china.shp")
    geoshow(ax, china, edgecolor='k', linewidth=1, color=None)

    pro = shaperead(r"D:\Comp_MI\MeteoInfo\map\cn_province.shp")
    geoshow(ax, pro, edgecolor='grey', linewidth=0.5, color=None)

    # 自动添加南海脚图
    add_south_sea(ax, r"D:\Comp_MI\MeteoInfo\map\coastline.shp", extent=[110, 120, 5, 15], ratio=1)



    # 显示图形
    plt.show()
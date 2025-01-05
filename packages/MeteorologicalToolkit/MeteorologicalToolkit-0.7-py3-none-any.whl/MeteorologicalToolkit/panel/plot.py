import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from matplotlib.colors import BoundaryNorm
from matplotlib import colorbar as cbar


def imshowm(ax, lon, lat, data, levels=None, cmap=None):
    """
    在给定的 ax 上绘制带 levels 的填色图。

    参数:
    ax (matplotlib.axes.Axes): 目标 Axes 对象。
    lon (numpy.ndarray): 经度数组，形状为 (nlon,) 或 (nlat, nlon)。
    lat (numpy.ndarray): 纬度数组，形状为 (nlat,) 或 (nlat, nlon)。
    data (numpy.ndarray): 数据数组，形状为 (nlat, nlon)。
    levels (list or int, optional): 等值线层级。如果是整数，表示等值线数量；如果是列表，表示具体的等值线值。
    cmap (str or matplotlib.colors.Colormap, optional): 颜色映射。

    返回:
    im (matplotlib.collections.QuadMesh): 填色图对象。
    """
    # 确保 lon 和 lat 是二维数组
    if lon.ndim == 1 and lat.ndim == 1:
        lon, lat = np.meshgrid(lon, lat)  # 将一维经纬度转换为二维网格

    # 获取 ax 的投影
    projection = ax.projection

    # 处理 levels 参数
    if levels is not None:
        if isinstance(levels, int):
            # 如果 levels 是整数，生成等间距的 levels
            levels = np.linspace(np.nanmin(data), np.nanmax(data), levels + 1)
        # 创建 BoundaryNorm 对象，用于离散化数据
        norm = BoundaryNorm(levels, ncolors=256)
    else:
        norm = None  # 如果没有 levels，使用默认的线性归一化

    # 绘制填色图
    im = ax.pcolormesh(lon, lat, data, cmap=cmap, norm=norm, transform=ccrs.PlateCarree())

    return im




def colorbar(im, ax, position=None, shrink=0.7, ticks=None, orientation='horizontal', fontname=None, label=None, tickwidth=1, edgesize=1, ticklen=11, tickin=False, aspect=50, fontsize=12, yshift=0, labelloc='right', x_label_move=0, y_label_move=0):
    """
    为填色图添加颜色条。

    参数:
    im (matplotlib.collections.QuadMesh): 填色图对象（imshowm 返回的对象）。
    ax (matplotlib.axes.Axes): 目标 Axes 对象。
    position (list): 颜色条的位置和大小 [left, bottom, width, height]，默认为右侧。
    shrink (float): 颜色条的缩放比例（仅在 position 为 None 时生效）。
    ticks (list): 颜色条的刻度值。如果为 None，则自动生成刻度。
    orientation (str): 颜色条的方向，支持 'horizontal' 或 'vertical'。
    fontname (str): 刻度标签和标题的字体名称。
    label (str): 颜色条的标题。
    tickwidth (float): 刻度线的宽度。
    edgesize (float): 颜色条边框的宽度。
    ticklen (float): 刻度线的长度。
    tickin (bool): 刻度线是否朝向颜色条内部。
    aspect (float): 颜色条的纵横比。
    fontsize (int): 刻度标签和标题的字体大小。
    yshift (float): 标题的垂直偏移量（仅适用于水平颜色条）。
    labelloc (str): 标题的位置，支持 'left', 'right', 'top', 'bottom'。
    x_label_move (float): 标题在水平方向上的偏移量（仅适用于垂直颜色条）。
    y_label_move (float): 标题在垂直方向上的偏移量（仅适用于水平颜色条）。

    返回:
    cbar (matplotlib.colorbar.Colorbar): 颜色条对象。
    """
    # 如果未指定 position，则使用默认位置
    if position is None:
        bbox = ax.get_position()  # 获取 ax 的位置
        if orientation == 'horizontal':
            position = [bbox.x0, bbox.y0 - 0.04, bbox.width * shrink, 0.02]  # 底部
        else:
            position = [bbox.x1 + 0.02, bbox.y0, 0.02, bbox.height * shrink]  # 右侧

    # 创建颜色条的 Axes
    cax = ax.figure.add_axes(position)

    # 创建颜色条
    cb = plt.colorbar(im, cax=cax, orientation=orientation, ticks=ticks, aspect=aspect)

    # 设置刻度线
    cb.ax.tick_params(width=tickwidth, length=ticklen, direction='in' if tickin else 'out')

    # 关闭小刻度线
    cb.ax.minorticks_off()

    # 设置边框
    for spine in cb.ax.spines.values():
        spine.set_linewidth(edgesize)

    # 设置刻度标签
    if fontname:
        for l in cb.ax.get_xticklabels() + cb.ax.get_yticklabels():
            l.set_fontname(fontname)
            l.set_fontsize(fontsize)

    # 设置标题
    if label:
        if orientation == 'horizontal':
            # 水平颜色条的标题：y_label_move 对应 labelpad
            cb.set_label(label, fontname=fontname, fontsize=fontsize, labelpad=yshift + y_label_move, loc=labelloc)
            # x_label_move 调整水平位置
            label_obj = cb.ax.get_xaxis().label
            label_obj.set_position((label_obj.get_position()[0] + x_label_move, label_obj.get_position()[1]))
        else:
            # 垂直颜色条的标题：x_label_move 对应 labelpad
            cb.set_label(label, fontname=fontname, fontsize=fontsize, labelpad=yshift + x_label_move, loc=labelloc)
            # y_label_move 调整垂直位置
            label_obj = cb.ax.get_yaxis().label
            label_obj.set_position((label_obj.get_position()[0], label_obj.get_position()[1] + y_label_move))

    return cb








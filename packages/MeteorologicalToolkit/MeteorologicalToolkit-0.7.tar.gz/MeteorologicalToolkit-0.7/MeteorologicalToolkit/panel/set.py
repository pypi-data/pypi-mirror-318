import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np


def axism(ax, extent):
    """
    设置地图的显示范围。

    参数：
    ax : matplotlib.axes.AxesSubplot
        地图的轴对象。
    extent : list or tuple
        地图的范围 [lon1, lon2, lat1, lat2]，其中
        lon1, lon2 是经度的范围，lat1, lat2 是纬度的范围。
    proj : cartopy.crs.Projection, optional
        地图的投影，默认使用 PlateCarree 投影。
    """

    projection = ax.projection

    ax.set_extent(extent, crs=projection)


def xticks(ax, values, visible=True, loc='bottom', fontname='Arial', fontsize=10):
    """
    设置经度刻度。

    参数：
    ax : matplotlib.axes.AxesSubplot
        地图的轴对象。
    values : list
        刻度值的列表，如 [80, 100, 120]。
    visible : bool, optional
        是否显示刻度，默认为 True。
    loc : {'bottom', 'top'}, optional
        刻度的显示位置，默认为 'bottom'。
    fontname : str, optional
        刻度标签的字体，默认为 'Arial'。
    fontsize : int, optional
        刻度标签的字体大小，默认为 10。
    """
    if visible:
        ax.set_xticks(values, crs=ccrs.PlateCarree())
        ax.set_xticklabels([f'{i}°E' for i in values], fontname=fontname, fontsize=fontsize)
        if loc == 'bottom':
            ax.tick_params(axis='x', direction='out', labelbottom=True)
        elif loc == 'top':
            ax.tick_params(axis='x', direction='out', labeltop=True)


def yticks(ax, values, visible=True, loc='left', fontname='Arial', fontsize=10):
    """
    设置纬度刻度。

    参数：
    ax : matplotlib.axes.AxesSubplot
        地图的轴对象。
    values : list
        刻度值的列表，如 [30, 40, 50]。
    visible : bool, optional
        是否显示刻度，默认为 True。
    loc : {'left', 'right'}, optional
        刻度的显示位置，默认为 'left'。
    fontname : str, optional
        刻度标签的字体，默认为 'Arial'。
    fontsize : int, optional
        刻度标签的字体大小，默认为 10。
    """
    if visible:
        ax.set_yticks(values, crs=ccrs.PlateCarree())
        ax.set_yticklabels([f'{i}°N' for i in values], fontname=fontname, fontsize=fontsize)
        if loc == 'left':
            ax.tick_params(axis='y', direction='out', labelleft=True)
        elif loc == 'right':
            ax.tick_params(axis='y', direction='out', labelright=True)




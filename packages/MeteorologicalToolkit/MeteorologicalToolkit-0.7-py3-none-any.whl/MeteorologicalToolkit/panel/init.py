import matplotlib.pyplot as plt
import matplotlib as mpl

def set_math_font_italic(italic=True):
    """
    设置全局公式是否斜体。

    参数:
    italic (bool): 如果为 True，全局公式为斜体；如果为 False，全局公式不为斜体。
    """
    if italic:
        # 设置为斜体
        mpl.rcParams['mathtext.default'] = 'it'  # 默认斜体
    else:
        # 设置为非斜体
        mpl.rcParams['mathtext.default'] = 'regular'  # 默认非斜体
from setuptools import setup, find_packages


setup(
    name='MeteorologicalToolkit',  # 包名
    version='0.7',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
    ],
    author='张栩滔',
    author_email='zxt0413363@163.com',
    description='气象数据处理工具箱',
    long_description=open('README.md').read(),  # 从 README.md 中读取描述
    long_description_content_type='text/markdown',  # 指定 README 文件的格式
    url='https://github.com/zhangxutao3/meteorological-toolkit',  # GitHub 项目地址
    classifiers=[
        'Programming Language :: Python :: 3.8',  # 支持的 Python 版本
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',  # 你的开源协议
    ],
    python_requires='>=3.8',
)


from setuptools import setup, find_packages
import os

with open("requirements.txt") as f:
    required = f.read().splitlines()
    
# 读取 README 文件
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = "bio-tfcomb",
    version = "1.0.0a2",
    keywords = ["pip", "tfcomb"],
    description = "TFcomb is a python library to identify reprogramming TFs and TF combinations using scRNA-seq and scATAC-seq data.",
    # long_description = "TFcomb is a python library to identify reprogramming TFs and TF combinations using scRNA-seq and scATAC-seq data.",
    long_description=long_description,  # 将 README 内容作为长描述
    long_description_content_type='text/markdown',  # 指定格式为 Markdown
    license = "MIT License",
    url = "https://github.com/Chen-Li-17/TFcomb",
    author = "Chen Li",
    author_email = "chen-li21@qq.com",
    packages = ['TFcomb'],
    python_requires = ">3.8.0",
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    install_requires=required
)

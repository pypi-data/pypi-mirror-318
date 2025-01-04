from setuptools import setup, find_packages

setup(
    name='hellopackage_wuyouran',  # 包名
    version='0.1.0',   # 版本
    packages=find_packages(),  # 自动发现所有包
    description='A simple package that says hello',  # 包的描述
    long_description=open('README.md').read(),  # 读取 README.md 文件作为长描述
    long_description_content_type='text/markdown',  # 文件格式
    author='wuyouran',  # 作者
    author_email='2719875726@qq.com',  # 作者邮箱 # 项目主页
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python版本要求
)

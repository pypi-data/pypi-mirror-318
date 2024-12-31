# from setuptools import setup, find_packages
#
# setup(
#     name='insta360_lib',
#     version='0.2.8',  #版本号记得增加，打包完记得提交git
#     packages=find_packages(),
#     package_data={
#         'insta360_lib': ['dlls/*.dll', 'dlls/VB/*.dll','dlls/iac3/*.dll'],
#         # 将需要的依赖文件写在这个列表里面
#     },
#     include_package_data=True,
#     install_requires=[
#         "loguru"
#         # 列出你的依赖项
#     ],
#     entry_points={
#         # 如果有命令行工具，可以在这里定义
#     },
#     author='rain',
#     author_email='chenrunming@insta360.com',
#     description='insta360 算法库调用封装库',
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     url='https://gitlab.insta360.com/test2/production-testing-tools/insta360_lib.git',
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
#     python_requires='>=3.7',
# )

from skbuild import setup
from setuptools import find_packages

setup(
    name="insta360_lib",
    version="0.1.4",
    description="Python bindings for sunnyinstaSFR using pybind11",
    author='rain',
    author_email='chenrunming@insta360.com',
    url='https://gitlab.insta360.com/test2/production-testing-tools/insta360_lib.git',
    packages=find_packages(),
    cmake_install_dir="iac_sfr",
    python_requires='>=3.8',
    include_package_data=True,
    package_data={
        "iac_sfr": ["example.py"],  # 包含 example.py 文件
    },
)
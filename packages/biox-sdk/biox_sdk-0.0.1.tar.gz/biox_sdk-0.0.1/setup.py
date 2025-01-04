from setuptools import setup, find_packages

setup(
    name="Biox_SDK",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "bleak>=0.19.0",  # 用于蓝牙通信的异步库
    ],
    python_requires=">=3.7",
    author="qiucheng.su",
    author_email="suqiucheng@zju.edu.cn",
    description="a sdk for connecting with a Biox device",
    keywords="bluetooth, ble, sdk",
) 
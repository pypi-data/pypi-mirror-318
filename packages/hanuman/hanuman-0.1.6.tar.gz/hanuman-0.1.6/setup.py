# setup.py

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hanuman",
    version="0.1.6",
    author="CZHanoi",
    author_email="21301010003@m.fudan.edu.cn",
    description="Typhoon Animation Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CZHanoi/hanuman",
    packages=find_packages(),  # 自动查找包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy",
        "opencv-python",
        "tqdm",
    ],
    entry_points={
        'console_scripts': [
            'hanuman=hanuman.main:main',
        ],
    },
    include_package_data=True,
)

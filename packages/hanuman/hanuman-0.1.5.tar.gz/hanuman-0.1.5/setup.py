# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hanuman",
    version="0.1.5",
    author="CZHanoi",
    author_email="21301010003@m.fudan.edu.cn",
    description="Typhoon Animation Generator",
    long_description_content_type="text/markdown",
    url="https://github.com/CZHanoi/hanuman",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "opencv-python",
        "tqdm",
        # 其他依赖项
    ],
    entry_points={
        'console_scripts': [
            'hanuman=hanuman.main:main',
        ],
    },
    include_package_data=True,
)

from setuptools import setup, find_packages

setup(
    name="exploralytics",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas>=1.3.0',
        'plotly>=5.0.0',
        'numpy>=1.20.0'
    ],
    author="John Paul Curada",
    author_email="johncurada.work@gmail.com",
    description="A toolkit for data exploration and visualization",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jpcurada/exploralytics",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.9",
    keywords="data visualization plotly analytics eda subplot",
    project_urls={
        "Bug Tracker": "https://github.com/jpcurada/exploralytics/issues",
        "Source Code": "https://github.com/jpcurada/exploralytics",
    }
)
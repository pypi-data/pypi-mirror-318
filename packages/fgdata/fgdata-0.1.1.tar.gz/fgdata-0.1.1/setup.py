from setuptools import setup, find_packages

setup(
    name='fgdata',
    version='0.1.1',  
    packages=find_packages(),  # 自动找到所有的包
    include_package_data=True,
    license='MIT',  
    description='A data toolkit for the Chinese futures market.',  
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    author='shuzip',  
    url='https://github.com/shuzip/fgdata',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',  
    install_requires=[
        'requests',
        'pandas',
        'lxml'
    ],
    keywords=[
        "futures",
        "fund",
        "finance",
        "data",
    ],
)
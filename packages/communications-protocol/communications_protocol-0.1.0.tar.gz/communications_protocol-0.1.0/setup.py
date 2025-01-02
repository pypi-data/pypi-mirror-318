from setuptools import setup, find_packages

setup(
    name='communications_protocol',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PySide6',  # 添加其他依赖项
    ],
    author='lhb',
    author_email='spike.edjet@gmail.com',
    description='A package for communication protocol handling',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourproject',  # 项目的URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

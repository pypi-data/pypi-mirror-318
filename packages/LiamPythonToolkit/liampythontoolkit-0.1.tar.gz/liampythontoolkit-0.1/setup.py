from setuptools import setup, find_packages

setup(
    name='LiamPythonToolkit',
    version='0.1',
    packages=find_packages(),
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/your_package',
    install_requires=[
        # 列出你的包依赖的其他包
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
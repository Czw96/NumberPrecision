import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='number_precision',
    version='2020.10.16',
    author='Czzwww',
    author_email='459749926@qq.com',
    description='Python 精度计算',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Czw96/NumberPrecision',
    packages=setuptools.find_packages(exclude=['trash']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

from setuptools import setup, find_packages

setup(
    name='MCFXQ',
    version='0.1.0',
    author='风汐琴',
    author_email='2062479194@qq.com',
    packages=find_packages(),
    license='LICENSE',
    description='低音5到中音5到高音4#的乐器乐谱',
    long_description=open('README.md').read(),
    install_requires=[
        'keyboard'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
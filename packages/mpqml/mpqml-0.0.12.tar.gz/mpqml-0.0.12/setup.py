from setuptools import find_packages, setup
setup(
    name='mpqml',
    version='0.0.12',
    description='machine learning for MPQ_code',
    author='MPQ',#作者
    author_email='miaopeiqi@163.com',
    url='https://github.com/miaopeiqi',
    #packages=find_packages(),
    packages=['mpqml'],  #这里是所有代码所在的文件夹名称
    package_data={
    '':['*.pyd'],
    },
    install_requires=['chardet','scikit-learn','PyWavelets','scipy','mpqlock'],
)

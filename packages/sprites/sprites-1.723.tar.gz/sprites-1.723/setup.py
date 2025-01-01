﻿from setuptools import setup,find_packages

with open("README.md", encoding='utf-8') as fh:
    long_d = fh.read()


setup(name='sprites',
      long_description_content_type="text/markdown",
      version = '1.723',
      description = 'Python Sprites Module for make introductory animations and games and educational purpose。It mainly provides Sprite class inherited from Turtle class。Can be applied to the teaching of elementary mathematics。Pyhton的精灵模块，为教育目的而制作启蒙动画与游戏。主要提供继承自Turtle类的Sprite类,Key类,Mouse类等及一些工具函数,如洪水填充命令,几何相关命令。它支持像素级碰撞检测命令及增强的图章命令等等，也可应用于初等数学几何的教学。作者：李兴球。微信:scratch8，专业编程私教。网址： www.lixingqiu.com',
      long_description = long_d,      
      keywords = 'creative game pygame turtle animation sprite geometry math Elementary Mathematics Teaching',
      url = 'http://www.lixingqiu.com',
      wechat = 'scratch8',
      author ='lixingqiu',
      author_email = '406273900@qq.com',
      license = 'MIT',
      packages = ['sprites'],
      zip_safe = False,
      install_requires = [ 'pillow==9.5.0','numpy==1.21.4']
     )


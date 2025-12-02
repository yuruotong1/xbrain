from setuptools import setup
from xbrain.utils.config import Constants
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyxbrain',
    version= Constants().VERSION,
    description='极简的智能体开发框架',   
    long_description=long_description, 
    long_description_content_type="text/markdown",  
    packages=['xbrain', 'xbrain.core', 'xbrain.utils'],
    zip_safe=False,
    install_requires=[
        'pyyaml==6.0.2',
        'openai==2.8.1',
    ]
)
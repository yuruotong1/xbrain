from setuptools import setup
from xbrain.utils.config import Constants
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyxbrain',
    version= Constants().VERSION,
    description='XBrain通过装饰器将函数接入OpenAI的Chat',
    long_description=long_description, 
    long_description_content_type="text/markdown",  
    packages=['xbrain', 'xbrain.core', 'xbrain.utils'],
    zip_safe=False,
    install_requires=[
        'pyyaml==6.0.2',
        'openai==1.55.3',
    ]
)
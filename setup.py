from setuptools import setup
from xbrain.utils.config import Constants
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyxbrain',
    version= Constants().VERSION,
    description='xbrain专注于构建一款可解释的AI开发框架',
    long_description=long_description, 
    long_description_content_type="text/markdown",  
    packages=['xbrain', 'xbrain.utils', 'xbrain.plugin', 'xbrain.core'],
    zip_safe=False,
    install_requires=[
        'pyyaml==6.0.2',
        'openai==1.48.0',
        'requests==2.32.3',
        'flask==3.0.3',
        'flask-openapi3==3.1.3',
        'gradio==4.44.1',
    ],
    entry_points={
        'console_scripts': [
            'xb = xbrain.main:main',
        ],
    },
)
from setuptools import find_packages, setup
from xbrain.utils.config import Constants
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyxbrain',
    version= Constants().VERSION,
    description='XBrain 是一个让 Python 函数变身为 AI 驱动的 HTTP 服务的超级智能体',
    long_description=long_description, 
    long_description_content_type="text/markdown",  
    packages=['xbrain', 'xbrain.plugin', 'xbrain.core', 'xbrain.utils', 'xbrain.plugin.agent'],
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
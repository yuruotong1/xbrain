from setuptools import setup
 
setup(
    name='xbrain',
    version='1.0.0',
    description='xbrain专注于构建一款可解释的AI开发框架',
    packages=['xbrain'],
    zip_safe=False,
    install_requires=[
        'pyyaml==6.0.2',
        'openai==1.48.0',
        'requests==2.32.3'
    ],
    entry_points={
        'console_scripts': [
            'xb = command.main:main',
        ],
    },
)
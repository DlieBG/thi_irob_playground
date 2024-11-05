from setuptools import find_packages, setup

setup(
    name='png-invert',
    version='0.1.0',
    description='',
    url='https://github.com/DlieBG/thi_irob_playground',
    author='Benedikt Schwering',
    author_email='bes9584@thi.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'click',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'png-invert=src.main:cli',
        ],
    },
)

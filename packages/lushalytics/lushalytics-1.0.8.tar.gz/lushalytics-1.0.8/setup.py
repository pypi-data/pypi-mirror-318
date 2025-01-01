from setuptools import setup, find_packages

setup(
    name='lushalytics',
    version = '1.0.8',
    author='Moran Reznik',
    description = 'tools for quick and convenient data analysis',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'plotly'
    ]
)

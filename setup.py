from setuptools import setup, find_packages

setup(
    name='kml',
    version='1.0',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "kml = kml.main:main",
        ],
    },
    author='Álvaro Aguirre',
    author_email='aaguirreu@utem.cl',
    description='DNA Kmer and Vectorization',
    license='MIT',
)
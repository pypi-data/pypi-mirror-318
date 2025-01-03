from setuptools import setup, find_packages

setup(
    name='edempy_wrapper',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',  # Add any other dependencies your package needs
        'pandas',
        'tqdm',
        'pyvista',
        'imageio'
    ],
    author='Deniz Canbay',
    author_email='decanbay@gmail.com',
    description='A package for analyzing EDEM simulation data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
python_requires='>=3.8,<3.9',
)

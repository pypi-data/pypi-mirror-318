from setuptools import setup, find_packages

# Classifiers for PyPI
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
]

# Read long description from files
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
with open('CHANGELOG.txt', 'r', encoding='utf-8') as f:
    long_description += '\n\n' + f.read()

# Setup function to package the project
setup(
    name='ChemDescriptors',
    version='0.0.2',  # Update version when necessary
    description="Chemical descriptors is a powerful Python package facilitating calculation of fingerprints for CSV files",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AhmedAlhilal14/chemical-descriptors.git',
    author='Ahmed Alhilal',
    author_email='aalhilal@udel.edu',
    license='MIT',
    classifiers=classifiers,
    keywords='Cheminformatics, Molecular Descriptors, Fingerprints, RDKit, Mordred, Padelpy',
    packages=find_packages(),
    install_requires=[
        'rdkit',
        'mordred',
        'pandas',
        'numpy',
        'matplotlib',
        'padelpy',
        "molfeat",
        'matplotlib-venn', 
    ],
)

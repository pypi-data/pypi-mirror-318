from setuptools import setup, find_packages

setup(
    name='EqualClustPath',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scikit-learn'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for balanced K-means clustering and path planning',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/EqualClustPath',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

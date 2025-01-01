from setuptools import setup, find_packages

setup(
    name='EqualClustPath',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scikit-learn'
    ],
    author='Jiawen Hu',
    author_email='dingqi2pi@gmail.com',
    description='A package for balanced K-means++ clustering and path planning',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Wild-Lemon/EqualClustPath',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT'
)
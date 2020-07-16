from setuptools import setup, find_packages

setup(
    name='mimid',
    description='A library for mining grammars from program traces.',
    url='https://github.com/trailofbits/mimid',
    author='Rahul Gopinath and Trail of Bits',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'The Fuzzing Book License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities'
    ]
)

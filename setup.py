from setuptools import setup, find_packages

setup(
    name='iiith-api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'pydantic',
    ],
    author='Sachin Mishra',
    author_email='007mishrasachinmishra@gmail.com',
    description='A simple API for performing operations on numbers.',
    keywords='fastapi, api, numbers',
    url='https://github.com/Imsachin010/iiith-api',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
) 
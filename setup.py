from setuptools import setup, find_packages

setup(
    name='iiith-api',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'fastapi>=0.68.0',
        'uvicorn>=0.15.0',
        'pydantic>=1.8.0',
        'sqlalchemy>=1.4.0',
        'python-jose[cryptography]>=3.3.0',
        'passlib[bcrypt]>=1.7.4',
        'python-multipart>=0.0.5',
        'bcrypt>=3.2.0',
        'python-dotenv>=0.19.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'pytest-cov>=2.12.0',
            'locust>=2.0.0',
            'black>=21.5b2',
            'flake8>=3.9.0',
        ],
    },
    author='Sachin Mishra',
    author_email='imsachin010@gmail.com',
    description='A FastAPI-based secure and performant REST API with authentication and database integration',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='fastapi, api, authentication, sqlalchemy, testing',
    url='https://github.com/Imsachin010/iiith-api',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8',
) 
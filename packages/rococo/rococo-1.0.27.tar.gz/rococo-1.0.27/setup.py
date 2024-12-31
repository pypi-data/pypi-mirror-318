from setuptools import find_packages, setup

setup(
    name='rococo',
    version='1.0.27',
    packages=find_packages(),
    url='https://github.com/EcorRouge/rococo',
    license='MIT',
    author='Jay Grieves',
    author_email='jaygrieves@gmail.com',
    description='A Python library to help build things the way we want them built',
    entry_points={
        'console_scripts': [
            'rococo-mysql = rococo.migrations.mysql.cli:main',
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'surrealdb==0.3.2',
        'boto3>=1.28.55',
        'pika==1.3.2',
        'python-dotenv==1.0.0',
        'PyMySQL==1.1.1',
        'PyMongo==4.6.3'
    ],
    python_requires=">=3.10"
)

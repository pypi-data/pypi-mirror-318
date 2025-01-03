from setuptools import setup, find_packages

setup(
    name='gepeto-core',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pydantic>=2.10.4',
    ],
    author='Uzair',
    author_email='uzair@hellogepeto.com',
    description='pip install gepeto-core',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gepetoai/gepeto-core',
)

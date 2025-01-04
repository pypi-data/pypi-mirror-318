from setuptools import setup, find_packages

setup(
    name='JynAi',
    version='1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'transformers',
        'torch',
    ],
    author='Jynoqtra',
    author_email='Jynoqtra@gmail.com',
    description='JynAi Python Ai Module',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Jynoqtra/JynPopMod',
    classifiers=[  
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Intended Audience :: Developers',
    ],
)

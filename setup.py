import setuptools

setuptools.setup(
    name='github-grasp',
    version='0.0.1',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='Get single files from any public repository onto your computer',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://gadhagod.github.io/github-grasp',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=['click'],
    scripts=['./bin/ghg'],
    python_requires='>=3.6'
)
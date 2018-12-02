from setuptools import setup

setup(
    name='markdown-code-blocks',
    description='Generate html from markdown with code-block highlighting',
    url='https://github.com/asottile/markdown-code-blocks',
    version='1.3.0',
    author='Anthony Sottile',
    author_email='asottile@umich.edu',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=['mistune', 'pygments'],
    py_modules=['markdown_code_blocks'],
    entry_points={'console_scripts': [
        'markdown-code-blocks-highlight=markdown_code_blocks:main',
    ]},
)

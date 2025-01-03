from setuptools import setup, find_packages

setup(
    name='CTkSimpleMessagebox',
    version='1.2.0',
    author='Scott',
    author_email='ctksimplemessagebox@gmail.com',
    description='Python Messagebox to display current Infos or Errors.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NotScottt/CTkSimpleMessageboxes',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

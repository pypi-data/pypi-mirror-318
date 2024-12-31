from setuptools import setup, find_packages

setup(
    name='dataanalysts',
    version='0.1.0',
    description='A basic Python data analysis library.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Venkata Govind Neelapu',
    author_email='venkatagovindneelapu@gmail.com',
    license='MIT',
    url='https://github.com/yourusername/dataanalysts',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scikit-learn'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='yemot-ai',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'yemot',
        'yemot-flow',
    ],
    url='https://github.com/davidTheDeveloperY/yemot-ai',
    author='davidTheDeveloper',
    author_email='bc98400@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    extras_require={
        'advanced': ['pytest'],
    },
    python_requires='>=3.8',
    description='a tool for processing data and recordings for the Yemot API',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
    

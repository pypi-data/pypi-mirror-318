from setuptools import setup, find_packages

setup(
    name='ultraclean',
    version='0.1.0-alpha',
    license="MIT License with attribution requirement",
    author="Ranit Bhowmick",
    author_email='bhowmickranitking@duck.com',
    description='UltraClean is a fast and efficient Python library for cleaning and preprocessing text data for AI/ML tasks and data processing.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Kawai-Senpai/UltraClean',
    download_url='https://github.com/Kawai-Senpai/UltraClean',
    keywords=["Text Cleaning", "Data Preprocessing", "AI", "ML", "Spam Detection"],
    install_requires=[
        'transformers>=4.0.0',  # For spam detection model
        'torch>=1.7.0',         # For PyTorch support
        'emoji>=1.2.0',         # For emoji handling
        'tf-keras>=2.6.0',      # For TensorFlow Keras compatibility
    ],
    python_requires='>=3.7',
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-asyncio>=0.21.0',  # For testing async features
            'black>=22.0.0',
            'mypy>=0.900',
            'flake8>=4.0.0',
        ],
        'docs': [
            'sphinx>=4.0.0',
            'sphinx-rtd-theme>=1.0.0',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Typing :: Typed',
    ],
)

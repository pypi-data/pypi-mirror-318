from setuptools import setup, find_packages

setup(
    name='stats_calculator',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple package for calculating mean and standard deviation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://www.example.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # 这里没有额外依赖，可根据实际情况添加
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            # 可根据需要添加命令行入口，这里暂未添加复杂功能的入口
        ],
    },
)

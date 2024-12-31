from setuptools import setup, find_packages

setup(
    name='math_calculator_ahd',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 列出你的项目依赖，例如：
        # 'numpy>=1.18.1',
    ],
    author='akida2002',
    author_email='aihedan_1122@qq.com',
    description='A simple math calculator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/math_calculator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

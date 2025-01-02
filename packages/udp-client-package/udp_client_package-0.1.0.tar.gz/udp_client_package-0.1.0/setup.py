from setuptools import setup, find_packages

setup(
    name='udp_client_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PySide6',  # 添加其他依赖项
    ],
    entry_points={
        'console_scripts': [
            # 如果需要创建命令行工具，可以在这里定义
        ],
    },
    author='lhb',
    author_email='spike.edjet@gmail.com',
    description='一个简单的UDP客户端API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://你的项目网址',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

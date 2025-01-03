from setuptools import setup, find_packages

setup(
    name='time_update',  # 包名
    version='0.1',  # 版本号
    packages=find_packages(),  # 自动查找包
    install_requires=[  # 依赖项
        'requests',
    ],
    author='kongchujun',
    author_email='98514515@qq.com',
    description='Help to solve the time formate',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-repo',  # 项目URL
    classifiers=[  # 分类信息
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',  # Python版本要求
)

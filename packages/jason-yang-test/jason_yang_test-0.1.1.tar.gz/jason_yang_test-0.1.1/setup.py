from setuptools import setup, find_packages

# 读取 README.md 的内容作为长描述
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='jason_yang_test',                # 包名
    version='0.1.1',           # 版本号
    author='jason',        # 作者名
    author_email='3544909637@qq.com',  # 作者邮箱
    description='一个简单的Python工具包',    # 简短描述
    long_description=long_description,      # 长描述
    long_description_content_type="text/markdown",  # 长描述的格式
    url='https://github.com/yourusername/yang',    # 项目主页
    packages=find_packages(),   # 自动找到所有包
    classifiers=[              # 包的分类信息
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',   # Python版本要求
    install_requires=[         # 依赖项
        # 如果有依赖包，在这里列出，例如：
        # 'requests>=2.25.1',
    ],
    entry_points={             # 命令行工具入口点
        'console_scripts': [
            'yang-calc=yang.test:show_result',  # 修改为实际存在的函数
            'yang-hello=yang.__init__:hello_world',
        ],
    },
)

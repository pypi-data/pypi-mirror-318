from setuptools import setup, find_packages

setup(
    name="ggguan_2025",  # 包名称（在PyPI上唯一）
    version="1.0.0",  # 初始版本号
    author="Emoli",  # 作者名称
    author_email="2586132625@qq.com",  # 作者邮箱
    description="miaomiaomiao.",  # 简短描述
    long_description=open("README.md", "r", encoding="utf-8").read(),  # 从README.md加载长描述
    long_description_content_type="text/markdown",  # 长描述内容类型
    url="https://github.com/ggguan0314/ggguan_2025",  # 项目主页链接
    packages=find_packages(),  # 自动查找所有包
    include_package_data=True,  # 包含附加的静态文件
    install_requires=[
        "matplotlib>=3.0",
        "numpy>=1.0",
    ],  # 列出依赖
    python_requires=">=3.6",  # 支持的Python版本
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "new_year_2025_visual=new_year_2025_visual.main:NewYearApp",  # 命令行入口
        ],
    },
)

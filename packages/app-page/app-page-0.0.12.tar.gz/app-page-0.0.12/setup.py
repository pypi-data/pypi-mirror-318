import setuptools

package_name = "app-page"
version = '0.0.12'
long_description = open("README.md", encoding="utf-8").read()

setuptools.setup(
    name=package_name,
    version=version,
    author="xiaohuicat",  # 作者名称
    author_email="1258702350@qq.com", # 作者邮箱
    description="python page application framework", # 库描述
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xiaohuicat/python-app-page", # 库的官方地址
    license="MIT",
    packages=setuptools.find_packages(),
    package_data={'app_page': ['*', 'assets/*', 'assets/*/*']},
    install_requires=[
        "PySide6",
        "nanoid",
        "app-page-core"
    ],
    zip_safe=False,
)
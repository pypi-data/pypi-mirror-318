import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ttkplus",
    version="0.0.2",
    author="iamxcd",
    description="TkinterHelper布局助手桌面版 官方拓展和工具库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.pytk.net",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8"
)

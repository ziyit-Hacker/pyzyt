import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="ziyit",
  version="1.1.1",
  author="Deng Yichen",
  author_email="3960140506@qq.com",
  description="The developer is from China. This package contains many tools, and if there are no built-in modules, you can download this package.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/pypa/sampleproject",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Windows",
  ],
)

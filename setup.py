from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in wap/__init__.py
from wap import __version__ as version

setup(
	name="wap",
	version=version,
	description="Whatsapp Integration",
	author="Thirvusoft Private Limited",
	author_email="thirvusoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

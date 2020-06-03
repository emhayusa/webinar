import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
	
setuptools.setup(
	name='webinar',
	version='0.2',
	author="Muhammad Hasannudin Yusa",
	author_email="emhayusa@gmail.com",
	description="A webinar bot package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/emhayusa/webinar",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		],
	install_requires=[
        'Click',
    ],
	entry_points={
        "console_scripts": ['webinar=webinar.main:hello']
    },
 )
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='base64tool',  
     version='0.3',
     scripts=['base64tool'] ,
     author="Kumari Aishwarya",
     author_email="k.aishwarya15@gmail.com ",
     description="A tool to encode decode Base64",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/k-aishwarya/Base64Tool",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
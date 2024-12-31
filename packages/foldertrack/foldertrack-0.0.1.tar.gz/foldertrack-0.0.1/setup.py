from setuptools import setup, find_packages

setup(name = "foldertrack",
      version="0.0.1",
      author="Gabriela A. Torres",
      author_email="gabi.torres@gmail.com",
      description="Package to maneger pacient records from a ESF, strategy of brasilian health.",
      long_description= "foldertrack_project/README.md",
      packages= find_packages(),
      install_requires = "pandas"
)

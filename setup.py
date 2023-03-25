from setuptools import setup, find_packages

setup(name='cmb_footprint',
      version='1.0',
      description='Visualize sky survey regions.',
      author='N. Miller, and [others]',
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      package_data={
        "cmb_footprint": ["*.cfg", "data/*.cfg", "data/maps/*"]
      },
      python_requires=">=3.7",
      install_requires=[
        "numpy>=1.21", # for npt.NDArray
        "astropy>='3.2.0",
        "matplotlib",
        "scipy",
        "healpy",
      ],
      )
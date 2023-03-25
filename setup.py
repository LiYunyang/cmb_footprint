from setuptools import setup, find_packages

setup(name='cmb_footprint',
      version='1.0',
      description='Visualize sky survey regions.',
      author='N. Miller, and [others]',
      package_dir = {'cmb_footprint' : 'src'},
      packages=['cmb_footprint'],
      python_requires=">=3.7",
      install_requires=[
        "numpy>=1.21", # for npt.NDArray
        "astropy>='3.2.0",
        "matplotlib",
        "scipy",
        "healpy",
      ],
      )
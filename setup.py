from setuptools import setup, find_packages


setup(
    name='card_pack_simulation',
    version='1.0.0',
    license='MIT',
    author="Timothy Perera",
    author_email='timothyperera.m@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/TimPerera/CardPackSimulation.git',
    keywords='card deck pack player',
    install_requires=[
          'scikit-learn',
      ],

)
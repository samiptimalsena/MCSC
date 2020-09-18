from distutils.core import setup
setup(
  name = 'MCSC',        
  packages = ['MCSC'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package for solving MCSC problems.',   # Give a short description about your library
  author = 'Samip Timalsena',                   # Type in your name
  author_email = 'samip425@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/samiptimalsena/MCSC',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/samiptimalsena/MCSC/archive/v_03.tar.gz',    # I explain this later on
  keywords = ['MCSC', 'KATHMANDU UNIVERSITY', 'Algorithms'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'prettytable',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',    
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',
  ],
)
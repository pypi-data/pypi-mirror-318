from setuptools import setup
import pypandoc

try:
    long_description = pypandoc.convert_file('README.md', 'rst')
    long_description = long_description.replace("\r","") # Do not forget this line
except OSError:
    print("Pandoc not found. Long_description conversion failure.")
    import io
    # pandoc is not installed, fallback to using raw contents
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

setup(
    name='tdone',
    version='0.1.2',
    long_description=long_description,    
    description='TD ONE: A Python Package for Banking and Pricing',
    url='https://github.com/tpdrg/tdone',
    author='Behrang Dadsetan',
    author_email='behrang.dadsetan@tpdrg.com',
    license='BSD 2-clause',
    packages=['tdone'],
    install_requires=['pika>=1.3.2',                  
                      ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Operating System :: Microsoft :: Windows',        
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
)
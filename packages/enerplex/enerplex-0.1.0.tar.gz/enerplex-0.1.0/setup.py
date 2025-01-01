import setuptools
from enerplex import __version__ as version

setuptools.setup(
    name='enerplex',
    version=version,
    description='Enerplex API Client',
    long_description=open('README.md').read().strip(),
    long_description_content_type='text/markdown',  # Ensures markdown is rendered correctly on PyPI
    author='Noel Schwabenland',
    author_email='noel@lusi.uni-sb.de',
    url='https://github.com/NoxelS/enerplex-api-client',
    py_modules=[],
    install_requires=[
        'requests>=2.25.0',
        'python-dotenv>=1.0.0'
    ],
    license='MIT License',
    zip_safe=False,
    keywords='energen enerplex',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering',
    ],
    python_requires='>=3.8',
)

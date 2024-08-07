"""Setup script for Cython."""

from pathlib import Path

from Cython.Build import cythonize
from setuptools import Extension, setup

src = [str(p) for p in Path('model_xpto').glob('*.py')]
extensions = [
    Extension(
        'model_xpto',  # module name resulting from the conversion
        sources=src,  # python file to be converted
        language='c++',
    ),  # used language for the conversion (C++ to support classes and strings)
]

setup(ext_modules=cythonize(extensions))

from setuptools import setup, Extension
from Cython.Build import cythonize
import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

ext_modules = [
    Extension(
        "Metamorphic.MorphAlyt.MorphAlyt",
        sources=[os.path.join(ROOT_DIR, "Metamorphic", "MorphAlyt", "MorphAlyt.pyx")]
    ),
    Extension(
        "Metamorphic.MorphSign.MorphSign",
        sources=[os.path.join(ROOT_DIR, "Metamorphic", "MorphSign", "MorphSign.pyx")]
    )
]

setup(
    name="Metamorphic",
    version="0.2.2",
    description="Elliptic curve operations using SageMath",
    long_description_content_type="text/markdown",
    author='fourchains_R&D',
    author_email='fourchainsrd@gmail.com',
     packages=["Metamorphic", "Metamorphic.MorphAlyt", "Metamorphic.MorphSign"],
    ext_modules=cythonize(
        ext_modules,
        compiler_directives={"language_level": "3"}  
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Cython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data={
        "Metamorphic": ["data/*.csv"], 
    },
    #package_data={
    #    "MetaMorphic": ["*.pxd", "*.c", "*.h", "*.pyd"],
    #},
    #exclude_package_data={
    #    "MetaMorphic": ["*.py", "*.pyx"],  # .py와 .pyx 파일 제외
    #},
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "numpy",
        "scipy",
        "sympy",
        "matplotlib",
        "seaborn",
    ],
)


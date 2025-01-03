from setuptools import setup, Extension
from Cython.Build import cythonize

'''
ext_modules = [
    Extension(
        "Metamorphic.MorphAlyt.MorphAlyt",
        sources=["Metamorphic/MorphAlyt/MorphAlyt.pyx"]  
    ),
    Extension(
        "Metamorphic.MorphSign.MorphSign",
        sources=["Metamorphic/MorphSign/MorphSign.pyx"]
    ),
    Extension(
        "Metamorphic.MorphEnc.MorphEnc",
        sources=["Metamorphic/MorphEnc/MorphEnc.pyx"]
    )
]

'''
ext_modules = [
    Extension(
        "Metamorphic.MorphAlyt.MorphAlyt",
        sources=["Metamorphic/MorphAlyt/MorphAlyt.c"]  # .pyx 대신 .c 파일 사용
    ),
    Extension(
        "Metamorphic.MorphSign.MorphSign",
        sources=["Metamorphic/MorphSign/MorphSign.c"]
    ),
    Extension(
        "Metamorphic.MorphEnc.MorphEnc",
        sources=["Metamorphic/MorphEnc/MorphEnc.c"]
    )
]
#'''

setup(
    name="Metamorphic",
    version="0.2.9",
    description="Elliptic curve operations using SageMath",
    long_description_content_type="text/markdown",
    author='fourchains_R&D',
    author_email='fourchainsrd@gmail.com',
     packages=["Metamorphic", "Metamorphic.MorphAlyt", "Metamorphic.MorphSign", "Metamorphic.MorphEnc"],
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
        "Metamorphic": ["data/*.csv", "MorphAlyt/*.c", "MorphSign/*.c", "MorphEnc/*.c"], 
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


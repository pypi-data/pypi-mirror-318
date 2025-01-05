import setuptools

setuptools.setup(
    name="minekuai",
    version="0.0.4",
    author="SCH",
    description="minekuai request library",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    py_modules=['minekuai'],
    package_dir={'minekuai': 'minekuai'},
)
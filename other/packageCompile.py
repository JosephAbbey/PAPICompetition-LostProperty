import setuptools

setuptools.setup(
    name='serverLib',
    version='0.2.2',
    author='Benjamin Jones',
    description='The core library for the LostProperty project',
    license='MIT',
    install_requires=["flask"],
    packages=setuptools.find_packages(include=['serverLib']),
    python_required=">=3.7"
)
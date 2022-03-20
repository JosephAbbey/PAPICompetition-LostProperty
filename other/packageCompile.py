import setuptools

setuptools.setup(
    name='serverLib',
    version='0.2.3',
    author='Benjamin Jones',
    description='The core library for the LostProperty project',
    license='MIT',
    install_requires=["flask"],
    packages=setuptools.find_packages(include=['serverLib']),
    python_required=">=3.7"
)

# python packageCompile.py bdist_wheel
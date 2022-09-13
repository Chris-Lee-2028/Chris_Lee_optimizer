from setuptools import find_packages, setup

setup(
    name='feloopy',
    packages=find_packages(include=['feloopy']),
    version='0.0.3',
    description='FelooPy: An Integrated Optimization Environment',
    author='Keivan Tafakkori',
    license='MIT',
    install_requires=['pyomo','pulp','gekko','ortools'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
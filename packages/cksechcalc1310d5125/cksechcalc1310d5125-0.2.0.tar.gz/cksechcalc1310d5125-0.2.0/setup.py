from setuptools import setup, find_packages

# name can not have hyphens or underscores
setup(
    name='cksechcalc1310d5125',
    version='0.2.0',
    packages=find_packages(),
    description='Calcluator package to test packaging and distribution.',
    author='Trainer',
    author_email='lms@echios.com',
    license='MIT',
    python_requires='>=3.6',
)

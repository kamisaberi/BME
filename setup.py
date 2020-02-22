from setuptools import setup, find_packages
setup(
    name='bme',
    version='0.0.1',
    packages=['include'],
    data_files=['resources', 'resources.database', 'resources.templates'],
    package_data={'': ['*.json']},
    url='',
    license='gpl3',
    author='kami',
    author_email='kamisaberi@yahoo.com',
    description='back-end management engine'
)

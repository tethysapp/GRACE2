from setuptools import setup, find_namespace_packages
from setup_helper import find_resource_files

# -- Apps Definition -- #
app_package = 'newgrace'
release_package = 'tethysapp-' + app_package

# -- Get Resource File -- #
resource_files = find_resource_files('tethysapp/' + app_package + '/templates', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/public', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/workspaces', 'tethysapp/' + app_package)


### Python Dependencies ###
dependencies = []

setup(
    name=release_package,
    version='2.0.0',
    description='The GRACE application is a visualization tool for GRACE global satellite data. It also provides visualization for global surface water, soil moisture, and groundwater data.',
    long_description='',
    keywords='',
    author='Travis McStraw',
    author_email='travis.mcstraw@gmail.com',
    url='',
    license='',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies
)

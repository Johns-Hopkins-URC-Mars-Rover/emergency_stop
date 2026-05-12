from setuptools import find_packages, setup

package_name = 'emergency_stop'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='katharinehsu',
    maintainer_email='katharinekhsu@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
                'signal_publisher = emergency_stop.signal_publisher:main',
                'signal_subscriber = emergency_stop.signal_subscriber:main',
        ],
    },
)

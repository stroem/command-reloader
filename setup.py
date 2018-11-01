from setuptools import find_packages, setup

setup(
    name='reloadcmd',
    version='0.9.0',

    description='Reload command on file changed',
    long_description=open("README.rst").read(),

    author='Jonathan Strom',
    author_email='jonathan.strom@gmail.com',
    url='https://github.com/stroem/python-reloadcmd',
    license='MIT License',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=[
        'coloredlogs',
        'watchdog',
    ],

    entry_points={
        'console_scripts': [
            'reloadcmd=reloadcmd.__main__:main',
        ],
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)

from setuptools import setup, find_packages

setup(
    name='seam-nrp',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',  # Add other dependencies if needed
    ],
    entry_points={
        'console_scripts': [
            'seam-create-demo=seam_nrp.demo:create_demo',  # Allow command-line execution of create_demo if needed
        ]
    },
)


from setuptools import setup, find_packages

setup(
    name='energy_tariff_scheduler',
    version='0.0.0',
    author='Craig White',
    author_email='dev.craigw@gmail.com',
    description='Schedule actions based on energy tariffs',
    packages=find_packages(exclude=["__tests__"]),
    install_requires=[
        "pydantic==2.10.4",
        "requests==2.32.3",
        "python-dateutil==2.9.0.post0",
        "apscheduler==3.11.0"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
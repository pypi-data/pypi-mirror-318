from setuptools import setup, find_packages

setup(
    name='lightweight_chess_engine',
    version='0.1.0',
    packages=find_packages(),
    package_data={
        'lightweight_chess_engine': ['binaries/bbc_1_engin'],  # تضمين الملف الثنائي
    },
    include_package_data=True,
    python_requires='>=3.6',
    description='A lightweight chess engine library for Linux.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lecheheb djaafar',
    author_email='djaafardjaafarlolo@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
    ],
)

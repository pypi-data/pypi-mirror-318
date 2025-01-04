from setuptools import setup, find_packages

setup(
    name='game_package',
    version='0.0.1',
    description="sudoku to solve",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'game_package=game_package.main:play',
        ],
    },
    author='-sudoku',
    url='https://github.com/anurag9601/pip-sudoku.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3',
)

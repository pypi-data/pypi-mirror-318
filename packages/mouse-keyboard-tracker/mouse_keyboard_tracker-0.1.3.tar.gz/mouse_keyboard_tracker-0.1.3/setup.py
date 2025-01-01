from setuptools import setup, find_packages

setup(
    name='mouse_keyboard_tracker',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'pynput',
    ],
    entry_points={
        'console_scripts': [
            'mouse-keyboard-tracker=mouse_keyboard_tracker.cli:main',
        ],
    },
    author='Victor L. Castro',
    author_email='victorlcastro.dsa@gmail.com',
    description='Uma biblioteca para monitorar atividades de teclado e mouse.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/victorlcastro-dsa/mouse-keyboard-tracker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
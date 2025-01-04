from setuptools import setup, find_packages

setup(
    name="exobanana-todo-app",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "todo-cli=todo:main",
        ],
    },
)

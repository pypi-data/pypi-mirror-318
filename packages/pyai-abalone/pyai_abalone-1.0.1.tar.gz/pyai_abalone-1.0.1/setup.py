from pathlib import Path
import setuptools
import os

src_path = "src"
packages = setuptools.find_namespace_packages(where=src_path)
project_name = os.environ.get("PROJECT_NAME", "pyai_abalone")
module_name = project_name.replace("-", "_")

setuptools.setup(
    name=module_name,
    version=os.environ.get("VERSION", "1.0.1"),
    author=os.environ.get("AUTHOR", "Harald Locke"),
    author_email=os.environ.get(
        "AUTHOR_EMAIL", "haraldlocke@gmx.de"),
    description="AI abalone player based on Alpha-Zero's concept with GUI",
    url="https://github.com/harloc-AI/pyai_abalone",
    project_urls={
        "Source Code": "https://github.com/harloc-AI/pyai_abalone",
    },
    packages=packages,
    package_dir={
        "": src_path,
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=open("requirements.txt", "r").read().split(),
    # include_package_data=True,
    package_data={
        "pyai_abalone.ai_files": ["*.h5", "*.json"],
        "pyai_abalone.images": ["*.png"]
        },
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
)

# mypy: disable-error-code="import-untyped"
#!/usr/bin/env python
"""Setup script for the project."""

import os
import re
import shutil
import subprocess

from setuptools import find_packages, setup
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py
from setuptools_rust import Binding, RustExtension

with open("README.md", "r", encoding="utf-8") as f:
    long_description: str = f.read()

with open("Cargo.toml", "r", encoding="utf-8") as fh:
    version_re = re.search(r"^version = \"([^\"]*)\"", fh.read(), re.MULTILINE)
assert version_re is not None, "Could not find version in Cargo.toml"
version: str = version_re.group(1)

with open("krec/requirements.txt", "r", encoding="utf-8") as f:
    requirements: list[str] = f.read().splitlines()

with open("krec/requirements-dev.txt", "r", encoding="utf-8") as f:
    requirements_dev: list[str] = f.read().splitlines()


class RustBuildExt(build_ext):
    def run(self) -> None:
        # Generate the stub file
        subprocess.run(["cargo", "run", "--bin", "stub_gen", "--package", "bindings"], check=True)

        # Move the generated stub file to parent directory
        src_file = "krec/bindings/bindings.pyi"
        dst_file = "krec/bindings.pyi"
        if os.path.exists(src_file) and not os.path.exists(dst_file):
            shutil.move(src_file, dst_file)
        if not os.path.exists(dst_file):
            raise RuntimeError(f"Failed to generate {dst_file}")
        if os.path.exists(src_file):
            os.remove(src_file)

        super().run()


class CustomBuild(build_py):
    def run(self) -> None:
        self.run_command("build_ext")
        super().run()


setup(
    name="krec",
    version=version,
    description="Python bindings for K-Scale recordings",
    author="K-Scale Labs",
    url="https://github.com/kscalelabs/krec",
    rust_extensions=[
        RustExtension(
            target="krec.bindings",
            path="krec/bindings/Cargo.toml",
            binding=Binding.PyO3,
        ),
    ],
    setup_requires=["setuptools-rust"],
    install_requires=requirements,
    extras_require={"dev": requirements_dev},
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    include_package_data=True,
    packages=find_packages(include=["krec"]),
    cmdclass={
        "build_ext": RustBuildExt,
        "build_py": CustomBuild,
    },
)

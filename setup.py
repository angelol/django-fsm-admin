import os
import subprocess

import setuptools

remote_version = subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()

if "-" in remote_version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v, i, s = remote_version.split("-")
    remote_version = v + "+" + i + ".git." + s

assert "-" not in remote_version
assert "." in remote_version

assert os.path.isfile("fsm_admin/version.py")
with open("fsm_admin/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % remote_version)

readme = open("README.md").read()

setuptools.setup(
    name="django-fsm-2-admin",
    version=remote_version,
    author="Coral.li",
    description="Integrate django-fsm-2 state transitions into the django admin",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="dev@coral.li",
    url="https://github.com/coral-li/django-fsm-2-admin",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=4.2",
        "django-fsm-2>=3.0.0",
    ],
    keywords="django fsm admin",
    license="MIT",
    platforms=["any"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

from setuptools import find_packages, setup

entry_point = (
    "metro-sp-mdp = metro_sp_mdp.__main__:main"
)


# get the dependencies and installs
with open("requirements.txt", encoding="utf-8") as f:
    # Make sure we strip all comments and options (e.g "--extra-index-url")
    # that arise from a modified pip.conf file that configure global options
    # when running kedro build-reqs
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()
        if req and not req.startswith("--"):
            requires.append(req)

setup(
    name="metro_sp_mdp",
    version="2.0.1",
    url="https://github.com/thiagodsd/metro-sp-mdp",
    author="thiagodsd",
    author_email="thiagodsd@thiagodsd.com",
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": [entry_point]},
    install_requires=requires,
    extras_require={
        "docs": [
            "docutils<0.18.0",
            "sphinx~=3.4.3",
            "sphinx_rtd_theme==0.5.1",
            "nbsphinx==0.8.1",
            "nbstripout~=0.4",
            "recommonmark==0.7.1",
            "sphinx-autodoc-typehints==1.11.1",
            "sphinx_copybutton==0.3.1",
            "ipykernel>=5.3, <7.0",
        ]
    },
)

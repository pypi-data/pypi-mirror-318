# Badges Gitlab

![Pypi Version](https://img.shields.io/pypi/v/badges-gitlab)
![Status](https://img.shields.io/pypi/status/badges-gitlab)
![Python Version](https://img.shields.io/pypi/pyversions/badges-gitlab)
![License](https://gitlab.com/felipe_public/badges-gitlab/-/jobs/artifacts/main/raw/public/badges/license_name.svg?job=badges)
![Coverage](https://gitlab.com/felipe_public/badges-gitlab/badges/main/coverage.svg?job=coverage)
![Pipeline](https://gitlab.com/felipe_public/badges-gitlab/badges/main/pipeline.svg)
[![Documentation Status](https://readthedocs.org/projects/badges-gitlab/badge/?version=latest)](https://badges-gitlab.readthedocs.io/en/latest/?badge=latest)




This project was created to generate badges for Gitlab in CI jobs, mainly for private repositories where
other common methods are not available (direct API Calls, shields.io, etc...).

By default, Gitlab supports only two types of badges: pipeline and test coverage.

These badges are better detailed at: [Gitlab Project Badges](https://docs.gitlab.com/ee/user/project/badges.html).

## Installation

You can install this package from pypi using pip.

```bash
$ pip install badges-gitlab
```
    
## General Usage
```console
usage: badges-gitlab [-h] [-p PATH] [-t TOKEN] [--junit-xml FILE_PATH] [-s LABEL MESSAGE COLOR] 
[-lb URLS [URLS ...]] [-V]

Generate Gitlab Badges using JSON files and API requests. Program version v0.0.0.

optional arguments:
  -h, --help            show this help message and exit
  -p TEXT, --path TEXT  path where json and badges files will be generated/located (default: ./public/badges/)
  -t TEXT, --token TEXT specify the private-token in command line (default: ${PRIVATE_TOKEN})
  --junit-xml TEXT      specifies the path of a JUnit XML file for parsing the test results
  -s LABEL MESSAGE COLOR, --static-badges LABEL MESSAGE COLOR
                        specify static badges in command line using lists
 -lb URLS [URLS ...], --link-badges URLS [URLS ...]
                        specify shields.io urls to download badges
  -V, --version         returns the package version
```
## Author

Felipe Pinheiro Silva

### Contributors

Benjamin Maréchal (irmo322)

## Further Documentation

Slowly moving documentation to [ReadTheDocs](https://badges-gitlab.readthedocs.io/).


## HOKUSAI [![CircleCI](https://circleci.com/gh/artsy/hokusai/tree/main.svg?style=svg)](https://circleci.com/gh/artsy/hokusai/tree/main)

<a href="https://en.wikipedia.org/wiki/Hokusai"><img height="300" src="hokusai.jpg"></a>

Hokusai is a Docker + Kubernetes CLI for application developers.

Hokusai "dockerizes" applications and manages their lifecycle throughout development, testing, and release cycles.

Hokusai wraps calls to [Kubectl](https://kubernetes.io/), [Docker](https://www.docker.com/), [Docker-Compose](https://docs.docker.com/compose/) and [Git](https://git-scm.com/) with a CLI, and defines a CI workflow.

Hokusai currently only supports Kubernetes deployments on AWS, configured to pull from ECS container repositories (ECR), although other providers may be added in the future.

### Why Hokusai?

At [Artsy](http://www.artsy.net), as we began working with Kubernetes, while impressed with its design, capabilities, and flexibility, we were in need of tooling we could deliver to agile development teams that addressed the day-to-day tasks of application development, delivery, introspection and maintenance, while providing a clean and uncomplicated interface.

Transitioning teams to the Docker / Kubernetes ecosystem can be intimidating, and comes with a steep learning curve. We set out to create a Heroku-like CLI that would shepherd the application developer into the ecosystems of Docker and Kubernetes, and while introducing new tooling and concepts, outlining a clear practice for dependency management, local development, testing and CI, image repository structure, deployment and orchestration.


## Installation

### MacOS

We recommend installing via Homebrew:

```
$ brew update
$ brew tap artsy/formulas
$ brew install hokusai
```

If you previously installed Hokusai via an alternate installation method, you may need to force the `link` step.

```
$ brew link --overwrite hokusai
```

If you previously installed Hokusai via Pip, you may want to first uninstall it:

```
$ pip uninstall hokusai
```

### Linux

```
curl -sSL https://raw.githubusercontent.com/artsy/hokusai/main/get-hokusai.sh | sudo bash
```

Note: This method installs Hokusai to `/usr/local/bin/hokusai`.

### Pip

Hokusai can be installed via Pip, on MacOS or Linux. If you do so, please first go through [Pyenv](#Pyenv), [Python](#Python), and [Virtualenv](#Virtualenv) steps.

Python 3.7+ is required.

```
pip install hokusai
```

Note: If Pip fails at upgrading your system Python packages, try:

```
pip install hokusai --ignore-installed
```

### Docker

We also maintain [Hokusai Docker images](https://hub.docker.com/r/artsy/hokusai) for running Hokusai in Docker.

### Github

Release artifacts are available on [Github](https://github.com/artsy/hokusai/releases).

### AWS S3

Release artifacts are also available in AWS S3. You can use this [convenience script](get-hokusai.sh) or Curl to fetch them.

### A note on Python 2.x

Hokusai currently supports Python 3.7+ only. The last version that supported Python 2.x was [v0.5.18](https://github.com/artsy/hokusai/tree/v0.5.18).


## Setup

We assume that you already have Kubernetes cluster, Git, Docker, and Docker-Compose set up, and that you have an AWS account. Perform the following steps to setup Hokusai:

1. [Configure AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#configuring-credentials).

2. Configure Hokusai

    ```
    hokusai configure --kubectl-version <kubectl version> --s3-bucket <bucket name> --s3-key <file key>
    ```

    Provide the Kubectl version matching that of your Kubernetes clusters, as well as the S3 bucket name/key where your org's Kubectl config file is stored.

    For system administrators: see [Administering Hokusai](./docs/Administering_Hokusai.md) for instructions on preparing AWS and Kubernetes, and on publishing a Kubectl config file.

    For Artsy developers: see [artsy/README](https://github.com/artsy/README/blob/main/playbooks/hokusai.md) for the current way of installing and configuring hokusai.

3. Enable Bash autocompletion:

    ```
    eval "$(_HOKUSAI_COMPLETE=source hokusai)"
    ```


## Getting Started

See [Getting Started](./docs/Getting_Started.md) to start using Hokusai for your project.


## Command Reference

A full command reference can be found in [Command Reference](./docs/Command_Reference.md).


## Review Apps

Hokusai can be used to simplify the process of spinning up a "review app" instance of your project, based on a feature branch or pull request.

Full details are in the [Review App reference](./docs/Review_Apps.md).


## Developing Hokusai

To work on Hokusai itself, please set up:

### Pyenv

We recommend using [Pyenv](https://github.com/pyenv/pyenv) to install the correct version of Python. For a tutorial of Pyenv, see [this guide](https://realpython.com/intro-to-pyenv/).

When installing on MacOS, please make sure to use brew-installed `openssl` and `readline` libraries, and xcode-installed `zlib` library. And make sure these libraries are correctly linked. Like so:

```
brew install openssl readline zlib

echo 'export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"' >> ~/.bash_profile
echo 'export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"' >> ~/.bash_profile
echo 'export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"' >> ~/.bash_profile
echo 'export PKG_CONFIG_PATH="/usr/local/opt/openssl@1.1/lib/pkgconfig"' >> ~/.bash_profile
```

### Python

Hokusai is currently tested on Python 3.9.10 so we recommend using that Python version.

If you use Pyenv to install Python, you should see an output similar to this:

```
pyenv install 3.9.10

    python-build: use openssl from homebrew
    python-build: use readline from homebrew

    Downloading Python-3.9.10.tar.xz...
    -> https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tar.xz
    Installing Python-3.9.10...
    python-build: use tcl-tk from homebrew
    python-build: use readline from homebrew
    python-build: use zlib from xcode sdk

    Installed Python-3.9.10 to $HOME/.pyenv/versions/3.9.10
```

With the desired Python version installed, activate it globally:

```
pyenv global 3.9.10
```

Note: If you want to create a PyInstaller distribution (by running `make build`) you need to install Python with development dylibs. Use the environment variable `PYTHON_CONFIGURE_OPTS="--enable-framework"` on Darwin and `PYTHON_CONFIGURE_OPTS="--enable-shared"` on Linux when running `pyenv install`.

### Virtualenv

We recommend using a virtual environment to isolate Hokusai's dependencies from that of other projects on your local environment.

The Pyenv install comes with [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) which can be used to create virtual environments.

### Poetry

Use [Poetry](https://python-poetry.org/) to install Hokusai's dependencies as well as Hokusai itself in [editable mode](https://pip-python3.readthedocs.io/en/latest/reference/pip_install.html#editable-installs). See [this guide](https://python-poetry.org/docs/basic-usage/) for working with Poetry.

Install Poetry:

```
pip install poetry
```

Install dependencies and Hokusai in editable mode:

```
poetry install
```

To update dependencies:

```
poetry lock
```


## Testing

### Install Minikube

[Minikube](https://minikube.sigs.k8s.io/docs/start/) is used for integration tests.

```
brew install minikube
minikube start --kubernetes-version=<version of your Kubernetes clusters, example: v1.2.3>
```

### Run tests

To run all tests:

```
make tests
```

To run only unit tests:

```
make test
```

Only integration tests:

```
make integration
```

Only specific modules, TestClasses, or even methods:

```
python -m unittest test.unit.test_module.TestClass.test_method
```

Tip: Set `DEBUG=1` environment variable to print boto logging


## Distributing Hokusai

Merges to `main` branch automatically create Hokusai beta version for testing.

The beta can be installed by:

### MacOS

```
$ brew update
$ brew tap artsy/formulas
$ brew install hokusai-beta
```

### Linux

```
curl -sSL https://raw.githubusercontent.com/artsy/hokusai/main/get-hokusai.sh | sudo bash -s beta
```

To create a new release, perform the following:

- bump Hokusai version in these files:
  - [pyproject.toml](pyproject.toml)
  - [hokusai/VERSION](hokusai/VERSION)
- update [CHANGELOG](./CHANGELOG.md)
- open a PR to merge `main` into `release` branch.


## The Name

The project is named for the great Japanese artist [Katsushika Hokusai](https://www.artsy.net/article/artsy-editorial-7-things-hokusai-creator-great-wave) (1760-1849).


## About Artsy

<a href="https://www.artsy.net/">
  <img align="left" src="https://avatars2.githubusercontent.com/u/546231?s=200&v=4"/>
</a>

This project is the work of engineers at [Artsy][footer_website], the world's
leading and largest online art marketplace and platform for discovering art.
One of our core [Engineering Principles][footer_principles] is being [Open
Source by Default][footer_open] which means we strive to share as many details
of our work as possible.

You can learn more about this work from [our blog][footer_blog] and by following
[@ArtsyOpenSource][footer_twitter] or explore our public data by checking out
[our API][footer_api]. If you're interested in a career at Artsy, read through
our [job postings][footer_jobs]!

[footer_website]: https://www.artsy.net/
[footer_principles]: https://github.com/artsy/README/blob/main/culture/engineering-principles.md
[footer_open]: https://github.com/artsy/README/blob/main/culture/engineering-principles.md
[footer_blog]: https://artsy.github.io/
[footer_twitter]: https://twitter.com/ArtsyOpenSource
[footer_api]: https://developers.artsy.net/
[footer_jobs]: https://www.artsy.net/jobs

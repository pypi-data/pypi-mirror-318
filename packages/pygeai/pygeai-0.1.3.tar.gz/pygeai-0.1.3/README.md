# PyGEAI - SDK for Globant Enterprise AI

PyGEAI is a Software Development Kit to interact with GEAI. It's composed of libraries, tools, code samples and
other documentation that allows developers to interact with the platform in an easier manner.

## Repository
[GitHub repository](https://github.com/VY-GEN032-KG/pygeai)

## Configuration
In order to use the SDK, GEAI_API_KEY and GEAI_API_BASE_URL must be defined. There are three ways in which they
can be used:
- Environment variables: Setting GEAI_API_KEY and GEAI_API_BASE_URL as environment variables.
- Credentials file: Setting GEAI_API_KEY and GEAI_API_BASE_URL in ${USER_HOME}/.geai/credentials
- Client instantiation: When instantiating a client, one can set the api_key and base_url parameters.

## Modules
The SDK is composed of several packages, enclosed within a meta-package:

- pygeai: meta-package that encapsulates all the components of the SDK.
  - pygeai-cli: command line tool to interact with the SDK
  - pygeai-chat: interactive version of the cli tool
  - pygeai-dbg: debugger to deal with potential issues with the SDK and to have a detailed view of what it’s doing.
  - pygeai-core: to handle interaction with base components of GEAI. Also to handle users, groups, permissions, API keys, organizations, projects, etc
  - pygeai-agent: to handle interactions with Agent Studio
  - pygeai-assistant: to handle interaction with Data Analyst Assistants, Rag Assistants, Chat with Data Assistants, Chat with API Assistants and Chat Assistants.
  - pygeai-flows: to handle interactions with Flows


## Usage
### Local install

Clone the repository.
Create virtual environment
```
~$ python3 -m venv venv
```
Enable virtual environment:
```
~$ source venv/bin/activate
```
Install module
```
(venv) ~$ pip install -e . 
```
Check version
```
(venv) ~$ geai v 
```

### Local update
Whenever a new version of the project is available, one can update by pulling the latest version and reinstalling the package:
Update repository
```
(venv) ~$ git pull origin master 
```
Reinstall module
```
(venv) ~$ pip install -e . 
```
Check version
```
(venv) ~$ geai v 
```


## Documentation
The documentation is generated with Sphinx.

Generate rst files:
```
sphinx-apidoc -f -o docs/source pygeai
```

To generate a new version of the documentation, run:
```
(venv) ~$ sphinx-build -M html docs/source docs/build
```
To generate a new version of the documentation in markdown format, run:
```
(venv) ~$ sphinx-build -b markdown docs/source docs/build/markdown
```


## Authors
Copyright 2024, Globant. All rights reserved

Developers:
- Alejandro Trinidad <alejandro.trinidad@globant.com>
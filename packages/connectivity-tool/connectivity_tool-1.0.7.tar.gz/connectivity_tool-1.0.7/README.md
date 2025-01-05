# Connectivity Tool CLI

![Latest Release](https://img.shields.io/github/v/release/haimkastner/connectivity-tool)
[![PyPI version](https://img.shields.io/pypi/v/connectivity_tool.svg?style=plastic)](https://pypi.org/project/connectivity-tool/)
[![License](https://img.shields.io/github/license/haimkastner/connectivity-tool.svg?style=plastic)](https://github.com/haimkastner/connectivity-tool/blob/main/LICENSE)
[![DockerHub](https://img.shields.io/badge/DockerHub-Connectivity--Tool-blue)](https://hub.docker.com/r/haimkastner/connectivity-tool)

<!-- 
Coming soon :)
![Docker Pulls](https://img.shields.io/docker/pulls/haimkastner/connectivity-tool)
[![GitHub stars](https://img.shields.io/github/stars/haimkastner/connectivity-tool.svg?style=social&label=Star)](https://github.com/haimkastner/connectivity-tool/stargazers) -->

[![connectivity-tool](https://github.com/haimkastner/connectivity-tool/actions/workflows/build.yaml/badge.svg?branch=main)](https://github.com/haimkastner/connectivity-tool/actions/workflows/build.yaml)


Welcome to the Connectivity Tool CLI, a command-line interface for network connectivity operations.

## 📦 Features
With the Connectivity Tool CLI, you can perform the following operations:
- **Ping** - Check the reachability of a host / URL
- **Performance** - Check the performance of a URL (latency download/upload bandwidth) 
- **Deviation** - Trace deviations of the response time of a host / URL 

## 🌐 Supported Protocols
- **DNS**
- **HTTPS**
- **HTTP**

## 📋 Requirements
Python 3.10 or Docker

## ⬇️ CLI Download

To start using this CLI, install it via PIP (PyPi registry) as a global python command
```bash 
pip install connectivity_tool
```

> **Note:** The CLI also available as a Docker image, see [Docker Hub](https://hub.docker.com/r/haimkastner/connectivity-tool)
> For more information, see the [Docker](https://github.com/haimkastner/unitsnet-py/blob/main/docker) section
## 🚀 Getting started

Before starting, run the help command to understand how to pass the operation's parameters and payload with all the available options.
```bash
connectivity_tool --help
```

## 📚 Usage Examples

### ⚡ Direct params
```bash
connectivity_tool -p DNS -d yahoo.com
```

### 📂 Test suite path
```bash     
connectivity_tool --suite-file ./suite.yaml
```
The file structure should be as follows:
```yaml
suite:
  - protocol: DNS
    domain: "yahoo.com"

  - protocol: HTTP
    url: "http://www.google.com"

  - protocol: HTTPS
    url: "https://www.facebook.com"
    latency_threshold_deviation: # Optional for HTTP/HTTPS only - default is 60 seconds
      value: 1 # Amount of units
      unit: Millisecond # Unit of the value (e.g. Millisecond, Second, Minute)
    test_upload_bandwidth: true # Optional for HTTP/HTTPS only - default is false
    test_download_bandwidth: true # Optional for HTTP/HTTPS only - default is false
```

The `json` format is also supported.
```json
{
  "suite": [
    {
      "protocol": "DNS",
      "domain": "yahoo.com"
    },
    {
      "protocol": "HTTP",
      "url": "http://www.google.com"
    },
    {
      "protocol": "HTTPS",
      "url": "https://www.facebook.com",
      "latency_threshold_deviation": {
        "value": 1,
        "unit": "Millisecond"
      },
      "test_upload_bandwidth": true,
      "test_download_bandwidth": true
    }
  ]
}
```

## 🗃️ Results Store 
Every operation result will be stored in a `jsonl` local file.

Run `connectivity_tool --output-store 5` to print to stdout the last 5 result/s.

The  store file is `./store_data/conn_tool_store.jsonl` as default and can be changed by `--store` flag.

For Docker see the [Docker](https://github.com/haimkastner/unitsnet-py/blob/main/docker) section

## 🔍 Troubleshooting and logging

The full version and build info of the SDK is available by `--info` see example:
```bash
connectivity_tool --info
```

Connectivity Tool Cli allows to print verbose logs.

```bash
connectivity_tool --verbos
```

## 🐞 Report Bug

In case of an issue or a bug found in the CLI, please open an [issue](https://github.com/haimkastner/connectivity-tool/issues) 

## 🛠️ Development & Contribution
See the [Development](https://github.com/haimkastner/unitsnet-py/blob/main/DEVELOPMENT.md) section for more information

## 📝 License
The Connectivity Tool CLI is licensed under the [MIT License](./LICENSE)

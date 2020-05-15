# OP Bank API Sandbox

[![Chat on Gitter](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/meeshkan/community)

<!-- TODO: Add link to Meeshkan blog once published -->
This repository contains the source code for our article: [How to create a sandbox for the OP Bank API]().

## What's in this document

* [Getting started](#getting-started)
    * [Installation](#installation)
    * [Starting the mock server](#starting-the-mock-server)
    * [Running the tests](#running-the-tests)
    * [Building the specification yourself](#building-the-specification-yourself)
* [Mentioned resources](#mentioned-resources)
* [Contributing](#contributing)
* [Tell us what you think](#tell-us-what-you-think)

## Getting started

⚠️**Prerequisites**:
- [Python 3.6+](https://www.python.org/downloads/)

### Installation

Clone this repository and move into the directory:
```bash
git clone https://github.com/meeshkan/hmt-examples.git
cd hmt-examples
```

Once you're there, [create a virtual environment](https://docs.python.org/3/tutorial/venv.html). 

Then, install the dependencies:
```bash
pip install -r requirements.txt
```

> This command will install all of the necessary dependencies for the OP Bank API sandbox. Most importantly, this includes the [HTTP Mocking Toolkit (HMT)](https://github.com/meeshkan/hmt) that will create the mock server and [`pytest`](https://docs.pytest.org/en/latest/) for running the tests.

Finally, move into the `opbank` directory:
```bash
cd opbank
```

### Starting the mock server

Run the following command to spin up your mock OP Bank server:
```bash
hmt mock ./specs/ --callback-dir ./callbacks/
```

> This command will use the default OpenAPI specification located in the `specs` directory and the custom callbacks in the `callbacks` directory to create a mock server with HMT. Alternatively, you can [build the specification yourself](#building-the-specification-yourself).

Keep this running because you'll need it to execute the tests.

### Running the tests

With your mock server running in another terminal window, you can run the tests with `pytest`:
```bash
pytest
```

### Building the specification yourself

To build your own specification, you first need to obtain recordings from the proxy. This can be done with the following HMT command:

```bash
hmt record
```

Keep that running. Then, in another terminal window, run:

```bash
python opbank_rec.py
```

> The `opbank_rec.py` file contains a script making various calls to the OP Bank API. You can modify this to change the outcome of your recordings. 

Once the recordings are complete, stop HMT without losing any of your data with `Ctrl + C` or another `kill` command.

Finally, build the specification using HMT:

```bash
hmt build --input-file ./logs/your-file-name.jsonl
```

> The input file will be the [JSONL](http://jsonlines.org/) recordings located in your `logs` directory. For reference, the current example in this repository is called `sandbox.apis.op-palvelut.fi-recordings.jsonl`.

This command will create a new `openapi.json` file in your `specs` directory. You can then use that to [start the mock server](#starting-the-mock-server).

## Mentioned resources

Here are a few of the resources mentioned in our tutorial:
- 📖 [OP Bank API Documentation](https://op-developer.fi/docs)
- 🔨 [`http-types`](https://github.com/Meeshkan/http-types/)
- ️🔗 [Kong Gateway](https://konghq.com/kong/) 

## Contributing

Notice a bug? Have any questions? The best way to get involved is to [open an issue](https://github.com/meeshkan/hmt-examples/issues).

Please note that this project is governed by the [Meeshkan Community Code of Conduct](https://github.com/meeshkan/code-of-conduct). By participating, you agree to abide by its terms.

## Tell us what you think

At [Meeshkan](https://meeshkan.com/), we're working to improve how people test their products. So no matter if you loved or loathed our tutorial, we want to hear from you. 

Here are some ways you can get in touch:
- [Open an issue](https://github.com/meeshkan/hmt-examples/issues)
- [Tweet at us](https://twitter.com/meeshkanml)
- [Reach out on Gitter](https://gitter.im/Meeshkan/community)
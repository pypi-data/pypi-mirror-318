# Imandra CLI and API client library

[Imandra](https://www.imandra.ai) is a cloud-native automated reasoning engine for analysis of algorithms and data.

This package contains a python library `imandra` for interacting with Imandra's web APIs, to do things such as:

- Creating cloud-hosted Imandra Core instances to interact with Imandra via:
  - Jupyter Notebooks
  - the HTTP API wrapper around an Imandra Core session,`imandra-http-api`.
- Submitting Imandra Protocol Languge (IPL) analysis jobs

If you're interested in developing Imandra models, you may also want to see the [main Imandra docs site](https://docs.imandra.ai/imandra-docs/), and consider setting up Imandra Core locally by following the installation instructions there.

The `imandra` python API reference documentation is available [here](https://docs.imandra.ai/imandra-docs/python/imandra/).

The `imandra` package also adds an entry point called `imandra-cli` which exposes the `imandra` library functionality in a more discoverable way:

```sh
$ python3 -m venv ./my/venv
...
$ ./my/venv/pip install imandra
...
$ ./my/venv/bin/imandra-cli --help
usage: imandra [-h] auth,ipl,core,rule-synth,cfb ...

Imandra CLI

positional arguments:
  {auth,ipl,core,rule-synth,cfb}

optional arguments:
  -h, --help            show this help message and exit
```

On Windows, the entry point can be found as `.\my\venv\Scripts\imandra-cli.exe`.

## Authentication

This is the first step to start using Imandra via APIs. Our cloud environment requires a user account, which you may setup like this:

```sh
$ ./my/venv/bin/imandra-cli auth login
```

and follow the prompts to authenticate. This will create the relevant credentials in `~/.imandra` (or `%APPDATA%\imandra` on Windows).

You should now be able to invoke CLI commands that require authentication, and construct an `auth` object from python code:

```py
    import imandra.auth
    auth = imandra.auth.Auth()
```

This auth object can then be passed to library functions which make requests to Imandra's web APIs.

## Quick Start with Python APIs:

The `imandra.session` class provides an easy-to-use interface for requesting and managing an instance of Imandra Core within our cloud environment. It has built-in use of `auth` class described above.

```py
import imandra
with imandra.session() as s:
    s.eval("let f x = if x > 0 then if x * x < 0 then x else x + 1 else x")
    verify_result = s.verify("fun x -> x > 0 ==> f x > 0")
    instance_result = s.instance("fun x -> f x = 43")
    decomposition = s.decompose("f")

print(verify_result)
print(instance_result)

for n, region in enumerate(decomposition.regions):
    print("-"*10 + " Region", n, "-"*10 + "\nConstraints")
    for c in region.constraints_pp:
        print("  ", c)
    print("Invariant:", "\n  ", region.invariant_pp) 
```

 Please note, while this simplifies usage, it can be less resource-efficient for repeated high-volume requests, as a new Imandra instance pod is started for each block (which may take a few seconds and be subject to availability if you're using community license). For more practical applications, manual management of your instances may be preferable:

```py
import imandra

s = imandra.session()

print(s.verify("fun x -> x > 0 ==> f x > 0"))

s.close()

```

We recommend using Jypyter notebooks (Python kernel) with our APIs so you can instanciate a session in one cell and repeatedly perform computation in others.

Please note: we enforce limits on the number of pods you can run simultaneously (per license level).

## (Advanced) Manually interacting with Imandra Core via HTTP

The package also includes `imandra_http_api_client`, an open-api generated API
client for `imandra-http-api`, the HTTP wrapper for Imandra itself, which can be
used for verifying Imandra models.

Although developing models is best done via a [local Imandra Core
installation](https://docs.imandra.ai/imandra-docs/notebooks/installation/), if
you've already built a model and want to dynamically interrogate its logical
constitution using Imandra, Imandra Core's HTTP API can lend a hand by giving
you lightweight access to an Imandra Core instance, and returning responses in a
structured, machine-readable format over HTTP.

- See the [`imandra_http_api_client` API reference
  documentation](https://docs.imandra.ai/imandra-docs/python/imandra_http_api_client/)
  for this module.

If you have a [local Imandra Core
installation](https://docs.imandra.ai/imandra-docs/notebooks/installation-simple/#Installation-of-Imandra-Core),
you can invoke `imandra-http-api` directly, and connect to it on localhost:

```bash
# In a terminal
$ imandra-http-api
```

```py
# with imandra-http-api running locally on port 3000
import imandra_http_api_client

config = imandra_http_api_client.Configuration(
    host = 'http://localhost:3000',
)
```

If you do not have a local Imandra Core installation, you can create an instance
of `imandra-http-api` on our cloud (after authenticating via the CLI command
`imandra auth login`):

```py
import imandra.auth
import imandra.instance
import imandra_http_api_client

auth = imandra.auth.Auth()
instance = imandra.instance.create(auth, None, "imandra-http-api")

config = imandra_http_api_client.Configuration(
    host = instance['new_pod']['url'],
    access_token =  instance['new_pod']['exchange_token'],
)
```

You can then use your `imandra_http_api_client.Configuration` object to make requests to `imandra-http-api`:

```py
with imandra_http_api_client.ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = imandra_http_api_client.DefaultApi(api_client)
    eval_req = {
        "src": "fun x -> List.rev (List.rev x) = x",
        "syntax": "iml",
        "hints": {
            "method": {
                "type": "auto"
            }
        }
    }
    req = {
        "src": "fun x -> List.rev (List.rev x) = x",
        "syntax": "iml",
        "hints": {
            "method": {
                "type": "auto"
            }
        }
    }
    print("Request: ")
    print(req)
    verify_request_src = imandra_http_api_client.VerifyRequestSrc.from_dict(req)

    try:
        # Verify a string of source code
        api_response = api_instance.verify_by_src(verify_request_src)
        print("The response of DefaultApi->verify:\n")
        print(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->verify: %s\n" % e)
```

Once you're done with your instance, terminate it with:

```
imandra.instance.delete(auth, instance['new_pod']['id'])
```

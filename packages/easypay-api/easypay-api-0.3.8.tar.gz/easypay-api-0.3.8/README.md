# [Easypay API](http://easypay-api.hive.pt)

API client for the [Easypay](https://www.easypay.pt) service, conformant with the typical Python API client provided by Hive Solutions.

The Easypay API client provides a simple and convenient way to interact with the [Easypay](https://www.easypay.pt) payment gateway. This client allows developers to integrate payment processing, manage transactions, and perform other operations using Easypay services in their Python applications.

## Installation

Install the package using pip:

```bash
pip install easypay-api
```

## Quick Start

Here’s a simple example of how to use the Easypay API client:

```python
import easypay

client = easypay.Api(account_id="your_account_id", key="your_key")
payment = client.generate_payment(100, method="mb")

print(payment)
```

## Resources

- [Easypay API Docs](https://docs.easypay.pt/)
- [Easypay Admin](https://id.easypay.pt/)
- [Easypay Admin Test](https://id.test.easypay.pt/)

## Support

For more information, visit the [Easypay API Documentation](https://docs.easypay.pt/) or contact Easypay support.

## License

Easypay API is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://github.com/hivesolutions/easypay-api/workflows/Main%20Workflow/badge.svg)](https://github.com/hivesolutions/easypay-api/actions)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/easypay-api/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/easypay-api?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/easypay-api.svg)](https://pypi.python.org/pypi/easypay-api)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)

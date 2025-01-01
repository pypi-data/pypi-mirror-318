# Dischub Python SDK

## Overview

The Dischub Python SDK allows developers to easily integrate with the Dischub API for online payment processing. This SDK provides a simple interface for creating payments via the Dischub API.

## Installation

You can install the Dischub SDK using pip:

```bash
pip install dischub
```

## Usage

Copy and paste code below as a function called "payment" in your functions' file

```bash
from dischub import Dischub

def payment():
    data = {
        "sender": "sender-dischub-account-email-@gmail.com",
        "recipient": "your-dischub-business-account-email-@gmail.com",
        "amount": 100,
        "currency": "USD",
    }
    payment_instance = Dischub()
    response = payment_instance.create_payment(data)
    print(response)
payment()
```

## Response

If your integration is done so well, you will get the below response

```bash
{'Status': 'Success', 'Message': 'Payment initiated', 'Response_code': 201}
```


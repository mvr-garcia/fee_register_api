# Fee Register

This is a simple API, which I created just for study purposes.
Its function is to record customer fee changes and return an organized list of them. 

#### To know:

My initial problem was to find a way to create a historical record in which it was possible, in addition to recording all operations, to link a specified client's update operations to the create operation.

The hypothetical problem was:

The secretary will set a new rate for a customer with an expiration date (a create operation), the secretary can at any time, as long as before the expiration, change to a new rate with a new expiration date (an update operation ).

In addition to recording the two operations, the service must be able to link to the same index [custom_fee_id] as the customer's fee create operation, so we will keep a history of when a custom fee was created for that customer and its extensions and changes.

Similar to a medical record, in which procedures performed on a patient are recorded.

## Endpoints

### Create register

```http://localhost:8000/api/create/```

For **create** a register:

Make a POST request with the follow payload:

```{"client": "334455", "taker": 0.00300000, "maker": 0.00400000, "staff_email": "abdef@hotmail.com", "expires_at":"23-08-2021", "register_type": "create", "observation": "anything"}```

For **update** a register, remember that the client has to be already created a register, and the register type has to be "update".

Make a POST request with the follow payload:

```{"client": "334455", "taker": 0.00300000, "maker": 0.00400000, "staff_email": "abdef@hotmail.com", "expires_at":"23-08-2021", "register_type": "update", "observation": "update because I don't know"}```

### List all registers

```http://localhost:8000/api/list/```

## Requirements

To make the magic happen, you just need to have installed:

* Docker

## Starting the application

Inside the application directory:

```bash
make start
```
In the first time, you should perform the migrations, so:

```bash
make bash
```
```bash
python manage.py migrate
```

## Authors

Marcos Garcia   
e-mail: mvrgarcia05@gmail.com

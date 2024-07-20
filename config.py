# API Documentation

## Endpoints

### Create Employee

* **Method:** `POST`
* **Endpoint:** `/employees`
* **Request Body:**
	+ `name`: string
	+ `age`: integer
	+ `department`: string
* **Response:**
	+ `message`: string

### Get All Employees

* **Method:** `GET`
* **Endpoint:** `/employees`
* **Response:**
	+ `employees`: array of objects
		- `id`: integer
		- `name`: string
		- `age`: integer
		- `department`: string

### Get Employee by ID

* **Method:** `GET`
* **Endpoint:** `/employees/<id>`
* **Path Parameters:**
	+ `id`: integer
* **Response:**
	+ `id`: integer
	+ `name`: string
	+ `age`: integer
	+ `department`: string

### Update Employee

* **Method:** `PUT`
* **Endpoint:** `/employees/<id>`
* **Path Parameters:**
	+ `id`: integer
* **Request Body:**
	+ `name`: string
	+ `age`: integer
	+ `department`: string
* **Response:**
	+ `message`: string

### Delete Employee

* **Method:** `DELETE`
* **Endpoint:** `/employees/<id>`
* **Path Parameters:**
	+ `id`: integer
* **Response:**
	+ `message`: string
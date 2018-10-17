[![Build Status](https://travis-ci.org/muthigani/STORE-MANAGER-API.svg?branch=develop)](https://travis-ci.org/muthigani/STORE-MANAGER-API)

[![Maintainability](https://api.codeclimate.com/v1/badges/8b5a690623d9460a6aee/maintainability)](https://codeclimate.com/github/muthigani/STORE-MANAGER-API/maintainability)

## STORE-MANAGER-API :book:
* 	Admin can add a product
* 	Admin/store attendant can get all products
* 	Admin/store attendant can get a specific product
* 	Store attendant can add a sale order
* 	Admin can get all sale order records

The application should have following endpoints:

| Endpoint   | Functionality |
| ------------- | ------------- |
| GET /products   | Fetch all products  |
| GET /products/<productId>  | Fetch a single product record  |
| GET /sales  | Fetch all sale records  |
| GET /sales/<salesId>  | Fetch a single sale record  |
| POST /products  | Create a product  |
| POST /sales  | Create a sale order  |

  
## Installations
* OS -Windows 10
* Gitbash
  
## How to setup Locally
* install on virtual env:
```sh
pip install virtual env
```
* install  flask:
```sh
pip install flask 
```
* install flask restful :
```sh
pip install flask-restful
```




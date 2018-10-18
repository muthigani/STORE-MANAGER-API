[![Build Status](https://travis-ci.org/muthigani/STORE-MANAGER-API.svg?branch=develop)](https://travis-ci.org/muthigani/STORE-MANAGER-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/8b5a690623d9460a6aee/maintainability)](https://codeclimate.com/github/muthigani/STORE-MANAGER-API/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/muthigani/STORE-MANAGER-API/badge.svg?branch=develop)](https://coveralls.io/github/muthigani/STORE-MANAGER-API?branch=master)
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
* Postman
  
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

## Heroku Links
* Welcome Page: https://store-manager-api-1987.herokuapp.com
* Sales Page: https://store-manager-api-1987.herokuapp.com/api/v1/sales
* Products Page: https://store-manager-api-1987.herokuapp.com/api/v1/products


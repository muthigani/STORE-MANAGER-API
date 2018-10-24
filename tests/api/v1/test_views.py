import unittest
from flask import Flask, json


app = Flask(__name__)


class TestingEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    
    def test_to_get_all_(self):
        """These tests check  all sales """
        response = self.app.get('/api/v1/sales', content_type="application/json")
        self.assertTrue(response.status_code, 200)


    def test_get_specific_order(self):
        """These tests check  specific order """ 
        response = self.app.get('/api/v1/sales/1', content_type="application/json")
        self.assertTrue(response.status_code, 200)

    def test_error_id(self):
        """Test to check error in specific order """ 
        orderid = "1"
        api_url = '/api/v1/ordersss/'+ orderid
        response = self.app.get(api_url)
        self.assertRaises(TypeError, response)


    def test_nonexistant_saleid(self):
        """Test check none existing saleid """
        response = self.app.get('/api/v1/sales/20', content_type="application/json")
        self.assertEqual(response.status_code,404)
   
    
    def test_error_when_string_is_notpassed(self):
        """Test whether productname  parameter is a string"""
        response = self.app.post('/api/v1/sales',data = json.dumps({"productname": 7}),
                                content_type="application/json", follow_redirects=True)
        self.assertRaises(TypeError, response)
    

    def test_mandatory_parameter_missing_in_placed_order(self):
        """Test if mandatory parameter productname is not passed"""
        response = self.app.post('/api/v1/sales',data = json.dumps({"productname": "Techno Product"}),
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,404)

    def test_to_get_all_products(self):
        """These tests check  all products"""
        response = self.app.get('/api/v1/products', content_type="application/json")
        self.assertTrue(response.status_code, 200)


    def test_get_specific_product(self):
        """These tests check  specific product""" 
        response = self.app.get('/api/v1/products/2', content_type="application/json")
        self.assertTrue(response.status_code, 200)

    def test_error_productid(self):
        """Test to check error in specific product""" 
        productid = "1"
        api_url = '/api/v1/productsxx/'+ productid
        response = self.app.get(api_url)
        self.assertRaises(TypeError, response)


    def test_nonexistant_productid(self):
        """Test check none existing productid """
        response = self.app.get('/api/v1/products/15', content_type="application/json")
        self.assertEqual(response.status_code,404)
   
    
    def test_error_when_product_is_notpassed(self):
        """Test whether productname  parameter is a string"""
        response = self.app.post('/api/v1/products',data = json.dumps({"productname": 17}),
                                content_type="application/json", follow_redirects=True)
        self.assertRaises(TypeError, response)
    

    def test_parameter_missing_in_placed_product(self):
        """Test if mandatory parameter productname is not passed"""
        response = self.app.post('/api/v1/products',data = json.dumps({"productname": "Samsung S8"}),
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,404)


def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()


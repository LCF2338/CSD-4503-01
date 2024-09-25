# The file name for unit testing must follow this convention. test_<something>

from app import flask_app
import unittest

# Class to represent the test cases.
# Use functions (methods) to define the scenarios.

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        #Set up the test client. These two lines are specific to Flask.
        self.app = flask_app.test_client();
        self.app.testing = True;

    def test_index_1(self):
        # Send a get request to the Index "/" route.
        response = self.app.get("/")

        # Check if the response is 200 OK.

        # assertEqual checks if they match, otherwise it returns false.
        self.assertEqual(first=response.status_code, second=200)

    def test_index_2(self):
        response = self.app.get("/index")
        self.assertEqual(first=response.status_code, second=200)

    def test_index_data(self):
        response = self.app.get("/index")
        # Response.data returns the "This is the index page. It's better to decode it to utf-8 for characters(?)."
        self.assertEqual(first=response.data.decode('utf-8'), second="This is the index page.")
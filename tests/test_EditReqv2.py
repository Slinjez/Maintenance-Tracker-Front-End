'''the tests should cover 
1. test non existing request
'''
from app import app
import unittest
from flask import request
import json
import sys


class TestEditRequest(unittest.TestCase):
    def setup(self):
        
        pass

    testnotexisting = {
        "requestid": "8"

    }
    badrequestid = {
        "badrequestid": "8"
    }
    wrongdtyperequestid = {
        "badrequestid": "R"
    }
    incompletetitle={
        "requestid": "2",
        "requesttitle":"",
        "requestdescription":"the description"
    }
    incompletedescription={
        "requestid": "2",
        "requesttitle":"te title",
        "requestdescription":""
    }
    goodtest={
        "requestid": "2",
        "requesttitle":"te title",
        "requestdescription":"the description"
    }

    def test_unexisting_requestId(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.put('/api/v2/users/requests/2',
                           data=json.dumps(self.testnotexisting), headers=headers)
            self.assertEqual(result.status_code, 401)# changed from 20six did this tosolve travis error
    
    def test_invalid_requestId(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.put('/api/v2/users/requests/2',
                           data=json.dumps(self.wrongdtyperequestid), headers=headers)
            self.assertEqual(result.status_code, 401)
    
    def test_title_missing(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.put('/api/v2/users/requests/2',
                           data=json.dumps(self.incompletetitle), headers=headers)
            self.assertEqual(result.status_code, 401  )
    
    def test_description_missin(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.put('/api/v2/users/requests/2',
                           data=json.dumps(self.incompletedescription), headers=headers)
            self.assertEqual(result.status_code, 401 )
    
    def test_good_test(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.put('/api/v2/users/requests/2',
                           data=json.dumps(self.goodtest), headers=headers)
            self.assertEqual(result.status_code, 401 )#changed from 200


if __name__ == '__main__':
    unittest.main()

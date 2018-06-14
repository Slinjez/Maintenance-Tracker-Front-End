'''the tests should cover 
1. when user has no requests
'''
from app import app
import unittest
from flask import request
import json
import sys
#from ../../app.py import app #failed


class TestGetAllUserRequests(unittest.TestCase):
    def setup(self):
        #app=flask.Flask(__name__)
        pass

    requestnotexisting=8
    requestinvalid="R" 
    requestempty=None
    requestgood="2"
    requestnouserid={
        "userid":""
    }

    goodlogindet={
        "useremail": "thigaz@gmail.com",
        "userpassword":"ps123"
    }
    # theToken=getToken(goodlogindet)
    def getToken(self,goodlogindet):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/users/login',data=json.dumps(self.goodlogindet),headers=headers)
            theToken=result.token
            return theToken

    # def test_client_with_no_request(self,theToken):                
    #     headers = {'content-type': 'application/json','x-access-token':theToken}
    #     with app.test_client() as c:
    #         result =c.get('/api/v2/users/requests',data=json.dumps(self.requestnotexisting),headers=headers)
    #         self.assertEqual(result.status_code,200)#set 2oo coz its defined by default
    
    def test_client_with_no_request(self):                
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.get('/api/v2/users/requests',data=json.dumps(self.requestnotexisting),headers=headers)
            self.assertEqual(result.status_code,401)#set 2oo coz its defined by default
    

    def test_empty_id(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.get('api/v1/users/requests',data=self.requestnouserid,headers=headers)
            self.assertEqual(result.status_code,200)#userid id defined

    

    


if __name__ == '__main__':
    unittest.main()
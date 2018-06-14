import psycopg2
import psycopg2.extras
from datetime import datetime as dt


class dbOperations():

    connection = psycopg2.connect("dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
    cursor = connection.cursor()

    def confirmNewUser(self, usermail):
        query = "select * from users where useremail='{usermail}'".format(
            usermail=usermail)
        theResult = self.getFromDb(query)
        if not theResult:
            return True
        else:
            return False

    def saveUser(self, newUser):
        username = newUser.username
        useremail = newUser.useremail
        userpassword = newUser.userpassword
        userrole = newUser.userrole

        query = "insert into users (username,useremail,password,userrole) values('{username}','{useremail}','{userpassword}','{userrole}')".format(
            username=username,
            useremail=useremail,
            userpassword=userpassword,
            userrole=userrole
        )
        self.addToDb(query)

    def confirmLogin(self, theUser):
        usermail = theUser.useremail

        query = "select * from users where useremail='{usermail}'".format(
            usermail=usermail)
        theResult = self.getFromDb(query)

        if not theResult:
            return False
        else:
            return True

    def confirmAdminLogin(self, theMail):
        usermail = theMail

        query = "select * from users where useremail='{usermail}'".format(
            usermail=usermail)
        theResult = self.getFromDb(query)

        if not theResult:
            return False
        else:
            return True

    def getLoginCredentials(self, theUser):
        usermail = theUser.useremail
        query = "select * from users where useremail='{usermail}'".format(
            usermail=usermail)
        theResult = self.getFromDb(query)
        if not theResult:
            return None
        else:
            return theResult

    def getAdminLoginCredentials(self, theUserEmail):
        usermail = theUserEmail
        query = "select * from users where useremail='{usermail}'".format(
            usermail=usermail)
        theResult = self.getFromDb(query)
        if not theResult:
            return None
        else:
            return theResult

    def createRequest(self, thisRequest):
        self.connection = psycopg2.connect(
            "dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
        self.cursor = self.connection.cursor()
        requestorid = thisRequest.requestorid
        requesttitle = thisRequest.requesttitle,
        requestdescription = thisRequest.requestdescription,
        requesttype = thisRequest.requesttype,
        requestcreationdate = dt.now(),
        requeststatus = thisRequest.requeststatus
        requeststatus = int(requeststatus)

        self.cursor.execute("INSERT INTO requests (requesttitle,requestdescription,requesttype,requestdate,requeststatus,requestorid) values(%s,%s,%s,%s,%s,%s)", (
            requesttitle,
            requestdescription,
            requesttype,
            requestcreationdate,
            requeststatus,
            requestorid))

        self.connection.commit()
        self.cursor.close()

    def getAllRequest(self, userid):

        query = "select * from requests where requestorid='{userid}'".format(
            userid=userid)
        theResult = self.getFromDb(query)

        if not theResult:
            return None
        else:

            return theResult

    def getAllRequestForAdmin(self):
        query = "select * from requests "
        theResult = self.getFromDb(query)

        if not theResult:
            return None
        else:
            return theResult

    def getOneRequest(self, userid, requestid):
        query = "select * from requests where requestorid='{userid}' and requestid='{requestid}'".format(
            userid=userid, requestid=requestid)
        theResult = self.getFromDb(query)

        if not theResult:
            return None
        else:
            return theResult

    def getOneRequestForAdmin(self, requestid):
        query = "select * from requests where requestid='{requestid}'".format(
            requestid=requestid)
        theResult = self.getFromDb(query)

        if not theResult:
            return None
        else:

            return theResult

    def canEditOneRequest(self, userid, requestid):
        query = "select * from requests where requestid='{requestid}'".format(
            requestid=requestid)
        theResult = self.getFromDb(query)

        if not theResult:
            return None
        else:
            return theResult

    def updateRequest(self, requestUpdates):
        query = """
            UPDATE requests
            SET requesttitle = '{requesttitle}',
                requestdescription = '{requestdescription}' ,
                requesttype = '{requesttype}' 
            WHERE
            requestid='{requestid}';
        """.format(requesttitle=requestUpdates['requesttitle'], requestdescription=requestUpdates['requestdescription'], requesttype=requestUpdates['requesttype'], requestid=requestUpdates['requestid'])
        self.addToDb(query)

    def verifyRequest(self, requestUpdates):
        query = """
            UPDATE requests
            SET requeststatus = '{reueststatus}'
            WHERE
            requestid='{requestid}';
        """.format(reueststatus=requestUpdates['requeststatus'], requestid=requestUpdates['requestid'])
        self.addToDb(query)

    def getFromDb(self, query):
        self.connection = psycopg2.connect(
            "dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
        cur = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query)
        resultset = cur.fetchall()
        dict_result = []
        for row in resultset:
            dict_result.append(dict(row))
        return dict_result
        self.connection.commit()
        self.cursor.close()

    def addToDb(self, query):
        self.connection = psycopg2.connect(
            "dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        self.connection.commit()
        self.cursor.close()

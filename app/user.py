
class User:

    def __init__(self, username="", useremail="", userpassword="", userrole=""):

        self.username = username
        self.useremail = useremail
        self.userpassword = userpassword
        self.userrole = userrole

    def setUserName(self, username):
        self.username = username

    def setUserEmail(self, useremail):
        self.useremail = useremail

    def setUserpassword(self, userpassword):
        self.userpassword = userpassword

    def setUserRole(self, userrole):
        self.userrole = userrole

    def getUserName(self):
        return self.username

    def getUserEmail(self):
        return self.useremail

    def getUserpassword(self):
        return self.userpassword

    def getUserRole(self):
        return self.userrole

    def createUser(self, username, useremail, userpassword, userrole):
        self.username = username
        self.useremail = useremail
        self.userpassword = userpassword
        self.userrole = userrole
        return self

    def createUserEmailOnly(self, useremail):
        self.useremail = useremail
        return User

    def getUser(self):
        return User


class Client(User):
    def createRequest(self):
        pass

    def editRequest(self):
        pass

    def deleteRequest(self):
        pass


class Admin(User):
    def approveRequest(self):
        pass

    def disApproveRequest(self):
        pass

    def resolveRequest(self):
        pass

class User:

    def __init__(self, id, uname, fname, lname, email, pwd, phone, status):
        self.id = id
        self.uname = uname
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pwd = pwd
        self.phone = phone
        self.status = status

    def get_data(self):
        return {
                        "id": self.id,
                        "username": self.uname,
                        "firstName": self.fname,
                        "lastName": self.lname,
                        "email": self.email,
                        "password": self.pwd,
                        "phone": self.phone,
                        "userStatus": self.status
                }



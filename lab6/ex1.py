class UserAccount():
    def __init__(self, username: str, email: str, password: str):
        self.email = email
        self.username = username
        self._password = password
    
    def set_password(self, new_password: str):
        self._password = new_password
    
    def check_password(self, password: str) -> bool:
        return self._password == password
    
account1 = UserAccount('Freez', 'freez@gmail.com', '12345')

print(account1.check_password('12345'))

account1.set_password('54321')

print(account1.check_password('12345'))
print(account1.check_password('54321'))
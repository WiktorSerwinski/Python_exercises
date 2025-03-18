class client:
    def __init__(self,name,surname,phone_number):
        self.name= name
        self.surname = surname
        self.phone = phone_number        
    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self,val):
        if(len(val)!=9):
            raise ValueError("Number should contain 9 digits")
        self._phone = val

class Account:
    def __init__(self, account_nr,balance = 0.0):
        self.account_number = account_nr
        self.balance = balance
    
    def deposit(self, amount):
        self.balance+= amount
        
    def withdraw(self, amount):
        if(amount > self.balance):
            raise ValueError("Not enough money!")
        self.balance -= amount
        
    def get_balance(self):
        return self.balance
            
    
    
class Bank_client(client):
    def __init__(self,account_nr,balance,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.account = Account(account_nr,balance)
        
        
if __name__ == '__main__':
    seba = Bank_client("123",0,"Seba","Ser","123456789")
    print(seba.account.balance)
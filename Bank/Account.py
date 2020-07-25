from datetime import datetime
class BankAccount:
  bank = "KCB"
  
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.balance = 0


    
  def account_name(self):
    name = "{} account for {} {}". format(self.bank, self.first_name, self.last_name)
    return name
  
  def deposit(self,amount):
    self.balance += amount
    print("You deposited {} to your account".format(amount))

  def withdraw(self,amount):
    self.balance -= amount
    print("You withdrawn {} from your account".format(amount)) 


  def withdraw(self, amount):
    self.balance -= amount
    if amount <= 0:
      print("You can't withdraw {} from your account".format(amount))
    else:
      self.balance -= amount
      print("You have withdrawn {} from your account".format(amount))
  
  def deposit(self, amount):
     self.balance += amount
     if amount <=0:
       print("You cannot deposit zero amount from your account". format(amount))
     else:
       self.balance += amount
       self.deposit.append(amount)
       print("You have deposited {} money to {}".format (amount, self.account_name()))
from datetime import datetime
class BankAccount:
  def __init__(self,first_name,last_name,bank,phone_number):

    self.first_name = first_name
    self.last_name = last_name
    self.bank = bank
    self.phone_number = phone_number
    self.balance = 0
    self.deposit_update = []
    self.withdraw_update = []
    self.loan = amount
    self.pay_loan = amount
    self.time=datetime.now()





  def phone_number(self, phone_number):
    contact = "Your phone_number {}".format(phone_number)
    return phone_number
  def deposit(self, amount):
    time = datetime.now()
    date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    deposit = {"time": "time", "amount" : "amount"}

    try:
      amount + 0
    except TypeError:

      print("You must enter amount in figures")
    return
    print("Hello you deposited {} amount at {}".format(amount, get_time ))
    
    if amount <= 0:
      print("You can't deposit zero to your account".format(amount))
    else:
      self.balance += amount
      self.deposits.append(amount)
      print("You have deposited {} to your account".format(amount, self.account_name()))

  def withdraw(self, amount):
    time = datetime.now()
    date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    withdraw = {"time": "time", "amount" : "amount"}

    try:
      amount + 1
    except TypeError:
      print("You dont have enough money to withdraw")
      return
      print("Hello {} you have withdrawn {} amount from your account at {} on {}".format(self.account_name(),amount, get_time))


    if amount == 0:
      print("You can't withdraw zero from your account".format(amount))
    elif amount > self.balance:
      print("You dont have enough balance")
    else:
      self.balance -= amount
      self.withdraw.append(amount)
      print("You have withdrawn {} from your account".format(amount,self.account_name()))
  def get_balance(self): 
    time = datetime.now()
    date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    get_balance = {"time": "time", "amount" : "amount"}
    return"The balance for {} is {} amount at {}".format(self.account_name(),amount,get_time )
  def show_deposit_statement(self):
    for deposit in self.deposits:
      time = date_time.now()
      date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
      show_deposit_statement = {"time": "time", "amount" : "amount"}
      print(deposit,get_time)
  def show_withdrawals_statement(self):
    for withdrawal in self.withdrawals:
      time = date_time.now()
      date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
      show_withdrawals_statement = {"time": "time", "amount" : "amount"}
      print(withdrawal, get_time)
  def get_loan(self, amount):
    time = date_time.now()
    date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    get_loan = {"time": "time", "amount" : "amount"}
    if amount <= 0:
      print("You cannot get loan of {} amount at {}".format(amount,get_time))
    else:
      self.loan = amount
      print("You have been given loan of {} at {}".format(amount, get_time))
    
  def pay_loan(self, amount): 
    time = date_time.now()
    date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    
    get_loan = {"time": "time", "amount" : "amount"}
    try:
     amount +1
    except TypeError:
      print("Enter amount in figures")
      return
    if amount <= 0:
      print("You cannot pay with that amount")
    elif self.loan == 0:
      print("You dont have a loan at the moment")
    elif amount > self.loan:
      print("Your loan is paid amount at")
    else:
      self.loan = amount
      print("You have paid your loan of {} at{}".format(amout, get_time))
   



 
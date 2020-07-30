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
    self.repayment= []


  def account_name(self):
    name = "{} account for {} {}". format(self.bank, self.first_name, self.last_name)
    return name

  def phone_number(self, phone_number):
    contact = "Your phone_number {}".format(phone_number)
    return phone_number

  def deposit(self, amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter amount in figures")
      return
    if amount <= 0:
      print("You can't deposit zero to your account".format(amount))
    else:
      self.balance += amount
      time = datetime.now()
      deposit = {
        "time": time,
        "amount": amount
      }
      self.deposits.append(deposit)
      formated_time = time.strftime("%m/ %d/ %Y, %H:%M:%S")
      print("You have deposited {} to your account to {} on {}".format(amount, self.account_name(), formated_time))  
  def withdraw(self, amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter amount in figures")
      return
    if amount == 0:
      print("You can't withdraw zero from your account".format(amount))
    elif amount > self.balance:
      print("You dont have enough balance")
    else:
      self.balance -= amount
      time = datetime.now()
      withdraw = {"time": "time", "amount" : "amount"} 
      self.withdraw.append(withdraw)
      formated_time = time.strftime("%m/ %d/ %Y, %H:%M:%S")
      print("Hello {} you have withdrawn {} amount from your account at {} on {}".format(self.account_name(),amount, date_time))
  def get_balance(self): 
    return"The balance for {} is {} amount".format(self.account_name(),amount,)
  def show_deposit_statement(self):
    for deposit in self.deposit:
      time = deposit ['time']
      amount = deposit['amount']
      formated_time = self.get_formated_time(time)
      statement ="You deposited {} on {}".format(amount, formated_time)
      print(deposit)
  def show_withdrawals_statement(self):
    for withdrawal in self.withdraw:
      time = withdrawal['time']
      amount = withdrawal['amount']
      formated_time = self.get_formated_time(time)
      statement ="You withdrew {} on {}".format(amount, formated_time)
      print(withdrawal)
  def get_loan(self, amount):
    try:
      amount +10
    except TypeError:
      print("Enter amount in figures")
      return
    if amount <= 0:
      print("You cannot get loan of that amount"
    else:
      self.loan = amount
      time = datetime.now()
      get_loan = {"time": "time", "amount" : "amount"} 
      self.get_loan
      formated_time = time.strftime("%m/ %d/ %Y, %H:%M:%S") 
      print("You have been given loan of {} ".format(amount))

    
  def repay_loan(self, amount): 
    try:
     amount +10
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
      self.loan -= amount
      time = date_time.now()
      date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
      repay_loan = {"time": "time", "amount" : "amount"}
      print("You have paid your loan of {} at{}".format(amount, date_time))

  def loan_repayment_statement(self):
    for repayment in self.loan_repayment:
      time = repayment['time']
      amount = repayment['amount']
      formated_time = self.get_formated_time(time)
      statement ="You repaid {} on {}".format(amount, formated_time)
      print(statement)

   
   
class BankAccount(Account):
  def __init__(self, first_name, last_name, phone_number,bank):
    self.bank = bank
    self.recieve money = []
    self.send money = []
    super().__init__(first_name, last_name, phone_number)


  def recieve_money(self, amount):
    for recieve_money in self.recieve:
      time = recieve['time']
      amount = recieve ['amount']
      formated_time = self.get_formated_time(time)
      statement = "You recieved {} on {}".format(amount, formated_time)

  def send_money(self, amount):
    try:
      amount + 1
    except TypeError:
      print("Please enter amount in figures")
      return
    if amount >= self.balance:
      print("You don't have enough amount to send")
    else:
      self.balance >= amount
      time = datetime.now()
      sendmoney = {
        "time": time, "sendmoney": amount
      }
      self.send_money.append(send_money)
      print("You have sent {} amount on {}".format(amount, self.get_formated_time(time)))

class MobileMoneyAccount(Account):
  def __init__(self, first_name, last_name, phone_number, service_provider):
    self.service_provider = service_provider
    self.airtime = []
    self.paybill = []
    self.recieve money = []
    self.send money = []
    super().__init__(first_name, last_name, phone_number)

  def buy_airtime(self, amount):
    try:
      amount + 1
    except TypeError:
      print("Please enter the amount in figures")
      return
    if amount > self.balance:
      print("You don't have enough balance. Your balance is {}".format(self.balance))
    else:
      self.balance -= amount
      time = datetime.now()
      airtime = {
        "time": time, "airtime": amount
      }
      self.airtime.append(airtime)
      print("You have bought airtime worth {} on {}".format(amount, self.get_formated_time(time)))

  def pay_bill(self, amount):
    try:
      amount + 1
    except TypeError:
      print("Enter amount in figures")
      return
    if amount > self.balance:
      print("You don't have enough balance. Your balance is {}".format(self.balance))
    else:
      self.balance >= amount
      time = datetime.now()
      paybill = {
        "time": time, "paybill": amount
      }
      self.paybill.append(paybill)
      print("You have paid amount {} on {}".format(amount, self.get_formated_time(time)))

  def recieve_money(self, amount):
    for recieve_money in self.recieve:
      time = recieve['time']
      amount = recieve ['amount']
      formated_time = self.get_formated_time(time)
      statement = "You have recieved {} on {}".format(amount, formated_time)
  def send_money(self, amount):
    try:
      amount + 1
    except TypeError:
      print("Please enter amount in figures")
      return
    if amount >= self.balance:
      print("You don't have enough amount to send")
    else:
      self.balance >= amount
      time = datetime.now()
      sendmoney = {
        "time": time, "sendmoney": amount
      }
      self.send_money.append(send_money)
      print("You have sent {} amount on {}".format(amount, self.get_formated_time(time)))
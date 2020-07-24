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

  def phone_number(self, phone_number):
    contact = "Your phone_number {}".format(phone_number)
    return phone_number
  def deposit(self, amount):
    
    if amount <= 0:
      print("You can't deposit zero to your account".format(amount))
    else:
      self.balance += amount
      self.deposits.append(amount)
      print("You have deposited {} to your account".format(amount, self.account_name()))

  def withdraw(self, amount): 
    if amount == 0:
      print("You can't withdraw zero from your account".format(amount))
    elif amount > self.balance:
      print("You dont have enough balance")
    else:
      self.balance -= amount
      self.withdraw.append(amount)
      print("You have withdrawn {} from your account".format(amount,,self.account_name()))
  def get_balance(self):
    return"The balance for {} is {}".format(amount, self.balance)
  def show_deposit_statement(self):
    for deposit in sel.deposits:
      print(deposit)
  def show_withdrawals_statement(self):
    for withdrawal in self.withdrawals:
      print(withdrawal)
  def get_loan(self, amount):
    if amount <= 0:
      print("You cannot get loan of that amount")
    else:
      self.loan = amount
      print("You have been given loan of {}".format(amount))
    
 def pay_loan(self, amount):
    if amount <= 0:
      print("You cannot pay with that amount")
    elif self.loan == 0:
      print("You dont have a loan ata the moment")
    elif amount > self.loan:
      print("Your loan is paid amount")
    else:
      self.loan = amount
      print("You have paid your loan of {}".format(amout))
   



 #print(acc1.account_name())
 #print(acc2.account_name())   



#name = BankAccount("Lucy", "Wangui")
#name = BankAccount("Mark", "Maina")

#print(acc1.account_name())
#print(acc2.account_name())

#acc1.withdraw(500)
#acc2.withdraw(400)
#acc1.deposit(5000)
#acc2.deposit(489)

#acc1.phone_number(+2543678898)
#acc2.phone_number(+2546784367)


#print(acc1.get_balance())
#print(acc2.get_balance())

#print(acc1.account_name())
#print(acc2.account_name())

#acc1.deposit(15000)
#acc2.deposit(3000)
#acc1.withdraw(700)
#acc2.withdraw(500)

#print(acc1.get_loan(250))
#print(acc2.pay_loan(400))
#print("-------")


    
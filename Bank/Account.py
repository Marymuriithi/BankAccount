class BankAccount:
  bank = "KCB"
  
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.balance = 0
    
  def account_name(self):
    name = "{} account for {} {}". format(self.bank, self.first_name, self.last_name)
    return name
    
  def withdraw(self, amount):
    self.balance -= amount
    print("You have withdraw {} from your account".format(amount))
  
  def deposit(self, amount):
     self.balance += amount
     if amount <=0:
       print("You have deposited {} to your account". format(amount))
     else:
       print("No money deposited")
  def get_balance(self): 
    return "This {} is the current balance for {}". format(self.balance, self.account_name()) 
acc1 = BankAccount("Lucy", "Wangui")
acc2 = BankAccount("Mark", "Maina")

print(acc1.account_name())
print(acc2.account_name())

acc1.withdraw(500)
acc2.withdraw(400)
acc1.deposit(5000)
acc2.deposit(489)

print(acc1.get_balance())
print(acc2.get_balance())

print(acc1.account_name())
print(acc2.account_name())

acc1.deposit(15000)
acc2.deposit(3000)
acc1.withdraw(700)
acc2.withdraw(500)

print(acc1.get_balance())
print(acc2.get_balance())
print("-------")
    
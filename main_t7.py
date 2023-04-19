class User:

    def __init__(self, name, money, checking_account):
        self.name = name
        self.money = money
        self.checking_account = checking_account

    def withdraw(self,money_to_withdraw):
        if money_to_withdraw > self.money:
            raise ValueError('ERROR, not enough money!')
        self.money -= money_to_withdraw
        return f'{self.name} has {self.money}.'

    def add_cash(self,money_to_add):
        self.money += money_to_add
        return f'{self.name} has {self.money}.'

    def check(self, other_user, money_to_user):
        if not other_user.checking_account:
            raise ValueError("Other user doesn't have checking account.")
        if money_to_user > other_user.money:
            raise ValueError('ERROR, not enough money!')
        self.money += money_to_user
        other_user.money -= money_to_user
        return f'{self.name} has {self.money} and {other_user.name} has {other_user.money}.'

Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

print(Jeff.withdraw(2)) # Returns 'Jeff has 68.'

print(Joe.check(Jeff, 50)) # Returns 'Joe has 120 and Jeff has 18.'

# print(Jeff.check(Joe, 80)) # Raises a ValueError

Joe.checking_account = True # Enables checking for Joe

print(Jeff.check(Joe, 80)) # Returns 'Jeff has 98 and Joe has 40'

# print(Joe.check(Jeff, 100)) # Raises a ValueError

print(Jeff.add_cash(20.00)) # Returns 'Jeff has 118.'
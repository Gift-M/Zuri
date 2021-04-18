class Budget:

    def __init__(self, category):
        self.category = category
        self.balance = 0

    def deposit(self):
        amount = int(input('How much do you want to deposit: '))
        self.balance += amount
        print('Deposit {} to {} category'.format(amount, self.category))
        return 'Current balance is {}.'.format(self.balance)

    def withdrawal(self):
        amount = int(input('How much do you want to withdraw: '))
        if (amount > self.balance):
            print('Insufficient fund')
        else:
            self.balance -= amount
            print('You have withdrawn {} from {} category'.format(amount, self.category))
        return 'Current balance is {}'.format(self.balance)

    def transfer(self, amount, category):
        self.amount = amount
        self.category = category
        print('Transfer {} to {} category'.format(self.amount, self.category))
        if (amount > self.balance):
            print('Insufficient fund')
        else:
            self.balance -= amount
            print('You have transferred {} to {} category'.format(self.amount, self.category))
        return 'Current balance is {}'.format(self.balance)

    def balance(self):
       print('The balance is {}'.format(self.balance))

food = Budget('Food')
clothing= Budget('Clothing')
Entertainment= Budget('Entertainment')

food.deposit()
food.withdrawal()
food.transfer(3000, 'Entertainment')
food.balance()


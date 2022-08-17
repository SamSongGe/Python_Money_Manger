expenseAmount = 100; #set input expense amount here, per transaction
income = 500; #set input income value here
name = 'vedika'; #set input name value here
category = "Shopping"
bankrupt = False

class Ledger:
    
    def __init__(self, name):
        
        self.bankrupt = bankrupt;
        self.expense = 0.0;
        self.income = income
        self.name = name;
        self.surplus = self.income - self.expense;
        self.spending_categories ={"Automotive & Gas":0.0,"Utilities":0.0,"Education":0.0,
                                   "Entertainment":0.0,"Food & Drink":0.0,
                 "Groceries":0.0,"Miscellanous":0.0,"Shopping":0.0,"Travel":0.0}
        return;
        
    def credit(self, amount):  # credited amount
        self.income += amount;
        self.surplus = self.income - self.expense;
        return self.expense, self.surplus;

    def debit(self, amount, category): #amount of one debit transaction, category of transaction
        
        if (amount > self.surplus):
            print("You have exceeded your monthly income")
            bankrupt = True;
        else:
            self.expense +=amount;
            self.surplus = self.income - self.expense;
            
            if(category in self.spending_categories):
                self.spending_categories[category] += amount;
            else:
                self.spending_categories[category] = amount
            return self.expense, self.surplus;
    
    def getExpense(self):
        string = "" + self.name + "'s Expenses are : " + str(self.expense)
        return string
    
    def getIncome(self):
        string = "" + self.name + "'s Monthly Income is : " + str(self.income)
        return string;
    
    def getSurplus(self):
        string = "" + self.name + "'s Remaining Surplus is : " + str(self.surplus)
        return string;
    
    def getCategoryExpense(self, category):
        string = "" + self.name + "'s spending for " + category+ " is " + str(self.spending_categories[category])
        return string
    
    def getCategoryDict(self):
        return self.spending_categories



vedika = Ledger(name);


print(vedika.getIncome())
print(vedika.getExpense())
print(vedika.getSurplus())


vedika.debit(expenseAmount, category)


print(vedika.getCategoryExpense("Entertainment"))
#print(vedika.getCategoryExpense("Shopping"))

vedika.getCategoryDict()


print(vedika.income)
print(vedika.surplus)
print(vedika.expense)

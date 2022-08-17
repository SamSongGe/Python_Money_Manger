import sys
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox,QPushButton,QWidget

from PyQt5 import uic
import sys
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure
import numpy as np
import random
import matplotlib as mp



    


#import pyqtgraph as pg
#from pyqtgraph import PlotWidget, plot



class Ledger:

            def __init__(self,name,email,expense,income,category):





                self.bankrupt = bankrupt
                self.expense = expense
                self.income = income
                self.category = category
                self.name = name
                self.email= email
                self.surplus = self.income - self.expense
                self.spending_categories ={"Automotive & Gas":0.0,"Utilities":0.0,"Education":0.0,
                                           "Entertainment":0.0,"Food & Drink":0.0,
                                           "Groceries":0.0,"Miscellanous":0.0,"Shopping":0.0,"Travel":0.0}
                return;

            def credit(self, adding):  # credited amount
                self.income += adding
                self.surplus = self.income - self.expense
                return self.expense, self.surplus

            def debit(self, amount, category): #amount of one debit transaction, category of transaction

                if (amount > self.surplus):
                    print("You have exceeded your monthly income")
                    bankrupt = True;
                else:
                        self.expense +=amount;
                        self.surplus = self.income - self.expense;

                        if (category in self.spending_categories):
                            self.spending_categories[category] += amount;
                        else:
                                self.spending_categories[category] = amount
                        return self.expense, self.surplus;

            def getExpense(self):
                string = self.expense
                return string

            def getIncome(self):
                income = self.income
                return income;

            def getSurplus(self):
                string = self.surplus
                return string;

            def getCategoryExpense(self, category):
                string = self.spending_categories[category]
                return string

            def getCategoryDict(self):
                return self.spending_categories


qtCreatorFile = "project ui.ui"   #Enter file here

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)




class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.executeBT.clicked.connect(self.add_expense_and_income_bt)
        self.ui.firstButton.clicked.connect(self.get_output)
        self.ui.firstButton.clicked.connect(self.fill_from)
        self.ui.email_Button.clicked.connect(self.send_alert)
        #canvas = Canvas(self, width=3, height=3)
        #canvas.place(relx=0.5,rely=0.8)
        # self.plot()
        




    def get_info(self):
        global name
        global email
        global expense
        global income
        global category
        global bankrupt
        global user
        
        name=self.ui.name_box.toPlainText()
        email=self.ui.email_box.toPlainText()
        expense= int(self.ui.expense.toPlainText())
        income = int(self.ui.monthly_income.toPlainText()) #set input income value here
        category = self.ui.catalogs.currentText()
        bankrupt = False
        user = Ledger(name,email,expense,income,category)





    def get_output(self):
        self.get_info()
        self.ui.income_left.setText(str(user.getSurplus())) # left income output
        self.ui.total_expense.setText(str(user.getExpense())) #total expense output


    def add_expense_and_income_bt(self):
        expense = int(self.ui.expense.toPlainText())
        category = self.ui.catalogs.currentText()
        user.debit(expense,category)
        addIncome = int(self.ui.add_income.toPlainText())
        user.credit(addIncome)
        if int(self.ui.income_left.toPlainText())<expense :
            self.show_surplus()
            return

        self.ui.income_left.setText(str(user.getSurplus())) # left income output
        self.ui.total_expense.setText(str(user.getExpense()))

        print(user.getCategoryDict())
        print('utilities is ',user.spending_categories['Utilities'])
        print(user.getExpense())
        print(user.getSurplus())



#Create Pie Chart to show only categories that are non zero
        temp=user.spending_categories
        plotdic = {}
        for x, y in temp.items():
            if y != 0:
                plotdic[x] = y
        labels=plotdic.keys()
        expense=plotdic.values()


        fig1, ax1 = plt.subplots()

        ax1.pie(expense, labels=labels, autopct='%1.0f%%',
                shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show(fig1)


        #canvas = Canvas(self, width=3, height=3)

# Email Function code
    def send_alert(self):
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        #self.add_expense_and_income_bt()
        
        a = "Money Manager report for "+name+":"
        b = str(user.getCategoryDict())
        
        
        mylist =[a,b]
        
        fromaddr = "istm3119@gmail.com"
        toaddr = email
        msg4 = MIMEMultipart()
        msg4['From'] = fromaddr
        msg4['To'] = toaddr
        msg4['Subject'] = "Money Manager Alert"

        body = "\r\n".join(mylist)
        msg4.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL(host='smtp.gmail.com',port= 465)

        server.login("istm3119@gmail.com", "Python3119")
        text = msg4.as_string()
        server.sendmail(fromaddr, toaddr, text)



    def fill_from(self):
        income = self.ui.monthly_income.toPlainText()
        if not name:
            self.show_fillpopup()
        elif not income:
            self.show_fillpopup()
            return

    def show_fillpopup(self):
         msg = QMessageBox()
         msg.setWindowTitle("Fill Error!")
         msg.setText("Please fill the Name and Income!")
         msg.setIcon(QMessageBox.Information)
         x = msg.exec_()


    def show_surplus(self):
         msg2 = QMessageBox()
         msg2.setWindowTitle("Surplus Income Error!")
         msg2.setText("Warning: You are apporach your monthly income limit!\r\n Plase enter a number smaller than your left income")
         msg2.setIcon(QMessageBox.Warning)
         x = msg2.exec_()
         
         



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()


    exit(app.exec_())

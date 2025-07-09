# Project name banking system

print("M_S online banking system")
print("First signup your account")

class signup:
    @property
    def name(self):
        return f"{self.fname} {self.lname} you are successfull signup in application"
    @name.setter
    def name(self,name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]
#amna abdul rauf
    @property
    def pin(self):
        return self._pin
    @pin.setter
    def pin(self,new):
        if(new==int(new)):
            self._pin = new
        else:
            self._pin = "Pin must be in number not words"


a=input("Enter your account name: ")
try:
    p=int(input("Enter your account pin: "))
except:
    print("Warning enter only number")

acc=signup()
otr = acc.name = a
try: # this try is for pin code
    code = acc.pin = p
    with open("moiz.txt","w") as f:
        f.write(str(p))
    print(acc.name)
    
except:
    print("enter only number not words")
try: # this try is for name or pin
    if(otr==a and code == p):
        print("Salam")
        service = {
            "amount transfer" : "Amount transfer",
            "loan" : "Loan",
            "deposite" : "Deposite",
            "withdraw": "Withdraw"
        }
        print("Our services:\nAmount transfer\nLoan\nDeposite\nWithdraw")
        try: # This try is for dictionary
            w = input("Which do you want: ")
            which = w.lower()
            print(service[which])

            if(which=="amount transfer"):
                class transfer_money:
                    def __init__(self,balance):
                        self._balance = balance
                    @property
                    def trans_name(self):
                        return self.firstname, self.lastname
                    @trans_name.setter
                    def trans_name(self,name):
                        self.firstname = name.split(" ")[0]
                        self.lastname = name.split(" ")[1]

                    @property
                    def trans_money(self):
                        return self._transferm
                    @trans_money.setter
                    def trans_money(self,value):
                        if(value >self._balance):
                            self._transferm = "You have no balance to transfer"
                        else:
                            self._transferm = value
                            self._balance -= value
                    @property
                    def codepin(self):
                        return self._code
                    @codepin.setter
                    def codep(self,newpin):
                        if(newpin == code):
                            self._code = newpin
                            print(f"Account name {self.firstname} {self.lastname}\nTransfer {self._transferm} amount from {otr} was sucessfull\nand your balance after transfer is {self._balance}")
                        else:
                            print("Your pin was incorrect")
                balance = int(input("Enter your balance: "))
                transfern = input("Enter the account name which you want to transfer the amount: ")
                transferm = int(input("How much money do you want to transfer: "))
                pint = int(input("Enter you pin: "))
                t = transfer_money(balance)
                t.trans_name = transfern
                t.trans_money = transferm
                t.codep = pint

            elif(which == "loan"):
                print("You can take a loan of up to 100000 only, not more than that.")
                q = input("Do want to agree so write yes other wise no: ")
                question = q.lower()
                if(question =="yes"): # This if is for yes or no for loan
                    # amountl = int(input("Tell the amount you want to take as a loan: "))
                    class loan:
                        @property
                        def loanlimit(self):
                            return self._loanl
                        @loanlimit.setter
                        def loanlimit(self,value):
                            if(value <= 100000):  # This if is for loan limit cheacking
                                self._loanl = value
                            else:
                                print("Warning you enter a not unacceptable amount") # This else is for limit cheacking id
                        @property
                        def loanp(self):
                            return self._loanpin
                        @loanp.setter
                        def loanp(self,lp):
                            if(lp == code): # This if is for conformation pin code
                                self._loanpin = lp
                                print(f"You have successfully taken {self._loanl} loan, but your last date to repay the loan is 1st augest 2025")
                            else:
                                print("You enter a wrong pin")
                    loanamount = int(input("Tell the amount you want to take as a loan: "))
                    loanpin = int(input("Enter your code pin: "))
                    loanl = loan()
                    loanl.loanlimit = loanamount
                    loanl.loanp = loanpin
                else:
                    print("OK Jazakallah") # This else is for yes or no for loan
            
            elif(which == "deposite"):
                class deposite:
                    def __init__(self,balance):
                        self._balance = balance

                    @property
                    def amountd(self):
                        return self._deposite
                    @amountd.setter
                    def amountd(self,a):
                        if(a<=0):
                            print("Warning you are surrounded by security from all sides.")
                        else:
                            self._deposite = a
                            self._balance +=a
                    @property
                    def depop(self):
                        return self._depin
                    @depop.setter
                    def depop(self,dp):
                        if(dp == code): # This if is for conformation pin code
                            self._depin = dp
                            print(f"You amount {self._deposite} has been successfully deposited in your account {otr}, and now your amount is this after the deposite {self._balance}")

                        else:
                            print("You enter a wrong pin")

                b = int(input("Enter you balance: "))
                dep = int(input("How much amount would you like to deposite: "))
                dpin = int(input("Enter your code pin: "))
                d = deposite(b)
                d.amountd = dep
                d.depop = dpin

            elif(which == "withdraw"):
                class withdraw:
                    def __init__(self,balance):
                        self._balance = balance
                    @property
                    def withd(self):
                        return self._amount
                    @withd.setter
                    def withd(self,am):
                        if(am<= self._balance): # This if is for checking balance amount and withdraw amount
                            self._amount = am
                            self._balance -=am
                        else:  # This else is withdraw checking
                            print(f"You balance is not able for withdraw {am} rupees") 
                    @property
                    def wpop(self):
                        return self._depin
                    @wpop.setter
                    def wpop(self,dp):
                        if(dp == code): # This if is for conformation pin code
                            self._depin = dp
                            print(f"You withdraw {self._amount} rupees and your balance after withdraw is {self._balance}")
                        else:
                            print("You enter a wrong pin")

                withb = int(input("Enter your balance: "))
                witha = int(input("How much amount would you like to withdraw?: "))
                withp = int(input("Enter the pin code: "))
                z = withdraw(withb)
                z.withd = witha
                z.wpop = withp

        except:
            print("You enter some thing wrong")        

except:
    print("")



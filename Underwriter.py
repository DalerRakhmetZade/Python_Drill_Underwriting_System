#Python:    (2.7.13)
#Author:    Daler Rakhmet-Zade
#Website:   bolddeveloper.com
#Purpose:   The Tech Academy Python Course Drill, Item 36
#           Demonstrating how to pass variables from function to function
#           while producing car loan automated underwriting system

import time #time module to create a "processing" effect while waitng on decision

def start(rate=0.025,amount=0,term=0,credit_score=0,dti=0,payment=0,name=""):
    name = client(name)
    proceed()
    amount = request_amount(amount)
    rate,term = request_term(rate,term)
    rate,dti = debt_to_income(rate,dti)
    rate,credit_score = request_credit(rate,credit_score)
    r = (rate / 12)  
    payment,amount,r,term = monthly_payment(payment,amount,r,term)
    process()
    name,rate,amount,term,payment = decision(name,rate,amount,term,payment)
    rate,amount,term,credit_score,dti,payment,name = follow_up(rate,amount,term,credit_score,dti,payment,name)
     
def client(name): 
    if name !="": #Assigning string to a variable 
        print("\nThank you for using our services again, {}!".format(name))
    else:
        run = True
        while run: #Use of a while loop
            if name == "":
                name = raw_input("Hello! What is your name? : ").capitalize()
                if name !="":
                    print("\n{}, let's get you pre-approved for an auto loan!".format(name))
                    print("The process should take no more than 5 minutes...")
                    run = False
    return name

def proceed():
    run = True
    while run: #Use of a while loop
        choice = raw_input("\nWould you like to proceed? y/n: ").lower()
        if choice == "y":
            run = False
            return proceed
        if choice == "n":
            print ("It's OK! Let's submit your application later. See you soon ...")
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', 'n' for 'NO'...")

def request_amount(amount):
    print("\nGreat! Let's get started...")
    amount = int(raw_input("How much $ would you like to borrow? : $"))#Assigning integer to a variable
    print ("You can get a pretty nice car for ${}".format(amount))
    return amount

def request_term(rate,term):
    run = True
    while run: #Use of a while loop
        term = int(raw_input("\nPlease choose one of the following terms for your loan - 36/48/60 :"))
        if term == 36:
            rate = (rate + 0)
            run = False
            return rate,term
        
        if term == 48:
            rate = (rate + 0.0025)
            run = False
            return rate,term
        if term == 60:
            rate = (rate + 0.0050)
            run = False
            return rate,term
        else: # Use of conditional statements: else
            print("\nPlease enter '36' for '36 Months', '48' for '48 Months', '60' for '60 Months'...")
    
def debt_to_income(rate,dti):
    run = True
    while run: #Use of a while loop
        expense = float(raw_input("\nHow much $ do you pay for your rent or mortgage? : $"))#Assigning Float to a variable
        income = float(raw_input("\nWhat is your gross monthly income? : $"))
        dti = (expense / income)
        if dti <= 0.43: # Use of conditional statements: if, elif
            rate = (rate + 0)
            run = False
            return rate,dti
        elif 0.44 <= dti <= 0.70:
            rate = (rate + 0.0025)
            run = False
            return rate,dti
        elif dti >= 0.71:
            rate = (rate + 0.0050)
            run = False
            return rate,dti
    
def request_credit(rate,credit_score):
    run = True
    while run: #Use of a while loop
        credit_score = int(raw_input("\nWhat is your FICO credit score?  350-850 :"))
        if 850 >= credit_score >= 730:
            rate = (rate + 0)
            run = False
            return rate,credit_score
        if 729 >= credit_score >= 700:
            rate = (rate + 0.0025)
            run = False
            return rate,credit_score
        if 699 >= credit_score >= 660:
            rate = (rate + 0.0050)
            run = False
            return rate,credit_score
        if 659 >= credit_score >= 620:
            rate = (rate + 0.0125)
            run = False
            return rate,credit_score
        if 619 >= credit_score >= 580:
            rate = (rate + 0.0200)
            run = False
            return rate,credit_score
        if 579 >= credit_score >=350 :
            rate = (rate + 0.0500)
            run = False
            return rate,credit_score
        else :
            print ("\nPlease input your FICO credit score in range from '350' to '850'...")#Using Print function 
            
def monthly_payment(payment,amount,r,term):
    payment = '{:.2f}'.format(amount*((r*(1+r)**(term))/((1+r)**(term)-1)))#using .format() notation #using  +, - , * , / , =, ** operators
    return payment,amount,r,term

def process():
    print("\nThank you for submitting your application! Please give us a moment to review your application.")
    time.sleep(5)
    
def decision(name,rate,amount,term,payment):
    run = True
    while run: #Use of a while loop
        if rate <= 0.0575:    
            print("\nCongratulations, {}! Your application request has been APPROVED for the following terms:\n\nApproved amount: ${}.00 \nAPR: {}% \nTerm: {} Months \nMonthly payment: ${}").format(name,amount,rate * 100,term,payment)
            run = False
            return name,rate,amount,term,payment
        elif rate > 0.0575:
            print("\n{}, thank you for your request. Unfortunately, we cannot approve your application at this time...").format(name)
            run = False
            again(rate,amount,term,credit_score,dti,payment,name)
def follow_up(rate,amount,term,credit_score,dti,payment,name):
    time.sleep(5)
    print("\n{}, please send the following documents to myemail@nobank.com to finalize your loan:").format(name)
    docs = ['Valid Driver License','Proof Of Insurance','Proof Of Income']
    for i in docs: #Use of a for loop
        print i
    run = True
    while run: #Use of a while loop
        choice = raw_input("\nWould like to get another pre-approval? y/n: ").lower()
        if choice == "y":
            run = False
            reset(rate,amount,term,credit_score,dti,payment,name)
        if choice == "n":
            print("\nThank you for your business! See you later...")
            run = True
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', 'n' for 'NO'...")
            
def reset(rate,amount,term,credit_score,dti,payment,name):
    rate=0.025
    amount=0
    term=0
    credit_score=0
    dti=0
    payment=0
    start(rate,amount,term,credit_score,dti,payment,name)
    

            
if __name__ == "__main__":
    start()

import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nirmal"
)
mycursor = mydb.cursor()
mycursor.execute("use dbmsproject")

enter_exit = 0
while(enter_exit!=4):
    def HomeUI():
        print("Do You want to login as:- ")
        print("\t1. Customer")
        print("\t2. Retailer")
        print("\t3. Delivery Person")
        print("\t4.Exit the Application.")
        enter_exit = 0
        rep = 0
        while(enter_exit!=1 and enter_exit!=2 and enter_exit!=3 and enter_exit!=4):
            if(rep>=1):
                print("!!!!!!!!!!!!!!!!!!!! Invalid Entry !!!!!!!!!!!!!!!!!!")
                print("\t1. Customer")
                print("\t2. Retailer")
                print("\t3. Delivery Person")
                print("\t4.Exit the Application.")
            
            print("Enter:- ")
            enter_exit = int(input())
            rep = rep+1

        
        if(enter_exit == 1):
            print("------------------ You've Logged-IN as a Customer -------------------\n")
            mode = 0
            while(mode != 3):
                print("Choose what you want to see or edit")
                rep = 0
                mode = 0
                while(mode!=1 and mode!=2 and mode!=3):
                    if(rep >= 1):
                        print("!!!!!!!!!!!!!!!!!!!! Invalid Entry !!!!!!!!!!!!!!!!!!")
                        print("Choose what you want to see or edit")

                    print("\tEnter 1 if you want to view Products.\n")
                    print("\tEnter 2 if you want to Add a product to the Cart or Wants to view Your Cart\n")
                    print("\tEnter 3 if you want to place the Order.\n")
                    print("Enter: ")

                    rep = rep+1
                    mode = int(input())

                    if(mode == 1): #this is for viewing prodduc.
                        print("---------- Below is the Products List ---------")
                        mycursor.execute("SELECT * FROM Customer")
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            print(x)
                    
                    elif(mode == 2):  #this is for adding/viewing the cart.
                        print("------------ Do You Want to Add a Product to the Cart Or Wants to see the Cart? -------------- \n")
                        op = 0
                        rep = 0
                        while(op!=2):
                            if(rep>=1):
                                print("!!!!!!!!!!!!!!!!!!!! Invalid Entry !!!!!!!!!!!!!!!!!!")
                                print("------------ Do You Want to Add a Product to the Cart Or Wants to see the Cart? -------------- \n")



                            print("\tEnter 1 if you want to see the Cart.")
                            print("\tEnter 2 if you want to Add to the Cart.")
                            print("Enter: ")

                            op = int(input())
                            if(op == 1):
                                print("---------- Below is the Cart List ---------")
                                mycursor.execute("SELECT * FROM Cart")
                                myresult = mycursor.fetchall()
                                for x in myresult:
                                    print(x)
                        
                            elif(op == 2):
                                print("------------ Kindly Enter your Product_ID, Customer_ID and your Product Quantity. -----------")
                                inp_prodid = int(input())
                                inp_custid = int(input())
                                inp_prodquant = int(input())
                                mycursor.execute(f"INSERT INTO Cart(Cart_Product_ID, Cart_Customer_ID, Cart_product_quantity) VALUES ({inp_prodid},{inp_custid},{inp_prodquant})")
                                mydb.commit()

                    elif(mode == 3):    #this is for placing the Order
                        print(":::::::::::::::: If you're DONE with shopping then kindly follow the below steps in order to place the Order ::::::::::::::::::")
                        print("\t Enter 1 to place the Order.")
                        print("\t Enter 2 If you don't want to place the Order and wants to exit without making any payment.")
                        place = int(input())
                        if(place == 1):
                            print("//////////////////////////////// THANKS SO MUCH FOR SHOPPING AT THE VIRTUAL BAZAAR //////////////////////////////////")
                            mycursor.execute("SELECT * FROM Final_Order")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                print(x)







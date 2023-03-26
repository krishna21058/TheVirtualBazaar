import mysql.connector
from datetime import date


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="krishna1",
    database="dbmsproject"
)

mycursor = mydb.cursor()

while (True):
    print(":::::::::::::::::::::::::::::::::: Welcome to The Virtual Bazaar :::::::::::::::::::::::::::::::::::::::\n")
    print(".................................. Select one of the following options: ................................\n")
    print("\tEnter 1. to Sign Up")
    print("\tEnter 2. to Login")
    print("\tEnter 3. See some statistics")

    inp_home = int(input())
    if (inp_home == 1):
        print(">>>>>>>>>>>>>>>>>> Please Enter Your Details to Complete the SignUp <<<<<<<<<<<<<<<<<<<<<<<")
        print("-> Enter Your Username:- ")
        inp_signup_username = input()
        print("-> Enter Your Password:- ")
        inp_signup_pass = input()
        if (len(inp_signup_pass) <= 5):
            print(
                "!!!!!!!!!!!!!!!!!!!!!!!! Password should have length of 5 or more! !!!!!!!!!!!!!!!!!!!!!!!!!!")
            break

        print("-> Enter Your Login Type:- ")
        inp_signup_logintype = input()
        print()
        mycursor.execute(
            f"INSERT INTO Login(Login_username,password,login_type) VALUES('{inp_signup_username}','{inp_signup_pass}','{inp_signup_logintype}')")
        mydb.commit()

    elif(inp_home==3):
        input_stats=int(input())
        if(input_stats==1):
            mycursor.execute(f'''SELECT Product_Quantity, NULL AS Product_name, ROUND(AVG(Product_price_in$),2)
                                FROM Product
                                GROUP BY Product_Quantity
                                UNION ALL
                                SELECT NULL AS Product_Name, Product_name, ROUND(AVG(Product_price_in$),2)
                                FROM Product
                                GROUP BY Product_name;''')
            
            myresult = mycursor.fetchall()

                                # Print the column headers
            # print("Orders_from\tAge_Group\tNumber_Of_Orders")

                                # Print each row of the result
            for row in myresult:
                print(row)
        elif(input_stats==2):
            mycursor.execute(f'''SELECT  
                    IF(GROUPING(c.category_name), 'All Categories ', c.category_name) AS Category_Name, 
                    IF(GROUPING(p.product_name), 'All Products', p.product_name) AS Product_Name,
                    ROUND(AVG(p.product_price_in$ *(1-(p.product_discount/100))),2) AS Avg_Cost
                    FROM product AS p INNER JOIN category AS c ON c.category_id = p.product_category_id
                    GROUP BY p.product_name,c.category_name WITH ROLLUP;
                    ''')
            
            myresult = mycursor.fetchall()
            for row in myresult:
                print(row)            


    elif (inp_home == 2):
        print(">>>>>>>>>>>>>>>>>> Please Enter Your Details to Complete the LogIn <<<<<<<<<<<<<<<<<<<<<<<")
        print("-> Enter Your Username:- ")
        inp_signin_username = input()
        print("-> Enter Your Password:- ")
        inp_signin_pass = input()
        print("-> Enter Your LogIn Type:- ")
        inp_signup_logintype = input()
        mycursor.execute(
            f"SELECT Login_ID FROM Login WHERE Login_username = '{inp_signin_username}' AND Password='{inp_signin_pass}' AND Login_Type='{inp_signup_logintype}'")

        result = mycursor.fetchone()
        login_id = result[0]
        mycursor.fetchall()
        exists = bool(result)
        if (exists):
            if (inp_signup_logintype == "Customer"):
                print(
                    "------------------ You've Logged-IN as a Customer -------------------\n")
                inp_customer_fn = input()
                inp_customer_ln = input()
                inp_customer_age = input()
                inp_customer_street = int(input())
                inp_customer_distr = input()
                inp_customer_state = input()
                inp_customer_pin = input()
                inp_customer_phone = input()

                mycursor.execute(
                    f"INSERT INTO Customer(FirstName, LastName, Age, Street_Number, District, State, Pincode, Phone, CLogin_ID) VALUES('{inp_customer_fn}', '{inp_customer_ln}', {inp_customer_age}, {inp_customer_street}, '{inp_customer_distr}', '{inp_customer_state}', {inp_customer_pin}, {inp_customer_phone}, {login_id})"
                )
                mydb.commit()
                mode = 0
                # if result:
                print(login_id)

                mycursor.execute(
                    f"SELECT Customer_ID FROM Customer WHERE cLogin_ID = {login_id}")
                c_id = mycursor.fetchone()
                cust_id = c_id[0]
                mycursor.fetchall()

                # else:
                #     c_id = None
                print(c_id)
                while (mode != 3):
                    print("Choose what you want to see or edit")
                    print()
                    rep = 0
                    mode = 0
                    while (mode != 1 and mode != 2 and mode != 3):
                        if (rep >= 1):
                            print(
                                "!!!!!!!!!!!!!!!!!!!! Invalid Entry !!!!!!!!!!!!!!!!!!")
                            print("Choose what you want to see or edit")

                        print("\tEnter 1 if you want to view Products.\n")
                        print(
                            "\tEnter 2 if you want to Add a product to the Cart or Wants to view Your Cart\n")
                        print("\tEnter 3 if you want to place the Order.\n")
                        print("\tEnter 4 if you want to see our minimum prices.\n")
                        rep = rep+1
                        print("-> Enter:- ")
                        mode = int(input())

                        if (mode == 1):  # this is for viewing product.
                            print("---------- Below is the Products List ---------")
                            mycursor.execute("SELECT * FROM Product")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                print(x)

                        # this is for adding/viewing the cart.
                        elif (mode == 2):
                            print(
                                "------------ Do You Want to Add a Product to the Cart Or Wants to see the Cart? -------------- \n")
                            op = 0
                            rep = 0
                            while (op != 2):
                                if (rep >= 1):
                                    print(
                                        "!!!!!!!!!!!!!!!!!!!! Invalid Entry !!!!!!!!!!!!!!!!!!")
                                    print(
                                        "------------ Do You Want to Add a Product to the Cart Or Wants to see the Cart? -------------- \n")

                                print("\tEnter 1 if you want to see the Cart.")
                                print("\tEnter 2 if you want to Add to the Cart.")
                                print("Enter: ")

                                op = int(input())
                                if (op == 1):
                                    print(
                                        "---------- Below is the Cart List ---------")

                                    mycursor.execute(
                                        f"SELECT * FROM Cart WHERE cart_Customer_ID={cust_id}")
                                    myresult = mycursor.fetchall()
                                    for x in myresult:
                                        print(x)

                                elif (op == 2):
                                    print(
                                        "------------ Kindly Enter your Product_ID, Customer_ID and your Product Quantity. -----------")
                                    global inp_prodid
                                    inp_prodid = int(input())

                                    inp_prodquant = int(input())
                                    mycursor.execute(
                                        f"INSERT INTO Cart(Cart_Product_ID, Cart_Customer_ID, Cart_product_quantity) VALUES ({inp_prodid},{cust_id},{inp_prodquant})")
                                    print(
                                        "------------- Data Have Been SUCCESSFULLY Added. ---------------")
                                    mydb.commit()

                        elif (mode == 3):  # this is for placing the Order
                            print(
                                ":::::::::::::::: If you're DONE with shopping then kindly follow the below steps in order to place the Order ::::::::::::::::::")
                            print("\t Enter 1 to place the Order.")
                            print(
                                "\t Enter 2 If you don't want to place the Order and wants to exit without making any payment.")
                            place = int(input())
                            if (place == 1):
                                print(
                                    "//////////////////////////////// THANKS SO MUCH FOR SHOPPING AT THE VIRTUAL BAZAAR //////////////////////////////////")

                                mycursor.execute(
                                    f"INSERT INTO Final_Order(Order_Customer_id,Order_product_id, Total_Charges, Ordered_date) VALUES ({cust_id},{inp_prodid},10.5,'{date.today()}')")
                                myresult = mycursor.fetchall()
                                for x in myresult:
                                    print(x)
                        elif (mode==4):
                            mycursor.execute(f'''SELECT 
                                            IF(GROUPING(p.product_name), 'All Products', p.product_name) AS Product_Name,
                                            ROUND(MIN(p.product_price_in$ *(1-(p.product_discount/100))),2) AS Min_Cost_After_Discount_in$
                                            FROM product AS p
                                            GROUP BY p.product_name WITH ROLLUP;
                                                ''')
                            myresult = mycursor.fetchall()

                            # Print the column headers
                            # print("Orders_from\tAge_Group\tNumber_Of_Orders")

                            # Print each row of the result
                            for row in myresult:
                                print(row)
                                

            elif (inp_signup_logintype == "Retailer"):

                print(
                    "------------------ You've Logged-IN as a Retailer -------------------\n")
                inp_retailer_fn = input()
                inp_retailer_ln = input()
                inp_retailer_age = input()
                inp_retailer_addr = input()
                inp_retailer_phone = input()

                mycursor.execute(
                    f"INSERT INTO Retailer(FirstName, LastName, Age, Address, Phone, RLogin_ID) VALUES('{inp_retailer_fn}', '{inp_retailer_ln}', {inp_retailer_age},'{inp_retailer_addr}', {inp_retailer_phone}, {login_id})"
                )
                mydb.commit()

                mycursor.execute(
                    f"SELECT Retailer_ID FROM Retailer WHERE RLogin_ID = {login_id}")
                r_id = mycursor.fetchone()
                ret_id = r_id[0]
                mycursor.fetchall()

                retailer = 0
                print("     Enter 1. to Add Products to the Store.")
                print(
                    "     Enter 2. to See the Customers Statistics For a particular Product ID.")

                retailer = int(input())
                if (retailer == 1):
                    print(
                        ">>>>>>>>>>>>> Kindly Enter the below details in Order to add the Products to the Store. <<<<<<<<<<<<<")
                    print("-> Enter the Product ID:- ")
                    prodid = int(input())
                    print("-> Enter the Product Category ID:- ")
                    prod_catid = int(input())
                    print("-> Enter the Product Price in $:- ")
                    prod_price = float(input())
                    print("-> Enter the Product Name:- ")
                    prod_name = input()
                    print("-> Enter the Product Discount:- ")
                    prod_disc = int(input())
                    print("-> Enter the Product Quantity:- ")
                    prod_quant = int(input())
                    mycursor.execute(
                        f"INSERT INTO Product(product_ID,Product_Category_ID, product_price_in$, Product_name,Product_Discount,Product_Quantity) VALUES ({prodid},{prod_catid},{prod_price},'{prod_name}',{prod_disc},{prod_quant})")
                    print(
                        "------------- Data Have Been SUCCESSFULLY Added. ---------------")
                    mydb.commit()

                elif (retailer == 2):
                    print(
                        ">>>>>>>>>>>>> Enter 1 To See the Customers Statistics For a particular Product ID. <<<<<<<<<<<<<")
                    input_R = int(input("\tEnter:\t"))
                    if (input_R == 1):
                        mycursor.execute(f'''SELECT
                                                IF(GROUPING(c.state), 'All states', c.state) AS Orders_from,
                                                IF(GROUPING(c.age), 'All Age Groups', CONCAT(FLOOR(c.age/10)*10, '-', FLOOR(c.age/10)*10+9)) AS Age_Group,
                                                COUNT(c.customer_id) AS Number_Of_Orders
                                                FROM final_order AS o
                                                INNER JOIN customer AS c ON c.customer_id=o.order_customer_id
                                                INNER JOIN store AS s ON s.store_product_id=o.order_product_id
                                                WHERE s.store_retailer_id={ret_id}
                                                GROUP BY c.state, c.age WITH ROLLUP
                                                ''')
                        myresult = mycursor.fetchall()

                        # Print the column headers
                        print("Orders_from\tAge_Group\tNumber_Of_Orders")

                        # Print each row of the result
                        for row in myresult:
                            print(f"{row[0]}\t{row[1]}\t{row[2]}")

            elif (inp_signup_logintype == "Delivery Person"):
                
                print(
                    "------------------ You've Logged-IN as a Delivery Person -------------------\n")
                print(
                    ">>>>>>>>>>>>>>>>>> Kindly Enter the Product ID in Order to see the Delivery Date. <<<<<<<<<<<<<<<<<<<")
                order_id = int(input())
                mycursor.execute(
                    f"SELECT delivery_customer_id, date from Delivery where Delivery_Order_ID={order_id}")

                myresult = mycursor.fetchall()
                for row in myresult:
                    print(row)
                print()
                

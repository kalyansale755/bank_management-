from db import cursor, db

class Customer:

    def register(self, name, email, password, phone):

        query = """
        INSERT INTO customers(name,email,password,phone)
        VALUES(%s,%s,%s,%s)
        """

        values = (name, email, password, phone)

        cursor.execute(query, values)
        db.commit()

        print("Registration Successful - customer.py:17")


    def login(self, email, password):

        query = """
        SELECT * FROM customers
        WHERE email=%s AND password=%s
        """

        cursor.execute(query, (email, password))

        user = cursor.fetchone()

        if user:
            print("Login Successful - customer.py:32")
            return user

        else:
            print("Invalid Credentials - customer.py:36")
            return None
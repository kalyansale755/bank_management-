from db import cursor, db

class BankAccount:

    def __init__(self, customer_id):
        self.customer_id = customer_id


    def deposit(self, amount):

        query = """
        UPDATE customers
        SET balance = balance + %s
        WHERE customer_id=%s
        """

        cursor.execute(query, (amount, self.customer_id))

        db.commit()

        tquery = """
        INSERT INTO transactions(customer_id,transaction_type,amount)
        VALUES(%s,'Deposit',%s)
        """

        cursor.execute(tquery, (self.customer_id, amount))

        db.commit()

        print("Amount Deposited - account.py:30")


    def withdraw(self, amount):

        cursor.execute(
            "SELECT balance FROM customers WHERE customer_id=%s",
            (self.customer_id,)
        )

        balance = cursor.fetchone()[0]

        if balance >= amount:

            query = """
            UPDATE customers
            SET balance = balance - %s
            WHERE customer_id=%s
            """

            cursor.execute(query, (amount, self.customer_id))

            db.commit()

            tquery = """
            INSERT INTO transactions(customer_id,transaction_type,amount)
            VALUES(%s,'Withdraw',%s)
            """

            cursor.execute(tquery, (self.customer_id, amount))

            db.commit()

            print("Withdrawal Successful - account.py:63")

        else:
            print("Insufficient Balance - account.py:66")


    def check_balance(self):

        query = """
        SELECT balance FROM customers
        WHERE customer_id=%s
        """

        cursor.execute(query, (self.customer_id,))

        balance = cursor.fetchone()[0]

        print("Current Balance: - account.py:80", balance)


    def mini_statement(self):

        query = """
        SELECT transaction_type, amount, transaction_date
        FROM transactions
        WHERE customer_id=%s
        ORDER BY transaction_date DESC
        LIMIT 5
        """

        cursor.execute(query, (self.customer_id,))

        data = cursor.fetchall()

        for i in data:
            print(i)
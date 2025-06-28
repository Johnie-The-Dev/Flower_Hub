import mysql.connector

def get_connection():
	connection = mysql.connector.connect(
		host='localhost',  # Replace with your MySQL host
		user='root',
		password='your_password_here',  # Replace with your MySQL password
		port=3306,  # Default MySQL port
		# If you have a different port, change it accordingly
		# For example, if your MySQL server is running on port 3307, use port=3307
		# If you are using a different user or password, change them accordingly
		database='flowerhub'  # Replace with your database name
	)
	return connection

def add_flower(name, quantity, price):
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute(
		"INSERT INTO flowers (name, quantity, price) VALUES (%s, %s, %s)",
		(name, quantity, price)
	)
	conn.commit()
	cursor.close()
	conn.close()

def delete_sold_flower(flower_id, quantity_sold):
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute(
		"UPDATE flowers SET quantity = quantity - %s WHERE id = %s",
		(quantity_sold, flower_id)
	)
	conn.commit()
	cursor.close()
	conn.close()

def delete_spoilt_flower(flower_id, quantity_spoilt):
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute(
		"UPDATE flowers SET quantity = quantity - %s WHERE id = %s",
		(quantity_spoilt, flower_id)
	)
	conn.commit()
	cursor.close()
	conn.close()

def get_available_flowers():
	conn = get_connection()
	cursor = conn.cursor(dictionary=True)
	cursor.execute("SELECT * FROM flowers WHERE quantity > 0")
	flowers = cursor.fetchall()
	cursor.close()
	conn.close()
	return flowers

def get_total_flowers():
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT SUM(quantity) FROM flowers")
	total = cursor.fetchone()[0]
	cursor.close()
	conn.close()
	return total

def add_transaction(custname, custid, county, town, ftype, nflowers, price):
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute(
		"INSERT INTO transactions (custname, custid, county, town, ftype, nflowers, price) VALUES (%s, %s, %s, %s, %s, %s, %s)",
		(custname, custid, county, town, ftype, nflowers, price)
	)
	conn.commit()
	cursor.close()
	conn.close()

def get_available_transaction():
	conn = get_connection()
	cursor = conn.cursor(dictionary=True)
	cursor.execute("SELECT * FROM transactions")
	transaction = cursor.fetchall()
	cursor.close()
	conn.close()
	return transaction
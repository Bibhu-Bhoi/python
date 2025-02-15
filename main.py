import sqlite3 

# Connect to the SQLite database or create it if it doesn't exist
conn = sqlite3.connect('test.db') 

# Print message if the database is opened successfully
print("Opened database successfully") 

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define the SQL query to create the COMPANY table
create_table_query = '''
CREATE TABLE IF NOT EXISTS COMPANY (
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
);
'''

# Execute the SQL query to create the table
cursor.execute(create_table_query)

# Define the data to be inserted into the COMPANY table
data_to_insert = [
    (1, 'Paul', 32, 'California', 20000.00),
    (2, 'Allen', 25, 'Texas', 15000.00),
    (3, 'Teddy', 23, 'Norway', 20000.00),
    (4, 'Mark', 25, 'Rich-Mond', 65000.00)
]

# Insert data into the COMPANY table
cursor.executemany("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?, ?)", data_to_insert)

# Commit the changes to the database
conn.commit() 

# Print message if records are created successfully
print("Records created successfully")
cursor.execute("select * from company")
print("id:",i[0])
print("name:",i[1])
print("age:",i[2])


# Close the database connection
conn.close()

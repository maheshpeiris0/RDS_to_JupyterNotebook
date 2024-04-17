import psycopg2

# Set up database connection parameters
dbname = "your_dbname"
user = "your_username"
password = "your_password"
host = "localhost"  # or the IP address of your database server
port = "5432"       # default PostgreSQL port

# Establish a connection to the database
try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Database connection established.")
    
    # Create a cursor object using the connection
    cursor = connection.cursor()
    
    # Execute a query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("PostgreSQL version:", db_version)
    
    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as e:
    print("An error occurred:", e)

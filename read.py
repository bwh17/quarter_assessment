import sqlite3

def get_table_names():
    # Connect to the SQLite database
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Fetch all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()

    # Close the connection
    conn.close()

    return [name[0] for name in table_names]

def get_all_data_from_table(table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Fetch all data from the specified table
    cursor.execute(f"SELECT * FROM {table_name};")
    all_data = cursor.fetchall()

    # Close the connection
    conn.close()

    return all_data

# Example usage:

# Get all table names
table_names = get_table_names()
print("Table Names:", table_names)

# Get all data from a specific table (replace 'economics' with the desired table name)
table_data = get_all_data_from_table('economics')
print("Data from Economics Table:", table_data)
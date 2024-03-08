import sqlite3

def create_table(category):
    # Connect to the SQLite database
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Use lowercase category name as the table name
    table_name = category.lower()
    
    # Create table with columns: id, question, answer
    create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        );
    '''
    cursor.execute(create_table_query)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def add_data(category, question, answer):
    # Connect to the SQLite database
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Use lowercase category name as the table name
    table_name = category.lower()

    # Insert data into the table
    insert_data_query = f'''
        INSERT INTO {table_name} (question, answer) VALUES (?, ?);
    '''
    cursor.execute(insert_data_query, (question, answer))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Example usage:

# Create a new table for 'Economics'
create_table('Economics')

# Add data to the 'Economics' table
add_data('Economics', 'What is supply and demand?', 'Supply and demand are fundamental concepts in economics.')

# Repeat the add_data function with generative AI output for additional questions

# You can use a loop or any other method to generate and add multiple questions for each category
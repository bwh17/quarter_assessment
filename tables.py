import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Create tables for each category
categories = ['Accounting', 'Marketing', 'Stats', 'DS3860', 'DS3850']

for category in categories:
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
    
    # Insert 10 sample questions for each category
    for i in range(1, 11):
        question = f'What is the {i}-th question about {category}?'  # You can replace this with your generative AI output
        answer = f'This is the correct answer for the {i}-th question.'  # Replace with the correct answer
        insert_data_query = f'''
            INSERT INTO {table_name} (question, answer) VALUES (?, ?);
        '''
        cursor.execute(insert_data_query, (question, answer))

# Commit changes and close the connection
conn.commit()
conn.close()
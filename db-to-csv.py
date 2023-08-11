import mysql.connector
import csv
import argparse

def main(output_file):
    # Database connection details
    db_config = {
        'host': 'host1',
        'database': 'db1',
        'user': 'user1',
        'password': 'pass1'
    }

    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Your multiline complex query goes here
    query = """
    SELECT 
        column1, column2, column3
    FROM 
        your_table_name
    WHERE 
        some_conditions;
    """

    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Column names (headers)
    column_names = [desc[0] for desc in cursor.description]

    # Save the results to the specified CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(column_names)
        for row in results:
            writer.writerow(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()

    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save database query results to a CSV file.")
    parser.add_argument("output_file", help="Name of the output CSV file.")
    args = parser.parse_args()
    
    main(args.output_file)

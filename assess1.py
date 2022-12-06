#! python3

# Importing necessary libraries
import psycopg2

### Functions ###


def connect_db():
    """ Connects to the database

    Returns:
        Object: Database connection
    """

    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="assessment",
            user="postgres",
            password="MisoDaisy"
        )

        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# TODO 2. Fetch data
# TODO 2.1 Print to console
# TODO Commit


def list_data(conn):
    print("Do something")


# TODO 4. Insert function
def insert_data(conn):
    print("Do something")


# TODO 5. Delete function
def delete_data(conn):
    print("Do something")


def save_changes(conn):
    """ Commits changes to the database.

    Args:
        conn Object: Database connection
    """
    conn.commit()


# Running the program
conn = connect_db()

while True:
    user_input = input("Command: ").strip().split()

    user_input[0] = user_input[0].upper()

    # Formatting name
    name = " ".join(user_input[1:3])
    name = name.title()

    # Selection menu
    # LIST
    if user_input[0] == "LIST":
        list_data(conn)

    # ADD
    elif user_input[0] == "INSERT":
        insert_data(conn)

    # DELETE
    elif user_input[0] == "DELETE":
        delete_data(conn)

    # QUIT
    elif user_input[0] == "QUIT":
        print("Commiting all changes.")
        save_changes(conn)
        print("Connection to database closed.")
        print("Good bye!")
        break

    # Wrong input
    else:
        print("Please enter a valid command.")
        print("""LIST
LIST first_name last_name number
DELETE first_name last_name
QUIT""")

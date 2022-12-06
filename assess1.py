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


def list_data(conn):
    try:
        # Create a cursor.
        cur = conn.cursor()

        # Executing a statement.
        cur.execute("SELECT * FROM view_contacts;")

        # Check return from executed statement.
        rows = cur.fetchall()

        if rows is None:
            print("It seems as if there are no saved contacts.")
        else:
            print("Number of entries: " + str(cur.rowcount))
            for row in rows:
                print(f"{row[0]} {row[1]}, {row[2]}, {row[3]}, {row[4]}")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Close communication with databäase.
        cur.close()


def insert_data(conn):
    try:
        # Create a cursor.
        cur = conn.cursor()

        # Get relevant information
        contacts_first_name = input(
            "Please input the first name: ").strip().title()
        contacts_last_name = input(
            "Please input the last name: ").strip().title()
        contacts_title = input("Please input the title: ").strip().title()
        contacts_organization = input(
            "Please input the organization: ").strip().title()

        if contacts_first_name == '':
            contacts_first_name = 'UNKNOWN'
        if contacts_last_name == '':
            contacts_last_name = 'NULL'
        if contacts_title == '':
            contacts_title = 'NULL'
        if contacts_organization == '':
            contacts_organization = 'NULL'

        # Executing statement.
        cur.execute(f"""INSERT INTO contacts (first_name, last_name, title, organization)
VALUES ('{contacts_first_name}', '{contacts_last_name}', '{contacts_title}', '{contacts_organization}');""")

        # Save table.
        save_changes(conn)

        items_numbers = int(
            input("Please input the number of contact informations to add: "))

        contact_id = find_id(cur, contacts_first_name, contacts_last_name)

        for entries in range(items_numbers):
            items_contact = input(
                "Please input the contact information: ").strip()
            items_type = input(
                "Please input the contact type (Email, Phone, Skype or Instagram): ").strip().title()
            items_category = input(
                "Please input the contact category (Home, Work, Fax): ").strip().title()

            if items_contact == '':
                items_contact = 'UNKNOWN'

            if items_type == '':
                items_type = 'NULL'
            elif items_type == 'Email':
                items_type = 1
            elif items_type == 'Phone':
                items_type = 2
            elif items_type == 'Skype':
                items_type = 3
            elif items_type == 'Instagram':
                items_type = 4

            if items_category == '':
                items_category = 'NULL'
            elif items_category == 'Home':
                items_category = 1
            elif items_category == 'Work':
                items_category = 2
            elif items_category == 'Fax':
                items_category = 3

            # Executing statement.
            cur.execute(f"""INSERT INTO items (contact, contact_id, contact_type_id, contact_category_id)
VALUES ('{items_contact}', '{contact_id}', '{items_type}', '{items_category}');""")

        print(f"{contacts_first_name} {contacts_last_name} added.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Save table.
        save_changes(conn)

        # Close communication with database.
        cur.close()


def delete_data(conn):
    try:
        # Formatting name
        first_name = input(
            "Please enter the first name of the person you with to delete: ").strip().title()
        last_name = input(
            "Please enter the last name of the person you with to delete: ").strip().title()

        # Create a cursor:
        cur = conn.cursor()

        # Get contact id
        contact_id = find_id(cur, first_name, last_name)

        # Executing statement.
        cur.execute(f"""DELETE FROM contacts WHERE id = '{contact_id}'""")
        cur.execute(f"""DELETE FROM items WHERE contact_id = '{contact_id}'""")
        print(f"{first_name} {last_name} deleted.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Save table.
        save_changes(conn)

        # Close communication with database.
        cur.close()


def save_changes(conn):
    """ Commits changes to the database.

    Args:
        conn Object: Database connection
    """
    conn.commit()


def find_id(cur, first_name, last_name):
    # Find id
    cur.execute(
        f"SELECT id FROM contacts WHERE first_name = '{first_name}' AND last_name = '{last_name}';")
    # Check return from executed statement.
    rows = cur.fetchall()

    if rows is None:
        print("Can't find the contact.")
    else:
        for row in rows:
            contact_id = row[0]
            return contact_id


def assessment():
    # Running the program
    conn = connect_db()

    # Messages
    print("Please enter one of the following commands:")
    print("")
    print("LIST - Prints a list of all contacts.")
    print("INSERT - Inserts contact to list.")
    print("DELETE first_name last_name - Deletes contact from list..")
    print("QUIT - Exists the program.")

    while True:
        user_input = input("Command: ").strip().split()

        user_input[0] = user_input[0].upper()

        # Selection menu
        # LIST
        if user_input[0] == "LIST":
            list_data(conn)

        # INSERT
        elif user_input[0] == "INSERT":
            insert_data(conn)

        # DELETE
        elif user_input[0] == "DELETE":
            delete_data(conn)

        # QUIT
        elif user_input[0] == "QUIT":
            print("Commiting all changes.")
            save_changes(conn)
            conn.close()
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


if __name__ == "__main__":
    assessment()

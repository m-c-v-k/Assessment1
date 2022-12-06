#! python3

# Importing necessary libraries
import psycopg2


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


# TODO Commit

# TODO 2. Fetch data
# TODO 2.1 Print to console
# TODO Commit

# TODO 3. Control-loop
# TODO 3.1 Commands
# TODO 3.1.1 LIST
# TODO 3.1.2 INSERT
# TODO 3.1.3 DELETE
# TODO Commit

# TODO 4. Insert function

# TODO 5. Delete function

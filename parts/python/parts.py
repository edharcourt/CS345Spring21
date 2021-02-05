import psycopg2
import getpass

def connect_parts():

    # name of the database connecting to
    DBNAME = "cslabtes_parts_and_suppliers"
    USER = "cslabtes"
    HOST = "ada.hpc.stlawu.edu"
    PASSWORD = "cslabtes"
    PASSWORD_FILE = '.pgpass'

    # Security
    # On every line of code, "what can go wrong?"
    # Real software should never ever crash
    # always fail gracefully

    # PASSWORD = getpass.getpass("Please enter password:")

    try:
        pgpass_file = open(PASSWORD_FILE)
    except OSError:
        print("Cannot open credential file")
        exit(1)

    passwd = pgpass_file.readline()
    if len(passwd) == 0:
        print("Cannot open credential file")
        exit(1)

    # Sanitizing the inputs

    # Create a database connection
    # What can go wrong?
    # 1) host is not up
    # 2) user might not have access to the database
    # 3) password might be wrong
    # 4) username might be wrong
    # 5) dbname could be wrong
    try:
        conn = psycopg2.connect(
            dbname = DBNAME,
            user = USER,
            host = HOST,
            password = passwd
        )
    except psycopg2.Error as e:
        print("Cannot connect {0}".format(e.pgerror))
        exit(1)

    return conn

# M a i n    P r o g r a m
if __name__ == "__main__":




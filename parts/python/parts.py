import psycopg2
import getpass

# TODO refactor this in to a connection class
class PartDBConnection:
    pass

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

    # Watchout, password visible in debugger
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
        print(e)
        exit(1)

    return conn

def print_menu():
    # FIXME make sure user enters valid option
    # FIXME have function return the option
    print("1) Lookup part by name")
    print("2) Lookup part by part number")
    print("Q) Quit")

def get_parts_by_name(conn):

    cmd = "select * from parts where %s = lower(pname);"
    pname = input("Enter part name: ")
    pname = pname.lower().strip()

    # get a cursor to execute the query
    # TODO try-except these calls to catch exceptions
    try:
        cur = conn.cursor()
        cur.execute(cmd, (pname,) )
    except psycopg2.Error as e:
        print(e)
        return

    # cursors are iterable
    # a cursor is like a reference/pointer/location
    # a cursors keeps a reference to a row in the
    # ResultSet (the set of rows from a query).
    for row in cur:
        print(row)

def get_part_by_pno(conn):
    pno = input("Enter part number: ")
    pno = pno.lower().strip()

    cmd = "select * from parts where pno = " + pno

    # 6;insert into parts values (7,'Fudge','Mauve',9999,'Alcatraz')

    try:
        cur = conn.cursor()
        cur.execute(cmd)
    except psycopg2.Error as e:
        print(e)
        return

    if cur.rowcount == 0:
        print("No part found with part number {0}".format(pno))
        return

    print(cur.fetchone())




# M a i n    P r o g r a m
# double underscore names and functions
# dunder
if __name__ == "__main__":
    conn = connect_parts()
    conn.set_session(autocommit=True)

    # Assumption: We have a valid connection
    # Watchout, cannot assume connections stays valid
    # Keep checking the closed attribute on conn

    while True:
        print_menu()
        option = input("Enter menu option:")

        if option == '1':
            get_parts_by_name(conn)
        elif option == '2':
            get_part_by_pno(conn)
        elif option in ['Q','q']:
            exit()

"""
What options should we provide the user.
1) Put yourself in the shoea of the customer
2) analyze the domain (parts)
3) interview potential users and customers 
"""

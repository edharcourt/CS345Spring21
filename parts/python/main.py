import psycopg2

# http://initd.org/psycopg/docs/index.html
# http://initd.org/psycopg/docs/usage.html
# DB API 2.0 https://www.python.org/dev/peps/pep-0249/
# http://initd.org/psycopg/docs/

'''
select * 
   from student where lower(name) like '%tomason%';update student set tot_cred = tot_cred * 10 
   where name = 'Hawthorne';

   Tomason; update student set tot_cred = tot_cred * 10 where Name = 'Hawthorne';
'''

# could use getpass and method getpass.getpass(prompt)

# hopefully this password file is sitting somewhere secure
# what could go wrong?
try:
    pgpass_file = open('.pgpass')
except OSError:
    print("Authorization failed. Could not open credential file.")
    exit(1)

# named parameters as opposed to positional
try:
    conn = psycopg2.connect(
        dbname="cslabtes_parts_and_suppliers",
        user="cslabtes",
        host="ada.hpc.stlawu.edu",
        password=pgpass_file.readline().strip())  # <-- read the password right here quickly
except psycopg2.Error:
    print("Cannot connect to the database server. Exiting")
    exit()

pgpass_file.close()  # <-- close the password file
pgpass_file = None  # <-- and get rid of any reference to it


# update student set tot_cred = tot_cred * 10 where lower(Name) like '%hawthorne%';--
#  update student set tot_cred = tot_cred * 10 where lower(name) like '%hawthorne%';

def print_menu():
    print("1) Lookup part by name")
    print("2) Lookup part by part number")
    print("Q)uit")


done = False
while not done:
    print_menu()
    option = input("Enter menu option: ")

    if option == '1':
        name = input("Enter name: ")
        # cmd = "SELECT * FROM student where lower(name) like '%" + name.lower() + '%\'' + ';'
        #cmd = "SELECT * FROM parts where lower(pname) like %s"
        cmd = "SELECT * FROM parts where lower(pname) like %s"

        cur = conn.cursor()  # a cursor allows you to execute queries.
        cur.execute(cmd, (name.strip().lower(),))
        conn.commit()  # <- only necessary if modifying database
        for row in cur:
            print(row)

    elif option == '2':
        id = input("Enter course ID: ")
        cmd = 'SELECT * FROM parts where pno = ' + id + ';'

    elif option in ['q', 'Q']:
        done = True

print('Bye.')

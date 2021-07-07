import pymysql

# function to create a connection to the database
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = pymysql.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection(
    "host_name,", "user_name", "user_password", "db_name")

#create table code    

# sql = '''
# create table contacts (
# id int not null auto_increment,
# contactDetails text,
# createtionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
# primary key (id)
# )
# '''
# cursor.execute(sql)

# This function will add contact to database
def addContact():
     contactInfo = input("Contact Details: ")
     sql = '''insert into contacts(contactDetails) values('%s')''' % (contactInfo)
     cursor = connection.cursor()
     cursor.execute(sql)
     connection.commit()

# This function will remove contact from database
def removeContact():
     id = input("Contact ID: ")
     sql = '''delete from  contacts WHERE id = ('%s')''' % (id)
     cursor = connection.cursor()
     cursor.execute(sql)
     connection.commit()

# This function will rupdate exsiting contact  
def updateContact():
     id = input("Contact ID: ")
     updateValue = input("Update Contact Value: ")
     sql = '''UPDATE contacts set contactDetails = ('%s') WHERE id = ('%s')''' % (updateValue,id)
     cursor = connection.cursor()
     cursor.execute(sql)
     connection.commit()

# This function will show all data from contacts table
def showAll():
    sql = '''select * from contacts'''
    cursor = connection.cursor()
    cursor.execute(sql)
    allData = cursor.fetchall()
    print(allData)

# This function will show all data from contacts table by alpahbetical order
def showAllByAlphaBetical():
    sql = '''select * from contacts Order By contactDetails '''
    cursor = connection.cursor()
    cursor.execute(sql)
    allData = cursor.fetchall()
    print(allData)

# This function will show all data from contacts table by creation time  order
def showAllByCreationDate():
    sql = '''select * from contacts Order By createtionDate '''
    cursor = connection.cursor()
    cursor.execute(sql)
    allData = cursor.fetchall()
    print(allData)
     
# Console Menu
def menu():
    while(1):
        print('a - Add Contact')
        print('d - Remove Contact')
        print('u - Update Contact Details')
        print('b - Output All Contact by alpahbetical order')
        print('c - Output All Contact by Creation Date')
        print('o - Output All Contact')
        print('q - Close the Program')
        op = input("Choose An Option: ")

        if(op == "a"):
            addContact()
        elif(op == "u"):
            updateContact()
        elif(op == "d"):
            removeContact()
        elif(op=="b"):
            showAllByAlphaBetical()
        elif(op=="c"):
            showAllByCreationDate()
        elif(op=="o"):
            showAll()
        elif(op == "q"):
            return 0    
            

menu()    

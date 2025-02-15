
#-----------------------------showing the main menu-----------------------------------
def clear():
  for _ in range(1):
     print
def main_menu():
    while True:
      clear()
      print(' L I B R A R Y    M E N U')
      print("\n1.  Add Books")
      print('\n2.  Add Member')
      print('\n3.  Modify Member Information')
      print('\n4.  Search Menu')
      print('\n5.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_book()
      if choice == 2:
        add_member()
      if choice == 3:
        modify_member()
      if choice == 4:
        search_menu()
      if choice == 5:
        break

if __name__ == "__main__":
    main_menu()

#-----------------------------------adding books-------------------------------------------
def add_book():
  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='12345')
  cursor = conn.cursor()

  title = input('Enter Book Title :')
  author = input('Enter Book Author : ')
  publisher = input('Enter Book Publisher : ')
  pages = input('Enter Book Pages : ')
  price = input('Enter Book Price : ')
  edition = input('Enter Book Edition : ')
  copies  = int(input('Enter copies : '))
  sql = 'insert into book(title,author,price,pages,publisher,edition,status) values ( "' + title +'","'+author+'",'+price+','+pages+',"'+publisher+'","'+edition+'",
"available");'

    for _ in range(0,copies):
    cursor.execute(sql)
  conn.close()
  print('\n\nNew Book added successfully')
  wait = input('\n\n\n Press any key to continue....')

#-----------------------------------adding members--------------------------------------
def add_member():
  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='12345')
  cursor = conn.cursor()

  name = input('Enter Member Name :')
  clas = input('Enter Member Class & Section : ')
  address = input('Enter Member Address : ')
  phone = input('Enter Member Phone  : ')
  email = input('Enter Member Email  : ')
  
 
  sql = 'insert into member(name,class,address,phone,email) values ( "' + name + '","' +clas+'","'+address+'","'+phone + '","'+email+'");'
  cursor.execute(sql)
  conn.close()
  print('\n\nNew Member added successfully')
  wait = input('\n\n\n Press any key to continue....')



#-------------------------modifying members information----------------------------

def modify_member():
    conn = mysql.connector.connect(host='localhost',database='library', user='root', password='12345')
    cursor = conn.cursor()
    clear()
    print('Modify Memeber Information Screen ')
    print('-'*120)
    print('\n1. Name')
    print('\n2. Class')
    print('\n3. address')
    print('\n4. Phone')
    print('\n5. Emaile')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field =''
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'class'
    if choice ==3:
        field ='address'
    if choice == 4:
        field = 'phone'
    if choice == 5:
        field = 'email'
    mem_id =input('Enter name :')
    value = input('Enter new value :')
    sql = 'update member set '+ field +' = "'+value+'" where name = '+mem_id+';'
    cursor.execute(sql)
    print('Member details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

#------------------------------------searching books--------------------------------------

def search_book(field):
    conn = mysql.connector.connect(host='localhost',database='library', user='root', password='12345')
    cursor = conn.cursor()

    clear()
    print('\n BOOK SEARCH SCREEN ')
    print('-'*120)
    msg ='Enter '+ field +' Value :'
    title = input(msg)
    sql ='select * from book where '+ field + ' like "%'+ title+'%"'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for :',field,' :' ,title)
    print('-'*120)
    for record in records:
      print(record)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

#--------------------------------------search menu----------------------------------------

def search_menu():
    while True:
      clear()
      print(' S E A R C H   M E N U ')
      print("\n1.  Book Title")
      print('\n2.  Book Author')
      print('\n3.  Publisher')
      print('\n4.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field =''
      if choice == 1:
        field='title'
      if choice == 2:
        field = 'author'
      if choice == 3:
        field = 'publisher'
      if choice == 4:
        break
      search_book(field)

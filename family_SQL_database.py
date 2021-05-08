'''
This program stores the following information about all my family members:
- Name
- Email
- Birthday
- Hobbies
- Places they have traveled. 

I made this database to be able to remember birthdays, compare interests, and 
brag about places we have all been.
'''

# Import the built in SQL lite database.
import sqlite3
db = "family.db"

# Create a connection. Create a cursor object. 
conn = sqlite3.connect(db)
cursor = conn.cursor()

'''
Table 1:
title: Profile.
Columns: name, email, birth date.
'''

profile = '''CREATE TABLE IF NOT EXISTS profile(name TEXT PRIMARY KEY, email TEXT, birthday TEXT)'''
cursor.execute(profile)

'''
Table 2:
Title: Hobbies.
Columns: name, hobbies.
'''

hobbies = '''CREATE TABLE IF NOT EXISTS hobbies(name TEXT, hobby TEXT)'''
cursor.execute(hobbies)

'''
Table 3:
Title: Travel.
Columns: name, places visited.
'''

travel = '''CREATE TABLE IF NOT EXISTS travel(name TEXT, location TEXT)'''
cursor.execute(travel)

# Create menu to add, update, and remove from the database. 
choice = 0
while choice != '9':
    print("1. Display.")
    print("2. Create profile")
    print("3. Delete profile")
    print("4. Change email. ")
    print("5. Change birthdate. ")
    print("6. Add hobbies. ")
    print("7. Delete hobbies")
    print("8. Add travel locataions. ")
    print("9. Quit")
    print()
    choice = input()

    # Display.
    if choice == '1':
        # Select everything from profile and display it.
        cursor.execute('''SELECT * FROM profile''')
        print('name' + ' ' * 25, 'email' + ' ' * 20, 'Date of birth')
        for profile in cursor.fetchall():
            print(f'{profile[0]}', ' ' * 5, f'{profile[1]}', ' ' * 5, f'{profile[2]}')
                
        print()
        
        # Select everyting from hobbies and display it.
        cursor.execute('''SELECT * FROM hobbies''')
        print('Hobbies')
        for hobbies in cursor.fetchall():
            print(hobbies[0], hobbies[1])

        print()

        # Select everything from travel and display it.
        cursor.execute('''SELECT * FROM travel''')
        print('Places I have been.')
        for travel in cursor.fetchall():
            print(travel[0], travel[1])

    # Create profile.  
    elif choice == '2':
        name = input('Enter you name. First, Last ')
        email = input('Enter your email address. ')
        birthday = input("Enter your date of birth. (mm/dd/yyyy) ")

        values = (name, email, birthday)

        cursor.execute('''INSERT INTO profile VALUES(?,?,?)''', values)
        conn.commit()

    # Delete profile. 
    elif choice == '3':
        name = input('Enter the name to delete a profile ')
        values = (name, )
        cursor.execute('''DELETE FROM profile WHERE name = ?''', values)
        cursor.execute('''DELETE FROM hobbies WHERE name = ?''', values)
        cursor.execute('''DELETE FROM travel WHERE name = ?''', values)

        conn.commit()    

    # Change email.
    elif choice == '4':
        name = input('Enter a name to change email for. ')
        email = input('Enter the new email. ')
        values = (email, name)

        cursor.execute('''UPDATE profile SET email = ? WHERE name = ?''', values)
        conn.commit()
    
    # Change birthday.
    elif choice == '5':
        name = input('Enter a name to change birthday for. ')
        birthday = input('Enter the birthday. ')
        values = (birthday, name)

        cursor.execute('''UPDATE profile SET birthday = ? WHERE name = ?''', values)
        conn.commit()

    # Add hobbies.
    elif choice == '6':
        name = input('Enter your name. ')
        condition = ' '
        while condition.upper() != 'N':
            hobby = input("Enter a hobby. ")
        
            values = (name, hobby)
            cursor.execute('''INSERT INTO hobbies VALUES(?,?)''', values)
            conn.commit()

            condition = input('Enter another hobby? Y/N? ')

    # update hobbies.
    elif choice == '7':
        name = input('Enter your name. ')
        values = (name, )
        cursor.execute('''DELETE FROM hobbies WHERE name = ?''', values)

        conn.commit()
    
    # Add travel locations.
    elif choice == '8':
        name = input('Enter your name. ')
        condition = ' '
        while condition.upper() != 'N':
            travel_places = input('Enter cool places you have traveled to. Type q to quit. ')

            values = (name, travel_places)
            cursor.execute('''INSERT INTO travel VALUES(?,?)''', values)
            conn.commit()

            condition = input('Enter another location? Y/N? ')
    

print("Thanks for using the family database!")

# Close the connection.
conn.close()

'''
cursor.execute("SELECT courses.name, grades.grade FROM grades INNER JOIN courses ON grades.course_id == courses.id WHERE grades.student_id == ?", values)
        # Display results
        for record in cursor.fetchall():
            print("{} - {}".format(record[0], record[1]))
'''
# Menu 
from hashlib import new
import turtle
import pyfiglet
loop = True
while(loop):
   studentMenu = pyfiglet.figlet_format('Student Menu')
   print(studentMenu)
   print("----------------------------------------------------------------")
   print('Options:        ')
   print("     ", "1. ✅ Add Student")
   print("     ", "2. 👀 Show Student List")
   print("     ", "3. 🔬 Find Students")
   print("     ", "4. ❌ Delete List of student")
   print("     ", "5. ✏️ Draw VietNam Flag")
   print("     ", "6. 👋 EXIT")
   print("-----------------------------------------------------------------")

   # Select options 
   options = int(input('Select your options:  '))

   # Options 1 
   if options == 1: 
      studentAdd = pyfiglet.figlet_format('Add Student')
      print(studentAdd)
      nameList = []
      dobList = []
      addressList = []
      studentData = []
      
      for i in range(1):
         nameInput = str(input('Name of student: '))
         dobInput = str(input('Date of birth: '))
         addressInput = str(input("Input your home address: "))
         
         nameList.append(nameInput)
         dobList.append(dobInput)
         addressList.append(addressInput)
         
         
         name = nameList[i]
         dob = dobList[i]
         address = addressList[i]
         studentData = "Student's name: "+ name + "\n" + "Date of birth: " + dob +"\n" "Students Address: " + address
         print("------------------------------")
         print("STUDENTS ADDED SUCCESSFULLY ✅")
         print("\n")

   # Options 2 
   if options == 2: 
      print("\n")
      studentList = pyfiglet.figlet_format('Student Details')
      print(studentList)
      print(studentData)
      print("\n")
      print("-----------------------------------------------------------------")

   # Options 3 
   if options == 3: 
      findStudents = pyfiglet.figlet_format('Find Students')
      print(findStudents)
      searchInput = str(input('Who do you want to find? '))
      if searchInput in studentData:
         print("\n")
         print(studentData)
         print("-------------------------------------")
         print("\n")
      else: 
         continue
   
   # Options 4 
   if options == 4:
      userConfirm = input("Are you sure Y/N ?")
      if userConfirm == 'Y':
         
         print("List Deleted")
    
   # Options 5 
   if options == 5: 
      flag = turtle.Screen()            
      flag.bgcolor("red")
      screen_width = 850;
      screen_height = 450;
      star_length = 200; 
      flag.setup(width = screen_width, height = screen_height)
      flag.title("Vietnam Flag")
      mainFlag = turtle.Turtle()
      mainFlag.color("red")                
      mainFlag.setx((screen_width - star_length)/2 - screen_width/2)
      mainFlag.sety(star_length/4)
      mainFlag.color("yellow")
      mainFlag.shape("blank")              
      mainFlag.pensize(90)                 
      
      # Draw the flag
      for counter in range(5):
         mainFlag.forward(star_length)                 
         mainFlag.right(144)
      
      # Click the any where on the screen to exit
      flag.exitonclick()
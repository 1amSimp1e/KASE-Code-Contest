import os
import time
import pyfiglet
vongLap = True
studentList = []
# THIẾT KẾ MẪU CHO BÀI THI I CAN CODE TEENS LẬP TRÌNH PYTHON
while(True):
    ascii_banner = pyfiglet.figlet_format("STUDENT")
    print(ascii_banner)
    print("----------------------------------------------------------")
    print("              1.  THÊM 1 HỌC SINH                         ")
    print("              2.  SHOW DANH SÁCH HỌC SINH                 ")
    print("              3.  TÌM KIẾM MỘT HỌC SINH                   ")
    print("              4.  XÓA DANH SÁCH HỌC SINH                  ")
    print("              5.  VẼ CỜ VIỆT NAM                          ")    
    print("                                             6.  THOÁT    ")
    print("----------------------------------------------------------")
    choice = int(input("Select your options : "))
    os.system("cls")

    # CHỨC NĂNG 1 : THÊM MỚI MỘT HỌC SINH TỪ BÀN PHÍM - LƯU TRỮ QUA LIST
    if(choice == 1):
        ascii_banner = pyfiglet.figlet_format("THEM HOC SINH")
        print(ascii_banner)
        ten = input("Nhập vào tên học sinh : ")
        namSinh = int(input("Nhập vào năm sinh : "))
        diaChi = input("Nhập vào địa chỉ : ")
        print("----------------------------------------------------------")
        print("Học sinh đã được tạo !!!!!!!")
        infor = []
        infor.append(ten)
        infor.append(namSinh)
        infor.append(diaChi)
        studentList.append(infor)

    # CHỨC NĂNG 2 : TRÌNH BÀY TẤT CẢ CÁC HỌC SINH CÓ TRONG DANH SÁCH
    elif(choice == 2):
        ascii_banner = pyfiglet.figlet_format("DANH SACH")
        print(ascii_banner)
        for i in studentList:
            print("Tên HS : "+ i[0] + " - Năm sinh : " +  str(i[1]) + " - Địa chỉ : " + str(i[2]))
        print("----------------------------------------------------------")
        print("")
    
    # CHỨC NĂNG 3 : TÌM KIẾM MỘT HỌC VIÊN THEO TÊN HỌC VIÊN
    elif(choice == 3):
        ascii_banner = pyfiglet.figlet_format("TIM HOC SINH")
        print(ascii_banner)
        name = input("Tên học sinh cần tìm : ")
        for i in studentList:
            if(i[0] == name):
                print("Tên HS : "+ i[0] + " - Năm sinh : " +  str(i[1]) + " - Địa chỉ : " + str(i[2]))
            else:
                pass
    
    # CHỨC NĂNG 4 : XÓA DANH SÁCH HỌC SINH
    elif(choice == 4):
        ascii_banner = pyfiglet.figlet_format("XOA DANH SACH")
        print(ascii_banner)
        xoa = input("Xóa hay không (Y/N): ")
        if(xoa == "Y"):
            studentList.clear()
        else:
            pass
    
    # CHỨC NĂNG 5 : VẼ LÁ CỜ VIỆT NAM BẰNG PYTHON TURTLE
    elif(choice == 5):
        import turtle
        p=turtle.Turtle()
        p.getscreen().bgcolor('red')
        p.color('yellow')
        p.penup()
        p.goto(-100,100)
        p.pendown()
        p.begin_fill()
        for i in range(5):
            p.forward(200)
            p.left(216)
        p.end_fill()
        p.penup()
        p.goto(-200,200)
        p.pendown()
        p.forward(400)
        p.right(90)
        p.forward(250)
        p.right(90)
        p.forward(400)
        p.right(90)
        p.forward(250)
        turtle.exitonclick()
    
    # CHỨC NĂNG 6 : THOÁT KHỎI CHƯƠNG TRÌNH
    elif(choice == 6):
        ascii_banner = pyfiglet.figlet_format("Goodbye!!")
        print(ascii_banner)
        time.sleep(3)
        os.system("cls")
        exit()
    else:
        print("Error, Please choose another option")

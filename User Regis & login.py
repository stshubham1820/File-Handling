import os
def main():
    def valid (Name):
        List = os.listdir()
        for i in List :
            if i == Name :
                return True
                break
        else :
            return False
    def Register():
        Name = input("Enter Name : ")
        if valid(Name) == False :
            user = input("Enter User Name : ")
            passw = input("Enter Password : ")
            file = open(Name,'w')
            file.write('User Name : '+user+'\n')
            file.write("Password : "+passw)
            file.close()
            if valid(Name) == True :
                print("Sucessfully Registered : ")
            else :
                print("Unsucessful : ")
        else :
            print("User is Already There Please Login")
            Login()
    def add(Name):
        file= open(Name,'a')
        data = input("Enter what you want to add : ")
        file.write("\n"+data)
        file.close()
        optional(Name)
    def optional(Name):
        opt = input("Would you like to add something (Yes / No) : ").lower()
        if opt == "yes":
            add(Name)
        else :
            return 
    def Login():
        Name = input("Enter Name : ") 
        if valid(Name) == True :
            Passw = input("Enter Password : ")
            file = open(Name,'r')
            Nlist = file.read()
            for i in Nlist :
                if i in "Password : "+Passw :
                    print("Login Sucessful")
                    option = input("Would you like to see Your Data (Yes/No): ").lower()
                    if option == "yes":
                        file = open(Name,'r')
                        print(file.read())
                        file.close()
                        optional(Name)
                        break
                    else :
                        optional(Name)
                        break        
            else :
                print("Wrong Password")
            file.close()
        else :
            print("User is not Here please Register")
            Register()
    choice = input("Choose Register / Login : ").lower()
    print(choice)
    if choice == "register" :
        Register()
    elif choice == "login":
        Login()
    else :
        print("Wrong Input")
main()
with open("c:\\Users\\Yanek\\Dropbox\\Programming\\Python\\Codes\\Python-Tasks\\Lessons\\DuringLessons\\PasswordFinder\\password.txt","rt") as file:
    p = file.readline()
for i in range(1000,10000):    
    if str(i)==p:
        print(f"Password is {p}")

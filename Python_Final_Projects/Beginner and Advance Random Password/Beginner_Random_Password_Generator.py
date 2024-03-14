import random
import string

def creat_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter  password length: "))
    if length <= 0:
        print("Password length musst > 0.")
        return

    password = creat_password(length)
    print("Create Password:", password)

if __name__ == "__main__":
    main()

import hashlib
import sys

sys.stdout = open("hash.txt", "a")

put = input("Password : ")
password = ""
result = hashlib.sha256(put.encode())
password += result.hexdigest()
result = hashlib.sha256(password.encode())

print("Start Password : ", put)

num = int(input("Loop Count : "))

for i in range(1, num + 1):
    result = hashlib.sha256(password.encode())

    print("\nPassword (%d) : " %i, password)
    print("SHA256 : ", result.hexdigest())

    password = ""
    password += result.hexdigest()
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

while b != 0:
    a, b = b, a % b  

print("FPB dari kedua bilangan adalah:", a)

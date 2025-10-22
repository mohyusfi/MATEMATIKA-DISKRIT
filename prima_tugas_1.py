# MENENTUKAN BILANGAN PRIMA

n = int(input("Masukkan bilangan: "))

prima = True

if n <= 1:
    prima = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prima = False
            break   

if prima:
    print(n, "adalah bilangan prima.")
else:
    print(n, "bukan bilangan prima.")

# -*- coding: utf-8 -*-

broj1 = int(input("Unesite prvi četvorocifreni broj: "))
broj2 = int(input("Unesite drugi četvorocifreni broj: "))

zbir = 0

while (broj2 > 0):
    n = broj2 % 10
    zbir = zbir + n
    broj2 = broj2 // 10

print("\n Suma cifara drugog četvorocifrenog broja je : %d" % zbir)

cifre = []

while broj1> 0:
    cifre.append(broj1%10)
    broj1 //= 10

s = 0
p = 0
i = 0
for cifra in reversed(cifre):
    if i%2 == 0:
        s += cifra
    else:
        p += cifra
    i += 1

print '\n Razlika između sume na parne i neparne pozicije prvog četvorocifrenog broja je: ', s-p
# -*- coding: utf-8 -*-

x = int(input('Unesite broj: '))
cifre = []

while x > 0:
    cifre.append(x%10)
    x //= 10

p = 0
n = 0
i = 0
for cifra in reversed(cifre):
    if i%2 == 0:
        p += cifra
    else:
        n += cifra
    i += 1

print 'Suma brojeva na parnim mestima je: ', p
print 'Suma brojeva na neparnim mestima je: ', n
print 'Razlika između sume je: ', p-n
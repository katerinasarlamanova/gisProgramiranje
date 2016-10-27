# -*- coding: utf-8 -*-

x = int(input('Unesite broj: '))
cifre = []

while x > 0:
    cifre.append(x%10)
    x //= 10

s = 0
p = 0
i = 0
for cifra in reversed(cifre):
    if i%2 == 0:
        s += cifra
    else:
        p += cifra
    i += 1

print 'Suma brojeva na parnim mestima je: ', s
print 'Suma brojeva na parnim mestima je: ', p
print 'Razlika između sume je: ', s-p
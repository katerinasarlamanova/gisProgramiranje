# -*- coding: utf-8 -*-

a = "82:39:57"
aD = 82.0 + 39.0/60 + 57.0/3600 #ugao u decimale

b = "56:23:54"
bD = 56.0 + 23.0/60 + 54.0/3600 #ugao u decimale

rezD = aD - bD

print(a) + (" u stepenima, ") + str(aD) + (" u decimalima")
print(b) + (" u stepenima, ") + str(bD) + (" u decimalima")

print('\n')
print(rezD)

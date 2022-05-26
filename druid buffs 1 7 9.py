#(4000 * (12 - T))% DD1
#(12 * 1.8 ** (12 - T))% DD7
#(1.5 * x ** 0.9)% DD9
#(0.1 * x ** 0.45 * (12 - T) ** 2)% R545
#(150 * (12 - T) ** 2.15)% W3150
#(((buff / 100 + 1) ** (0.1 ** asc) - 1) * 100) ASCENSION PENALTY
asc = 1

T = 9
buff = (150 * (12 - T) ** 2.15)
print ('buff is '+str(int(buff))+'%')
print('with Ascension penalty it is '+str(int(((buff / 100 + 1) ** (0.1 ** asc) - 1) * 100))+'%')


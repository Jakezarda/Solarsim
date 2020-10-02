import numpy as np
import xlrd


databook = xlrd.open_workbook('planetdata2.xlsx')
datasheet = databook.sheet_by_name('Sheet1')

a = datasheet.row_values(15)
p = datasheet.row_values(13)
r = datasheet.row_values(16)

v = np.zeros(8)

for i in range(0,8):
    v[i] = ((2*np.pi*a[i])/p[i])*np.sqrt(2*(a[i]/r[i])-1)
    
f = open("initialplanetdata.dat", "w")
for i in range (0,8):
   f.write(str(a[i]) + " " + str(p[i]) + " " + str(r[i]) + " " + str(v[i]) + " " + "\n")
f.close()

print(r)

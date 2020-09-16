Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'Nguyen Cong Dao'

print ('-----------------')
print (name)

hocVien1 = {'Ten': 'Hoc vien 1', 'Tuoi': '30', 'Don_vi': 'Viettel' }
hocVien2 = {'Ten': 'Hoc vien 2', 'Tuoi': '31', 'Don_vi': 'Viettel' }
hocVien3 = {'Ten': 'Hoc vien 3', 'Tuoi': '32', 'Don_vi': 'Viettel' }
hocVien4 = {'Ten': 'Hoc vien 4', 'Tuoi': '33', 'Don_vi': 'Viettel' }
hocVien5 = {'Ten': 'Hoc vien 5', 'Tuoi': '34', 'Don_vi': 'Viettel' }
danhSach_hocVien = [hocVien1,hocVien2,hocVien3,hocVien4,hocVien5]

print ('-----------------')
for i in danhSach_hocVien:
    print("Ten:" + i['Ten'])
    print("Tuoi:" + str(i['Tuoi']))
    print("Don vi:" + i['Don_vi'])
    print ('-----------------')
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 1
1
>>> 2
2
>>> 3
3
>>> 
>>> name = 'Nguyen Cong Dao'
>>> print ('-----------------')
-----------------
>>> print (name)
Nguyen Cong Dao
>>> hocVien1 = {'Ten': 'Hoc vien 1', 'Tuoi': '30', 'Don_vi': 'Viettel' }
>>> hocVien2 = {'Ten': 'Hoc vien 2', 'Tuoi': '31', 'Don_vi': 'Viettel' }
>>> hocVien3 = {'Ten': 'Hoc vien 3', 'Tuoi': '32', 'Don_vi': 'Viettel' }
>>> hocVien4 = {'Ten': 'Hoc vien 4', 'Tuoi': '33', 'Don_vi': 'Viettel' }
>>> hocVien5 = {'Ten': 'Hoc vien 5', 'Tuoi': '34', 'Don_vi': 'Viettel' }
>>> danhSach_hocVien = [hocVien1,hocVien2,hocVien3,hocVien4,hocVien5]
>>> print ('-----------------')
-----------------
>>> for i in danhSach_hocVien:
	print("Ten:" + i['Ten'])
	print("Tuoi:" + str(i['Tuoi']))
	print("Don vi:" + i['Don_vi'])
	print ('-----------------')

	
Ten:Hoc vien 1
Tuoi:30
Don vi:Viettel
-----------------
Ten:Hoc vien 2
Tuoi:31
Don vi:Viettel
-----------------
Ten:Hoc vien 3
Tuoi:32
Don vi:Viettel
-----------------
Ten:Hoc vien 4
Tuoi:33
Don vi:Viettel
-----------------
Ten:Hoc vien 5
Tuoi:34
Don vi:Viettel
-----------------
>>> 
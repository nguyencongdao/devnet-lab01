# devnet-lab01
#Thuc hanh Python

name = 'Nguyen Cong Dao'

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
    
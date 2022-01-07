alternatif = ["1. HP Pavilion Gaming 15 i5 10300", 
              "2. ASUS TUF FX505DYRX560 4GB RYZEN 5 3550",
              "3. Lenovo Gaming 3", 
              "4. MSI GF63 THIN 10SCSR 1460ID - i5-10200H", 
              "5. ASUS FX505DT R5-3550 GTX1650"]

kriteria = ["Harga", 
            "Spesifikasi",
            "Ketangguhan Laptop",
            "Merek",
            "Service Center"]

costbenefit = ["cost", "benefit", "benefit", "benefit", "benefit"]

bobot = [0.25, 0.25, 0.25, 0.15, 0.10]

alternatifkriteria = [
    [11000000, 80, 75, 80, 70],
    [12000000, 80, 85, 85, 90],
    [12500000, 75, 70, 75, 70],
    [13000000, 80, 70, 70, 60],
    [10000000, 80, 90 ,85, 90]
]
print("alternatif           :")
print (str(alternatif))
print(" ")

print("kriteria             :")
print (str(kriteria))
print(" ")

print("costbenefit          :")
print (str(costbenefit))
print(" ")

print("bobot          :")
print (str(bobot))
print(" ")

print("alternatif kriteria  :")
print (str(alternatifkriteria))
print(" ")

pembagi = []
for i in range(len(kriteria)):
    pembagi.append(0)
    for j in range (len(kriteria)):
        if costbenefit[i] == "cost":
            if j == 0:
                pembagi[i] == alternatifkriteria[j][i]
            else:
                if pembagi[i] > alternatifkriteria[j][i]:
                    pembagi[i] = alternatifkriteria[j][i]
        else:   #if costbenefit[i] == 'benefit':
            if j == 0:
                pembagi[i] = alternatifkriteria[j][i]
            else:
                if pembagi[i] < alternatifkriteria[j][i]:
                    pembagi[i] = alternatifkriteria[j][i]
print("nilai alternatif yang digunakan     :")
print(str(pembagi))
print(" ")

normalisasi = []
for i in range(len(alternatif)):
    normalisasi.append([])
    for j in range(len(kriteria)):
        normalisasi[i].append(0)
        if costbenefit[j] == "cost":
            normalisasi[i][j] = pembagi[j] / alternatifkriteria[i][j]
        else: #if costbenefit[j] == 'benefit':
            normalisasi[i][j] = alternatifkriteria[i][j] / pembagi[j]

print("Normalisasi      :")
print(str(normalisasi))
print(" ")

hasil = [] 
for i in range(len(alternatif)):
    hasil.append(0)
    for j in range(len(kriteria)):
        hasil[i] = hasil [i] + (normalisasi[i][j] * bobot[j])
print("hasil        :")
print(str(hasil))
print(" ")

alternatifrangking = []
hasilrangking = []

for i in range(len(alternatif)):
    hasilrangking.append(hasil[i])
    alternatifrangking.append(alternatif[i])

for i in range(len(alternatif)):
    for j in range(len(alternatif)):
        if j > i:
            if hasilrangking[j] > hasilrangking[i]:
                tmphasil = hasilrangking[i]
                tmpalternatif = alternatifrangking[i]
                hasilrangking[i] = hasilrangking[j]
                alternatifrangking[i] = alternatifrangking[j]
                hasilrangking[j] = tmphasil
                alternatifrangking[j] = tmpalternatif


print("Rangking Alternatif:")
print(str(alternatifrangking))
print(" ")

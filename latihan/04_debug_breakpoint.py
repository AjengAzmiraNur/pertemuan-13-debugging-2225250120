def hitung_total(nilai):
    total = 0

    for angka in nilai:
        total += angka

    return total


data = [10, 20, 30]
hasil = hitung_total(data)

print("Data:", data)
print("Total:", hasil)
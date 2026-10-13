from bmi_calculator import hitung_bmi, kategori_bmi, validasi_input, tampilkan_hasil

print("=" * 55)
print("PENGECEKAN FUNGSI BMI CALCULATOR")
print("=" * 55)

print("\n1. CEK FUNGSI hitung_bmi()")
print("Input  : berat = 70 kg, tinggi = 1.75 m")
print("Output :", hitung_bmi(70, 1.75))

print("\n2. CEK FUNGSI kategori_bmi()")
print("Input  : nilai_bmi = 22.0")
print("Output :", kategori_bmi(22.0))

print("\n3. CEK FUNGSI validasi_input() - Input Valid")
print("Input  : berat = 70 kg, tinggi = 1.75 m")
print("Output :", validasi_input(70, 1.75))

print("\n4. CEK FUNGSI validasi_input() - Berat Negatif")
print("Input  : berat = -5 kg, tinggi = 1.75 m")
print("Output :", validasi_input(-5, 1.75))

print("\n5. CEK FUNGSI tampilkan_hasil() - Input Valid")
print("Input  : berat = 70 kg, tinggi = 1.75 m")
print("Output :", tampilkan_hasil(70, 1.75))

print("\n6. CEK FUNGSI tampilkan_hasil() - Input Invalid")
print("Input  : berat = -5 kg, tinggi = 1.75 m")
print("Output :", tampilkan_hasil(-5, 1.75))

print("\n" + "=" * 55)
print("PENGECEKAN MANUAL SELESAI")
print("=" * 55)
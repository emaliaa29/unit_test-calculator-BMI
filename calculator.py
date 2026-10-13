"""
BMI Calculator
Program untuk menghitung Body Mass Index (BMI).

Input:
- Berat badan dalam kilogram (kg)
- Tinggi badan dalam sentimeter (cm)

Output:
- Nilai BMI
- Kategori BMI
- Pesan hasil
"""


def hitung_bmi(berat, tinggi):
    """
    Menghitung nilai BMI.

    Parameter:
    berat  : berat badan dalam kilogram
    tinggi : tinggi badan dalam meter

    Return:
    Nilai BMI yang dibulatkan menjadi 2 angka desimal.
    """
    bmi = berat / (tinggi ** 2)
    return round(bmi, 2)


def kategori_bmi(nilai_bmi):
    """
    Menentukan kategori berdasarkan nilai BMI.

    Return:
    Underweight, Normal, Overweight, atau Obese.
    """
    if nilai_bmi < 18.5:
        return "Underweight"
    elif nilai_bmi <= 24.9:
        return "Normal"
    elif nilai_bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def validasi_input(berat, tinggi):
    """
    Memastikan berat dan tinggi adalah angka positif.

    Parameter:
    berat  : berat badan dalam kilogram
    tinggi : tinggi badan dalam meter

    Return:
    True jika input valid, False jika input tidak valid.
    """
    if not isinstance(berat, (int, float)):
        return False

    if not isinstance(tinggi, (int, float)):
        return False

    if berat <= 0 or tinggi <= 0:
        return False

    return True


def tampilkan_hasil(berat, tinggi):
    """
    Mengolah input berat dan tinggi, kemudian mengembalikan
    hasil BMI, kategori, serta pesan yang sesuai.

    Parameter:
    berat  : berat badan dalam kilogram
    tinggi : tinggi badan dalam meter

    Return:
    Dictionary hasil pengolahan.
    """
    if not validasi_input(berat, tinggi):
        return {
            "status": "error",
            "pesan": "Input tidak valid! Berat dan tinggi harus berupa angka positif."
        }

    bmi = hitung_bmi(berat, tinggi)
    kategori = kategori_bmi(bmi)

    if kategori == "Underweight":
        pesan = "Anda kekurangan berat badan. Pertimbangkan untuk konsultasi gizi."
    elif kategori == "Normal":
        pesan = "Berat badan Anda ideal. Pertahankan pola hidup sehat."
    elif kategori == "Overweight":
        pesan = "Anda kelebihan berat badan. Disarankan untuk lebih aktif berolahraga."
    else:
        pesan = "Anda mengalami obesitas. Disarankan konsultasi dengan dokter."

    return {
        "status": "success",
        "berat": berat,
        "tinggi": tinggi,
        "bmi": bmi,
        "kategori": kategori,
        "pesan": pesan
    }


def main():
    """
    Fungsi utama untuk menerima input pengguna dari terminal.
    """
    print("=" * 55)
    print("BMI CALCULATOR - Kalkulator Body Mass Index")
    print("=" * 55)

    try:
        berat = float(input("Masukkan berat badan dalam kg: "))
        tinggi_cm = float(input("Masukkan tinggi badan dalam cm: "))

        tinggi_m = tinggi_cm / 100

        hasil = tampilkan_hasil(berat, tinggi_m)

        print("\n" + "=" * 55)
        print("HASIL PERHITUNGAN BMI")
        print("=" * 55)

        if hasil["status"] == "success":
            print(f"Berat badan  : {hasil['berat']} kg")
            print(f"Tinggi badan : {tinggi_cm} cm")
            print(f"Tinggi meter : {hasil['tinggi']} m")
            print(f"Nilai BMI    : {hasil['bmi']}")
            print(f"Kategori     : {hasil['kategori']}")
            print(f"Pesan        : {hasil['pesan']}")
        else:
            print(f"Error: {hasil['pesan']}")

    except ValueError:
        print("\nError: Input harus berupa angka.")
        print("Contoh input benar: berat = 70, tinggi = 175")

    print("=" * 55)


if __name__ == "__main__":
    main()
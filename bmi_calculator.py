"""
BMI Calculator - Program Kalkulator Body Mass Index
Fungsi: Menghitung BMI dan menentukan kategori berdasarkan berat dan tinggi
"""

def hitung_bmi(berat, tinggi):
    """
    Menghitung nilai BMI berdasarkan berat (kg) dan tinggi (m)
    
    Args:
        berat (float): Berat badan dalam kilogram
        tinggi (float): Tinggi badan dalam meter
    
    Returns:
        float: Nilai BMI (dibulatkan 2 desimal)
    """
    bmi = berat / (tinggi ** 2)
    return round(bmi, 2)


def kategori_bmi(nilai_bmi):
    """
    Menentukan kategori BMI berdasarkan nilai BMI
    
    Args:
        nilai_bmi (float): Nilai BMI
    
    Returns:
        str: Kategori BMI (Underweight, Normal, Overweight, Obese)
    """
    if nilai_bmi < 18.5:
        return "Underweight"
    elif 18.5 <= nilai_bmi <= 24.9:
        return "Normal"
    elif 25.0 <= nilai_bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def validasi_input(berat, tinggi):
    """
    Memvalidasi input berat dan tinggi
    
    Args:
        berat (float): Berat badan dalam kilogram
        tinggi (float): Tinggi badan dalam meter
    
    Returns:
        bool: True jika input valid, False jika tidak valid
    """
    if not isinstance(berat, (int, float)) or not isinstance(tinggi, (int, float)):
        return False
    
    if berat <= 0 or tinggi <= 0:
        return False
    
    return True


def tampilkan_hasil(berat, tinggi):
    """
    Menghitung dan menampilkan hasil BMI lengkap
    
    Args:
        berat (float): Berat badan dalam kilogram
        tinggi (float): Tinggi badan dalam meter
    
    Returns:
        dict: Dictionary berisi hasil perhitungan BMI
    """
    if not validasi_input(berat, tinggi):
        return {
            "status": "error",
            "pesan": "Input tidak valid! Berat dan tinggi harus bilangan positif."
        }
    
    bmi = hitung_bmi(berat, tinggi)
    kategori = kategori_bmi(bmi)
    
    if kategori == "Underweight":
        pesan = "Anda kekurangan berat badan. Pertimbangkan untuk konsultasi gizi."
    elif kategori == "Normal":
        pesan = "Berat badan Anda ideal! Pertahankan pola hidup sehat."
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


if __name__ == "__main__":
    print("=" * 50)
    print("BMI CALCULATOR - Kalkulator Body Mass Index")
    print("=" * 50)
    
    print("\n--- Contoh 1: Input Valid (Normal) ---")
    hasil = tampilkan_hasil(70, 1.75)
    if hasil["status"] == "success":
        print(f"Berat: {hasil['berat']} kg")
        print(f"Tinggi: {hasil['tinggi']} m")
        print(f"BMI: {hasil['bmi']}")
        print(f"Kategori: {hasil['kategori']}")
        print(f"Pesan: {hasil['pesan']}")
    
    print("\n--- Contoh 2: Input Valid (Underweight) ---")
    hasil = tampilkan_hasil(45, 1.60)
    if hasil["status"] == "success":
        print(f"Berat: {hasil['berat']} kg")
        print(f"Tinggi: {hasil['tinggi']} m")
        print(f"BMI: {hasil['bmi']}")
        print(f"Kategori: {hasil['kategori']}")
        print(f"Pesan: {hasil['pesan']}")
    
    print("\n--- Contoh 3: Input Invalid (Negatif) ---")
    hasil = tampilkan_hasil(-5, 1.70)
    if hasil["status"] == "error":
        print(f"Error: {hasil['pesan']}")
    
    print("\n" + "=" * 50)
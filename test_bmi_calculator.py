"""
Unit Test untuk BMI Calculator
Menguji fungsi-fungsi: hitung_bmi, kategori_bmi, validasi_input
"""

import pytest
from bmi_calculator import hitung_bmi, kategori_bmi, validasi_input, tampilkan_hasil


# ============================================
# TEST 1: Fungsi hitung_bmi
# ============================================
def test_hitung_bmi_normal():
    """Test fungsi hitung_bmi dengan input normal"""
    berat = 70
    tinggi = 1.75
    expected = 22.86
    
    result = hitung_bmi(berat, tinggi)
    
    assert result == expected, f"Expected {expected}, tapi dapat {result}"


def test_hitung_bmi_underweight():
    """Test fungsi hitung_bmi dengan berat ringan"""
    berat = 45
    tinggi = 1.60
    expected = 17.58
    
    result = hitung_bmi(berat, tinggi)
    
    assert result == expected, f"Expected {expected}, tapi dapat {result}"


def test_hitung_bmi_obese():
    """Test fungsi hitung_bmi dengan berat besar"""
    berat = 95
    tinggi = 1.70
    expected = 32.87
    
    result = hitung_bmi(berat, tinggi)
    
    assert result == expected, f"Expected {expected}, tapi dapat {result}"


# ============================================
# TEST 2: Fungsi kategori_bmi
# ============================================
def test_kategori_bmi_underweight():
    """Test kategori BMI untuk nilai underweight"""
    assert kategori_bmi(17.0) == "Underweight"
    assert kategori_bmi(18.4) == "Underweight"


def test_kategori_bmi_normal():
    """Test kategori BMI untuk nilai normal"""
    assert kategori_bmi(18.5) == "Normal"
    assert kategori_bmi(22.0) == "Normal"
    assert kategori_bmi(24.9) == "Normal"


def test_kategori_bmi_overweight():
    """Test kategori BMI untuk nilai overweight"""
    assert kategori_bmi(25.0) == "Overweight"
    assert kategori_bmi(27.5) == "Overweight"
    assert kategori_bmi(29.9) == "Overweight"


def test_kategori_bmi_obese():
    """Test kategori BMI untuk nilai obese"""
    assert kategori_bmi(30.0) == "Obese"
    assert kategori_bmi(32.5) == "Obese"
    assert kategori_bmi(40.0) == "Obese"


# ============================================
# TEST 3: Fungsi validasi_input
# ============================================
def test_validasi_input_valid():
    """Test validasi input dengan data valid"""
    assert validasi_input(70, 1.75) == True
    assert validasi_input(45, 1.60) == True
    assert validasi_input(95, 1.70) == True


def test_validasi_input_berat_negatif():
    """Test validasi input dengan berat negatif"""
    assert validasi_input(-5, 1.75) == False
    assert validasi_input(-10, 1.60) == False


def test_validasi_input_tinggi_nol():
    """Test validasi input dengan tinggi = 0"""
    assert validasi_input(70, 0) == False


# ============================================
# TEST 4: Fungsi tampilkan_hasil (opsional)
# ============================================
def test_tampilkan_hasil_success():
    """Test fungsi tampilkan_hasil dengan input valid"""
    result = tampilkan_hasil(70, 1.75)
    
    assert result["status"] == "success"
    assert result["berat"] == 70
    assert result["tinggi"] == 1.75
    assert result["bmi"] == 22.86
    assert result["kategori"] == "Normal"


def test_tampilkan_hasil_error():
    """Test fungsi tampilkan_hasil dengan input invalid"""
    result = tampilkan_hasil(-5, 1.75)
    
    assert result["status"] == "error"
    assert "pesan" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
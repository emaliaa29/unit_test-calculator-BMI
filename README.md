# Test Case Design - BMI Calculator

**Mata Kuliah:** Analisis Pengujian Sistem  
**Program:** BMI Calculator  
**Tanggal:** 7 Oktober 2026  
**Penulis:** [Nama Kamu]

---

## Daftar Test Case

| No | Test Case ID | Fungsi | Deskripsi | Status |
|----|--------------|--------|-----------|--------|
| 1 | TC001 | hitung_bmi | Hitung BMI dengan input normal | ✅ PASS |
| 2 | TC002 | hitung_bmi | Hitung BMI dengan berat ringan | ✅ PASS |
| 3 | TC003 | hitung_bmi | Hitung BMI dengan berat besar | ✅ PASS |
| 4 | TC004 | kategori_bmi | Kategori Underweight | ✅ PASS |
| 5 | TC005 | kategori_bmi | Kategori Normal | ✅ PASS |
| 6 | TC006 | kategori_bmi | Kategori Overweight | ✅ PASS |
| 7 | TC007 | kategori_bmi | Kategori Obese | ✅ PASS |
| 8 | TC008 | validasi_input | Input valid (positif) | ✅ PASS |
| 9 | TC009 | validasi_input | Input berat negatif | ✅ PASS |
| 10 | TC010 | validasi_input | Input tinggi nol | ✅ PASS |
| 11 | TC011 | tampilkan_hasil | Hasil success dengan input valid | ✅ PASS |
| 12 | TC012 | tampilkan_hasil | Hasil error dengan input invalid | ✅ PASS |

---

## Detail Test Case

### TC001: Hitung BMI Normal

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC001 |
| **Fungsi** | hitung_bmi |
| **Test Scenario** | Menghitung BMI dengan input normal (70 kg, 1.75 m) |
| **Precondition** | Fungsi hitung_bmi sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi hitung_bmi(70, 1.75)<br>2. Tangkap hasil return |
| **Test Data** | berat = 70 kg, tinggi = 1.75 m |
| **Expected Result** | BMI = 22.86 |
| **Actual Result** | 22.86 |
| **Status** | ✅ PASS |

---

### TC002: Hitung BMI Underweight

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC002 |
| **Fungsi** | hitung_bmi |
| **Test Scenario** | Menghitung BMI dengan berat ringan (45 kg, 1.60 m) |
| **Precondition** | Fungsi hitung_bmi sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi hitung_bmi(45, 1.60)<br>2. Tangkap hasil return |
| **Test Data** | berat = 45 kg, tinggi = 1.60 m |
| **Expected Result** | BMI = 17.58 |
| **Actual Result** | 17.58 |
| **Status** | ✅ PASS |

---

### TC003: Hitung BMI Obese

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC003 |
| **Fungsi** | hitung_bmi |
| **Test Scenario** | Menghitung BMI dengan berat besar (95 kg, 1.70 m) |
| **Precondition** | Fungsi hitung_bmi sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi hitung_bmi(95, 1.70)<br>2. Tangkap hasil return |
| **Test Data** | berat = 95 kg, tinggi = 1.70 m |
| **Expected Result** | BMI = 32.87 |
| **Actual Result** | 32.87 |
| **Status** | ✅ PASS |

---

### TC004: Kategori BMI - Underweight

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC004 |
| **Fungsi** | kategori_bmi |
| **Test Scenario** | Menentukan kategori untuk BMI underweight |
| **Precondition** | Fungsi kategori_bmi sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi kategori_bmi(17.0)<br>2. Tangkap hasil return |
| **Test Data** | bmi = 17.0 |
| **Expected Result** | "Underweight" |
| **Actual Result** | "Underweight" |
| **Status** | ✅ PASS |

---

### TC005: Kategori BMI - Normal

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC005 |
| **Fungsi** | kategori_bmi |
| **Test Scenario** | Menentukan kategori untuk BMI normal |
| **Precondition** | Fungsi kategori_bmi sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi kategori_bmi(22.0)<br>2. Tangkap hasil return |
| **Test Data** | bmi = 22.0 |
| **Expected Result** | "Normal" |
| **Actual Result** | "Normal" |
| **Status** | ✅ PASS |

---

### TC006: Kategori BMI - Overweight

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC006 |
| **Fungsi** | kategori_bmi |
| **Test Scenario** | Menentukan kategori untuk BMI overweight |
| **Precondition** | Fungsi kategori_bmi sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi kategori_bmi(27.5)<br>2. Tangkap hasil return |
| **Test Data** | bmi = 27.5 |
| **Expected Result** | "Overweight" |
| **Actual Result** | "Overweight" |
| **Status** | ✅ PASS |

---

### TC007: Kategori BMI - Obese

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC007 |
| **Fungsi** | kategori_bmi |
| **Test Scenario** | Menentukan kategori untuk BMI obese |
| **Precondition** | Fungsi kategori_bmi sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi kategori_bmi(32.5)<br>2. Tangkap hasil return |
| **Test Data** | bmi = 32.5 |
| **Expected Result** | "Obese" |
| **Actual Result** | "Obese" |
| **Status** | ✅ PASS |

---

### TC008: Validasi Input - Data Valid

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC008 |
| **Fungsi** | validasi_input |
| **Test Scenario** | Validasi input dengan data valid |
| **Precondition** | Fungsi validasi_input sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi validasi_input(70, 1.75)<br>2. Tangkap hasil return |
| **Test Data** | berat = 70, tinggi = 1.75 |
| **Expected Result** | True |
| **Actual Result** | True |
| **Status** | ✅ PASS |

---

### TC009: Validasi Input - Berat Negatif

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC009 |
| **Fungsi** | validasi_input |
| **Test Scenario** | Validasi input dengan berat negatif |
| **Precondition** | Fungsi validasi_input sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi validasi_input(-5, 1.75)<br>2. Tangkap hasil return |
| **Test Data** | berat = -5, tinggi = 1.75 |
| **Expected Result** | False |
| **Actual Result** | False |
| **Status** | ✅ PASS |

---

### TC010: Validasi Input - Tinggi Nol

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC010 |
| **Fungsi** | validasi_input |
| **Test Scenario** | Validasi input dengan tinggi = 0 |
| **Precondition** | Fungsi validasi_input sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi validasi_input(70, 0)<br>2. Tangkap hasil return |
| **Test Data** | berat = 70, tinggi = 0 |
| **Expected Result** | False |
| **Actual Result** | False |
| **Status** | ✅ PASS |

---

### TC011: Tampilkan Hasil - Success

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC011 |
| **Fungsi** | tampilkan_hasil |
| **Test Scenario** | Menampilkan hasil dengan input valid |
| **Precondition** | Fungsi tampilkan_hasil sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi tampilkan_hasil(70, 1.75)<br>2. Tangkap hasil return |
| **Test Data** | berat = 70, tinggi = 1.75 |
| **Expected Result** | status = "success", bmi = 22.86, kategori = "Normal" |
| **Actual Result** | status = "success", bmi = 22.86, kategori = "Normal" |
| **Status** | ✅ PASS |

---

### TC012: Tampilkan Hasil - Error

| Field | Isi |
|-------|-----|
| **Test Case ID** | TC012 |
| **Fungsi** | tampilkan_hasil |
| **Test Scenario** | Menampilkan error dengan input invalid |
| **Precondition** | Fungsi tampilkan_hasil sudah diimplementasi |
| **Test Steps** | 1. Panggil fungsi tampilkan_hasil(-5, 1.75)<br>2. Tangkap hasil return |
| **Test Data** | berat = -5, tinggi = 1.75 |
| **Expected Result** | status = "error", ada pesan error |
| **Actual Result** | status = "error", pesan = "Input tidak valid..." |
| **Status** | ✅ PASS |

---

## Ringkasan Hasil Pengujian

| Metric | Nilai |
|--------|-------|
| **Total Test Case** | 12 |
| **Pass** | 12 |
| **Fail** | 0 |
| **Success Rate** | 100% |
| **Status Keseluruhan** | ✅ ALL TESTS PASSED |

---

## Analisis Hasil

Dari 12 test case yang telah dijalankan, **semua test case (100%) berstatus PASS**. Ini menunjukkan bahwa:

1. ✅ Fungsi `hitung_bmi()` menghitung nilai BMI dengan benar sesuai rumus matematika
2. ✅ Fungsi `kategori_bmi()` mengklasifikasikan BMI ke dalam 4 kategori dengan tepat
3. ✅ Fungsi `validasi_input()` berhasil mendeteksi input invalid (negatif dan nol)
4. ✅ Fungsi `tampilkan_hasil()` mengembalikan dictionary lengkap dengan status yang benar

**Kesimpulan:**

Program BMI Calculator **telah lolos unit testing** dan siap untuk tahap pengujian selanjutnya.

**Rekomendasi:**

- Tambahkan test case untuk nilai ekstrem (sangat besar/sangat kecil)
- Tambahkan validasi untuk tipe data (misal: input string)
- Tambahkan test untuk boundary values (18.5, 24.9, 25.0, 29.9, 30.0)
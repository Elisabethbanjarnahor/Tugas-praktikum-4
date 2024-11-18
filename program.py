data_mahasiswa = []

while True:
    nama = input("Masukkan nama mahasiswa (atau tekan Enter untuk berhenti): ")
    if not nama:
        break

    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas

    mahasiswa = {
        'nama': nama,
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'nilai_akhir': nilai_akhir
    }
    data_mahasiswa.append(mahasiswa)

print("\nDaftar Mahasiswa:")
for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"{i}. {mahasiswa['nama']}")
    print(f"   Nilai Tugas: {mahasiswa['tugas']}")
    print(f"   Nilai UTS: {mahasiswa['uts']}")
    print(f"   Nilai UAS: {mahasiswa['uas']}")
    print(f"   Nilai Akhir: {mahasiswa['nilai_akhir']}")
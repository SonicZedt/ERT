# ERT
Elkom Recap Tool adalah sebuah tool yang dibuat untuk memudahkan Penanggung Jawab Praktikum Lab. Elektronika Dasar, Sistem Digital, Mikroprosesor, Sistem Tertanam, dan Interface dalam membuat rekapan praktikum (_.docx_) dan shift Penanggung Jawab Shift (_.txt_) mingguan.

### Cara pengoperasian
1. Masukan semua laporan PJ Shift (_.docx_) minggu ke-n ke dalam folder .\BAP\Minggu_n, folder tersebut dapat dibuat secara manual.
2. Urutkan laporan dengan mengubah nama tiap file laporan (_.docx_), dapat dengan memberikan nomor urut atau urutan abjad di awal.  
![fileList_raw](https://user-images.githubusercontent.com/83224221/135095716-e921f523-3b4d-4e11-9a28-2d5e383d589a.jpg)
3. Buka file `ERT.exe`
4. Masukan input yang dibutuhkan:
   - `Lab: ` `str` (eldas, sisdig, mp, sister, iface) atau (ELDAS, SISDIG, MP, SISTER, IFACE)
   - `Minggu ke-: ` `int`
   - `Jenjang: ` `str`
   - `Daring (y/n): ` `str` (y atau yang lainnya). Akan ditambahkan text ` SELAMA COVID-19` pada header dan ` secara virtual` pada subheader untuk rekapan (_.docx_) apabila diberikan input y  
   ![ERT](https://user-images.githubusercontent.com/83224221/135095803-ce72ae8a-567b-4b03-a7ec-04f65fee2ece.jpg)
5. Selesai. Hasil rekapan bisa dilihat di folder .\Recap  
![output](https://user-images.githubusercontent.com/83224221/135096210-6dca1914-57a1-423c-8763-7530a3171011.jpg)

### Pembaharuan data nama Asisten
Data nama Asisten dan Coass disimpan dalam format (_.xlsx_) di dalam folder .\Data dan dapat ditambah, diubah, serta dihapus menggunakan software yang mendukung ekstensi tersebut.  
Nama baru yang ditambahkan tidak perlu nama lengkap, dan disarankan hanya memasukan nama yang sekiranya akan ditulis pada laporan PJ Shift.
Apabila nama coass seorang Asisten tidak diketahui atau sebaliknya, maka dapat diisi dengan `unknown` karena kolom `Assistant` dan `Coass` dalam baris yang sama salah satunya tidak dapat dibiarkan kosong.

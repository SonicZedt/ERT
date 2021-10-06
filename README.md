# ERT
Elkom Recap Tool adalah sebuah tool yang dibuat untuk memudahkan Penanggung Jawab Praktikum Lab. Elektronika Dasar, Sistem Digital, Mikroprosesor, Sistem Tertanam, dan Interface dalam membuat rekapan praktikum (_.docx_) dan shift Penanggung Jawab Shift (_.txt_) mingguan.
<br/>
  
### Cara pengoperasian
1. Masukan semua laporan PJ Shift (_.docx_) minggu ke-n ke dalam folder .\BAP\Minggu_n, folder tersebut dapat dibuat secara manual.
2. Urutkan laporan dengan mengubah nama tiap file laporan (_.docx_), dapat dengan memberikan nomor urut atau urutan abjad di awal.  
![fileList_raw](https://user-images.githubusercontent.com/83224221/135095716-e921f523-3b4d-4e11-9a28-2d5e383d589a.jpg)
3. Buka file `ERT.exe`
4. Masukan input yang dibutuhkan:
   - `Lab: str`. Berikut adalah list input yang dapat terbaca:
      - `["eldas", "ELEKTRONIKA DASAR", "Elektronika Dasar"],`
      - `["elan", "ELEKTRONIKA LANJUT", "Elektronika Lanjut"],`
      - `["sisdig", "SISTEM DIGITAL", "Sistem Digital"],`
      - `["mp", "MIRKOPROSESOR", "Mikroprosesor"],`
      - `["sister", "SISTEM TERTANAM", "Sistem Tertanam"],`
      - `["iface", "INTERFACE", "Interface"]`
   - `Minggu ke-: int`
   - `Jenjang: str`
   - `Daring (y/n): str` (y atau yang lainnya). Akan ditambahkan text ` SELAMA COVID-19` pada header dan ` secara virtual` pada subheader untuk rekapan (_.docx_) apabila diberikan input `y`  
   ![ERT](https://user-images.githubusercontent.com/83224221/135095803-ce72ae8a-567b-4b03-a7ec-04f65fee2ece.jpg)
5. Selesai. Hasil rekapan bisa dilihat di folder .\Recap  
![output](https://user-images.githubusercontent.com/83224221/135096210-6dca1914-57a1-423c-8763-7530a3171011.jpg)
<br/>
  
### Format Laporan PJ Shift
Format laporan PJ Shift yang dapat dibaca adalah laporan yang berekstensi (_.docx_) dan didalamnya terdapat:
- `Hari`. Nama hari yang dapat terbaca adalah `["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]`.
- `Kelas/Shift`. Kelas yang dapat terbaca adalah yang 3 huruf pertamanya `["2KB", "3KB", "2DC", "3DC"]`. Shift yang dapat terbaca adalah `["Shift 1", "Shift 2", "Shift 3", "Shift 4"]`
- `(Nama Asisten/Coass)` yang dapat terbaca adalah nama-nama yang tertera di dalam *Data_Assistant.xlxs*
> Semua text tersebut bersifat ***CASE SENSITIVE*** dan ***STYLE SENSITIVE***

Atau untuk lebih jelasnya dapat lihat [contoh laporan PJ Shift](https://docs.google.com/document/d/1Vd3yxQcf4oYirQsO771hFuyklJY6h4HN/edit?usp=sharing&ouid=106238154602768730311&rtpof=true&sd=true)
<br/>
  
### Pembaharuan data nama Asisten
Data nama Asisten, nama Coass, dan nama alternatif disimpan dalam format (_.csv_) di dalam [/Data](https://github.com/SonicZedt/ERT/tree/alt/Data).
Nama baru yang ditambahkan tidak perlu nama lengkap, dan disarankan hanya memasukan nama yang sekiranya akan ditulis pada laporan PJ Shift.
Apabila nama coass seorang Asisten tidak diketahui atau sebaliknya, maka kolom tersebut dapat dibiarkan kosong.

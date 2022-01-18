# ERT
Elkom Recap Tool adalah sebuah tool yang dibuat untuk memudahkan Penanggung Jawab Praktikum Lab. Elektronika Dasar, Sistem Digital, Mikroprosesor, Sistem Tertanam, dan Interface dalam membuat rekapan praktikum (_.docx_) dan shift Penanggung Jawab Shift (_.txt_) mingguan.
<br/>
  
### Cara pengoperasian
1. Download ERT.zip versi terbaru [di sini](https://github.com/SonicZedt/ERT/releases)
2. Masukan semua laporan PJ Shift (_.docx_) minggu ke-n ke dalam folder .\BAP\Minggu_n, folder tersebut dapat dibuat secara manual. Dokumen laporan untuk percobaan dapat di-download [di sini](https://drive.google.com/drive/folders/1OnGWbI7Od5HAZgkTv5CoOPJxJEpL0TaW?usp=sharing)
3. Urutkan laporan dengan mengubah nama tiap file laporan (_.docx_), dapat dengan memberikan nomor urut atau urutan abjad di awal.  
![fileList_raw](https://user-images.githubusercontent.com/83224221/135095716-e921f523-3b4d-4e11-9a28-2d5e383d589a.jpg)
3. Buka file `ERT.exe`
4. Masukan input yang dibutuhkan:
   - `Minggu ke-: int`
   - `Jenjang: str`
   - `Daring (y/n): str` (y atau yang lainnya). Akan ditambahkan text ` SELAMA COVID-19` pada header dan ` secara virtual` pada subheader untuk rekapan (_.docx_) apabila diberikan input `y`  
   ![ERT](https://user-images.githubusercontent.com/83224221/135095803-ce72ae8a-567b-4b03-a7ec-04f65fee2ece.jpg)
5. Selesai. Hasil rekapan bisa dilihat di folder .\Recap  
![output](https://user-images.githubusercontent.com/83224221/135096210-6dca1914-57a1-423c-8763-7530a3171011.jpg)
<br/>
  
### Format Laporan PJ Shift
Format laporan PJ Shift yang dapat dibaca adalah laporan yang berekstensi (_.docx_), nama file mengandung text `eldas, sisdig, mp, sister, atau iface` **(tidak case sensitive)**, serta didalamnya terdapat:
- `Hari`. Nama hari yang dapat terbaca adalah `["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]`.
- `Kelas/Shift`. Kelas yang dapat terbaca adalah yang 3 huruf pertamanya `["2KB", "3KB", "2DC", "3DC"]`. Shift yang dapat terbaca adalah `["Shift 1", "Shift 2", "Shift 3", "Shift 4", "Shift 5"]`
- `(Nama Asisten/Coass)` yang dapat terbaca adalah nama-nama yang tertera di dalam *data_Assistant.xlxs*
<br/>
Tanggal dan Hari tidak akan terbaca apabila tulisan `Hari` tidak ada atau ditulis secara tidak benar di dalam laporan.
<br/>
Kelas dan Shift tidak akan terbaca apabila tulisan `Kelas` tidak ada atau ditulis secara tidak benar di dalam laporan.
> tulisan `Hari` dan `Kelas` dalam laporan bersifat ***Case Sensitive***

Untuk lebih jelasnya dapat lihat [contoh laporan PJ Shift](https://docs.google.com/document/d/1Vd3yxQcf4oYirQsO771hFuyklJY6h4HN/edit?usp=sharing&ouid=106238154602768730311&rtpof=true&sd=true)
<br/>
  
### Koneksi
ERT memerlukan koneksi internet untuk membaca data. Operasi tidak dapat dilakukan apabila .\Data kosong

### Lisensi
File `Lisence.ZEDT` harus sesuai dan diletakan di dalam direktori instalasi agar proses perekapan otomatis dapat dilakukan

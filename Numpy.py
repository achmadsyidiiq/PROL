# sekali-kali ngasihlah biar semangat bikin bocoran!
# udah laper malah disuruh mikir
# https://saweria.co/azuria
# jika kode error hubungi admin



import numpy as np

"""
1. Buat array numpy 1 dimensi dengan nilai secara urut dari 0 (nol) sampai dengan 20,
kemudian tampilkan nilai mulai dari index ke 3 sampai ke 15 dengan step kelipatan 3."""

a = np.arange(21)
a
a[3:16:3]

"""
2. Buat array numpy 2 dimensi dengan panjang x = 5 dan y = 5 berisikan nilai seperti
berikut. Kemudian cari block array yang telah diwarnai sebagai berikut menggunakan
single element indexing
"""
b = np.array([[1, 5, 4, 3, 2], [2, 1, 5, 4, 3], [ 3, 2, 1, 5, 4], [4, 3, 2, 1, 5], [5, 4, 3, 2, 1]])
b
b[0, 1]
b[1, 2]
b[3, 4]
b[4, 0]

"""
3. Buat array numpy 3 dimensi dengan panjang x = 5, y = 5 dan z = 5. Tampilkan hasil
pembuatan array numpy tersebut, kemudian tampilkan element nilai pada :
- index x = 3, y = 4 dan z = 3
- index x = 2, y = 0 dan z = 1
- index x = 4, y = 3 dan z = 2
tampil element menggunakan advanced indexing
"""
c = np.random.random((5, 5, 5))
c
c[[[3, 1, 2], [3, 2, 4], [4, 0, 3]]]

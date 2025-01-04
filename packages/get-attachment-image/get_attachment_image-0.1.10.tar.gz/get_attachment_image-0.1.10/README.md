# get_attachment_image

`get_attachment_image` adalah paket Python yang memungkinkan Anda untuk mendapatkan gambar attachment yang terkait dengan model tertentu di Odoo. Paket ini memudahkan integrasi dengan sistem `Odoo` untuk mengambil file gambar yang terkait dengan entitas tertentu.

## Fitur

- Mengambil gambar attachment berdasarkan `res_model` dan `res_id`.
- Menggunakan query SQL untuk mengekstrak gambar attachment dari Odoo.

## Instalasi

Untuk menginstal paket ini, gunakan pip:
```python
pip install get-attachment-image
```

## Penggunaan 
1. Mengimpor fungsi dari paket get_attachment_image
```python
    from get_attachment_image import get_attachment_image
```
2. Deklrasi Variabel
```python
    model = 'nama.model'
    res_id = 123  # ID objek terkait
    name = 'nama field'
```
3. Menggunakan fungsi untuk mendapatkan ID gambar lampiran
```python
    image_id = get_attachment_image(model, res_id, name)
    if image_id:
        print(f"ID gambar: {image_id}")
    else:
        print("Gambar tidak ditemukan")
````

from PIL import Image
import os

def resize_images(input_dir, output_dir, quality, kb):
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.JPEG') or filename.endswith('.PNG') or filename.endswith('.JPG'):
            with Image.open(os.path.join(input_dir, filename)) as img:
                img.save(os.path.join(output_dir, filename), optimize=True, quality=quality)
                # optimize=True parametresi JPEG sıkıştırması yapar ve boyutu azaltır.
                # quality=95 parametresi JPEG kalitesini ayarlar.
            filesize = os.path.getsize(os.path.join(output_dir, filename)) / 1024 # Dosya boyutunu KB cinsinden alırız.
            while filesize > kb:
                img = Image.open(os.path.join(output_dir, filename))
                quality -= 1
                img.save(os.path.join(output_dir, filename), optimize=True, quality=quality) # JPEG sıkıştırması ile kaliteyi azaltırız.
                filesize = os.path.getsize(os.path.join(output_dir, filename)) / 1024
                if filesize < kb+1:
                    break # Dosya boyutu hedeflenen boyutun altına düştüğünde döngüden çık.
    print('Resim boyutları başarıyla güncellendi.')

# Kullanımı:
input_dir = 'inputs/'
output_dir = 'outputs/'
quality = 90
kb = 350 # Hedeflenen dosya boyutu KB cinsinden.
resize_images(input_dir, output_dir, quality, kb)

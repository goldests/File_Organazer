import os
from pathlib import Path
import shutil


os.chdir("c:/Users/goldest/Downloads")


folder = 'c:/Users/goldest/Downloads'
files = os.listdir()

png_image = [f for f in files if f.endswith('.png')] # смотрим сколько png
folder_png = 'Png_Image' # создаем папку 

os.makedirs(folder_png, exist_ok=True) # если есть, просто входим

for photo in png_image:
    shutil.move(photo, os.path.join(folder_png, photo)) # перекидываем все фотки в папку




# jpg
files = os.listdir()

jpg_image = [f for f in files if f.lower().endswith('.jpg')]
folder_jpg = 'Jpg_Image'

os.makedirs(folder_jpg, exist_ok=True)

for photo in jpg_image:
    shutil.move(photo, os.path.join(folder_jpg, photo))




# jar
files = os.listdir()

jar_file = [f for f in files if f.endswith('.jar')]
folder_jar = 'jar_File'

os.makedirs(folder_jar, exist_ok=True)

for file in jar_file:
    shutil.move(file, os.path.join(folder_jar, file))




# apk
files = os.listdir()

apk_file = [f for f in files if f.endswith('.apk')]
folder_apk = 'apk_File'

os.makedirs(folder_apk, exist_ok=True)

for file in apk_file:
    shutil.move(file, os.path.join(folder_apk, file))




# Html
files = os.listdir()

html_file = [f for f in files if f.endswith('.html')]
folder_html = 'Html_File'

os.makedirs(folder_html, exist_ok=True)

for file in html_file:
    shutil.move(file, os.path.join(folder_html, file))




# svg
files = os.listdir()

svg_file = [f for f in files if f.endswith('.svg')]
folder_svg = 'svg_File'

os.makedirs(folder_svg, exist_ok=True)

for file in svg_file:
    shutil.move(file, os.path.join(folder_svg, file))




# ogg
files = os.listdir()

ogg_file = [f for f in files if f.endswith('.ogg')]
folder_ogg = 'ogg_File'

os.makedirs(folder_ogg, exist_ok=True)

for file in ogg_file:
    shutil.move(file, os.path.join(folder_ogg, file))




# pdf
files = os.listdir()

pdf_file = [f for f in files if f.endswith('.pdf')]
folder_pdf = 'pdf_File'

os.makedirs(folder_pdf, exist_ok=True)

for file in pdf_file:
    shutil.move(file, os.path.join(folder_pdf, file))




# pyd
files = os.listdir()

pyd_file = [f for f in files if f.endswith('.pyd')]
folder_pyd = 'pyd_File'

os.makedirs(folder_pyd, exist_ok=True)

for file in pyd_file:
    shutil.move(file, os.path.join(folder_pyd, file))




# rar
files = os.listdir()

rar = ('rar', '7z', 'tgz')

rar_file = [f for f in files if f.endswith(rar)]
folder_rar = 'rar_File'

os.makedirs(folder_rar, exist_ok=True)

for file in rar_file:
    shutil.move(file, os.path.join(folder_rar, file))




# docx
files = os.listdir()

docx_file = [f for f in files if f.endswith('.docx')]
folder_docx = 'docx_File'

os.makedirs(folder_docx, exist_ok=True)

for file in docx_file:
    shutil.move(file, os.path.join(folder_docx, file))




# mp3
files = os.listdir()

mp_file = [f for f in files if f.endswith('.mp3')]
folder_mp = 'Mp3_File'

os.makedirs(folder_mp, exist_ok=True)

for file in mp_file:
    shutil.move(file, os.path.join(folder_mp, file))




# xls
files = os.listdir()

xls_file = [f for f in files if f.endswith('.xls')]
folder_xls = 'Xls_File'

os.makedirs(folder_xls, exist_ok=True)

for file in xls_file:
    shutil.move(file, os.path.join(folder_xls, file))




# msi
files = os.listdir()

msi_file = [f for f in files if f.endswith('.msi')]
folder_msi = 'msi_File'

os.makedirs(folder_msi, exist_ok=True)

for file in msi_file:
    shutil.move(file, os.path.join(folder_msi, file))




# pptx
files = os.listdir()

pptx_file = [f for f in files if f.endswith('.pptx')]
folder_pptx = 'Pptx_File'

os.makedirs(folder_pptx, exist_ok=True)

for file in pptx_file:
    shutil.move(file, os.path.join(folder_pptx, file))




# exe
files = os.listdir()

exe_file = [f for f in files if f.lower().endswith('.exe')]
folder_exe = 'Exe_File'

os.makedirs(folder_exe, exist_ok=True)

for file in exe_file:
    shutil.move(file, os.path.join(folder_exe, file))




# dll
files = os.listdir()

dll_file = [f for f in files if f.lower().endswith('.dll')]
folder_dll = 'dll_File'

os.makedirs(folder_dll, exist_ok=True)

for file in dll_file:
    shutil.move(file, os.path.join(folder_dll, file))




# zip
files = os.listdir()

zip_file = [f for f in files if f.lower().endswith('.zip')]
folder_zip = 'Zip_folder'

os.makedirs(folder_zip, exist_ok=True)

for file in zip_file:
    shutil.move(file, os.path.join(folder_zip, file))




# txt
files = os.listdir()

txt = ('.txt', '.log')

txt_file = [f for f in files if f.lower().endswith(txt)]
folder_txt = 'txt_File'

os.makedirs(folder_txt, exist_ok=True)

for file in txt_file:
    shutil.move(file, os.path.join(folder_txt, file))




# pth
files = os.listdir()

pth_file = [f for f in files if f.lower().endswith('._pth')]
folder_pth = 'pth_File'

os.makedirs(folder_pth, exist_ok=True)

for file in pth_file:
    shutil.move(file, os.path.join(folder_pth, file))




# avif
files = os.listdir()

avif_file = [f for f in files if f.lower().endswith('.avif')]
folder_avif = 'avif_File'

os.makedirs(folder_avif, exist_ok=True)

for file in avif_file:
    shutil.move(file, os.path.join(folder_avif, file))




# gif
files = os.listdir()

gif_file = [f for f in files if f.lower().endswith('.gif')]
folder_gif = 'gif_File'

os.makedirs(folder_gif, exist_ok=True)

for file in gif_file:
    shutil.move(file, os.path.join(folder_gif, file))




# jpeg
files = os.listdir()

jpeg_file = [f for f in files if f.lower().endswith('.jpeg')]
folder_jpeg = 'jpeg_File'

os.makedirs(folder_jpeg, exist_ok=True)

for file in jpeg_file:
    shutil.move(file, os.path.join(folder_jpeg, file))




# mkv
files = os.listdir()

mkv_file = [f for f in files if f.lower().endswith('.mkv')]
folder_mkv = 'mkv_File'

os.makedirs(folder_mkv, exist_ok=True)

for file in mkv_file:
    shutil.move(file, os.path.join(folder_mkv, file))




# mp4
files = os.listdir()

mp4_file = [f for f in files if f.lower().endswith('.mp4')]
folder_mp4 = 'mp4_File'

os.makedirs(folder_mp4, exist_ok=True)

for file in mp4_file:
    shutil.move(file, os.path.join(folder_mp4, file))




# torrent
files = os.listdir()

torrent_file = [f for f in files if f.lower().endswith('.torrent')]
folder_torrent = 'torrent_File'

os.makedirs(folder_torrent, exist_ok=True)

for file in torrent_file:
    shutil.move(file, os.path.join(folder_torrent, file))




# vdf
files = os.listdir()

vdf_file = [f for f in files if f.lower().endswith('.vdf')]
folder_vdf = 'vdf_File'

os.makedirs(folder_vdf, exist_ok=True)

for file in vdf_file:
    shutil.move(file, os.path.join(folder_vdf, file))




# gif
files = os.listdir()

webp_file = [f for f in files if f.lower().endswith('.webp')]
folder_webp = 'webp_File'

os.makedirs(folder_webp, exist_ok=True)

for file in webp_file:
    shutil.move(file, os.path.join(folder_webp, file))




# WHL
files = os.listdir()

WHL_file = [f for f in files if f.lower().endswith('.whl')]
folder_WHL = 'WHL_File'

os.makedirs(folder_WHL, exist_ok=True)

for file in WHL_file:
    shutil.move(file, os.path.join(folder_WHL, file))




# WINMD
files = os.listdir()

winmd_file = [f for f in files if f.lower().endswith('.winmd')]
folder_winmd = 'winmd_File'

os.makedirs(folder_winmd, exist_ok=True)

for file in winmd_file:
    shutil.move(file, os.path.join(folder_winmd, file))
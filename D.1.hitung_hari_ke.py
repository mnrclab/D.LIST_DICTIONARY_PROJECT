hari = ['senin', 'selasa', 'rabu', 'kamis', 'jum\'at', 'sabtu', 'minggu']
# Sekarang hari 'rabu', hari apakah 100 hari yang lalu?

now = 'rabu'
brphari = -100
jml_hari = 7

sekarang = hari.index(now)
sisa_hari = brphari%jml_hari

hari_ke = hari[(sekarang+sisa_hari)%7]
print('prediksi hari:', hari_ke)

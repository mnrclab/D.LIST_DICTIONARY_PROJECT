days = {
    'senin': 'monday', 'selasa': 'tuesday', 'rabu': 'wednesday',
    'kamis': 'thursday', 'jumat': 'friday', 'sabtu': "saturday",
    'minggu': 'sunday'
}

hari = list(days)
day = list(days.values())

x = input('Ketik nama hari (ENG/IDN): ')

if x.lower() in hari:
    engHari = day[hari.index(x.lower())]
    print(f'Bhs Inggris {x.lower()} adalah {engHari}')
else:
    idDay = hari[day.index(x.lower())]
    print(f'Bhs Indonesia {x.lower()} adalah {idDay}')

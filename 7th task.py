# *Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#         Примеры:
#         1234565 seconds = 14:6:56:5
seconds = int(input('Введите количество секунд: '))
seconds1= seconds % 60
mins = seconds //60%60
hours = seconds // 3600 % 24
days = seconds // 86400
# print(days + ':' + hours + ':' + mins + ':' + seconds1)
print(f'{days}:{hours}:{mins}:{seconds1}')

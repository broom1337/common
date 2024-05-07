ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
shot = input("Сделайте предположение: ")

shot = shot.upper()

ship = ship.upper()

if ship.find(shot) != -1:
    print("Попадание")
else:
    print("Мимо")

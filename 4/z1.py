sq = [x**2 for x in range(1,11)]
print(sq)

days = {x: i+1 for i,x in enumerate(["Понедельник", "Вторник", 
            "Среда", "Четверг", "Пятница", 
            "Суббота", "Воскресенье"] )}

print(days)

lower = [x.lower() for x in ["Django", "FastAPI", "Numpy", 
                           "PYTHON", "Pandas", "FASTAPI", 
                           "Python", "random"]]

print(lower)
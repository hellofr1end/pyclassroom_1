import requests

# Домашка часть 2:
# изучить 

# https://open-meteo.com/


# можно использовать любые средства (интернет), чтобы:

#  получить данные о погоде в Красноярске и вывести
#  данные в консоль в каком-то приличном виде на свое усмотрение

urlBangkok = "https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&current=temperature_2m"
urlKrasnoyarsk = "https://api.open-meteo.com/v1/forecast?latitude=56&longitude=92&current=temperature_2m"

responseB = requests.get(urlBangkok)
responseK = requests.get(urlKrasnoyarsk)

data = responseB.json()
print(f"погода в Бангкоке прямо сейчас: {data["current"]["temperature_2m"]}")


data = responseK.json()
print(f"погода в Красноярске прямо сейчас: {data["current"]["temperature_2m"]}")
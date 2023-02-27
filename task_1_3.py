import datetime
import pytz
import addict

class Task:
    @staticmethod
    def find_fridays_13th():
        today = datetime.date.today()
        friday13 = []
        while len(friday13) < 10:
            if today.day == 13 and today.weekday() == 4:
                friday13.append(today)
            today += datetime.timedelta(days=1)
        return friday13

    @staticmethod
    # этот метод не возвращает разницу между часовыми поясми, я не понял почему. Следующий метод возвращает разницу
    def get_time_diff(city1, city2):
        tz1 = pytz.timezone(city1)
        tz2 = pytz.timezone(city2)

        time1 = datetime.datetime.now(tz1)
        time2 = datetime.datetime.now(tz2)

        difference = (time1 - time2).total_seconds() / 3600
        return time1.strftime("%H:%M:%S"), time2.strftime("%H:%M:%S"), difference

    @staticmethod
    # вот этот уже вернет разницу между часовыми поясами, решение находил тут:
    # https://stackoverflow.com/questions/46736529/how-to-compute-the-time-difference-between-two-time-zones-in-python
    def get_time_diff2(city1, city2):
        date = datetime.datetime.today()
        return (city1.localize(date) - city2.localize(date).astimezone(city1)).seconds / 3600

    @staticmethod
    def get_age_and_sign(birth_date):
        date_format = "%d-%m-%Y"
        birth_datetime = datetime.datetime.strptime(birth_date, date_format)
        today_datetime = datetime.datetime.now()
        age = today_datetime.year - birth_datetime.year - (
                (today_datetime.month, today_datetime.day) < (birth_datetime.month, birth_datetime.day))

        zodiac_signs = {
            (1, 20): "Водолей",
            (2, 19): "Рыба",
            (3, 21): "Овен",
            (4, 20): "Телец",
            (5, 21): "Близнецы",
            (6, 21): "Рак",
            (7, 23): "Лев",
            (8, 23): "Дева",
            (9, 23): "Весы",
            (10, 23): "Скорпион",
            (11, 22): "Стрелец",
            (12, 22): "Козерог"
        }

        zodiac_sign = None
        for key in zodiac_signs:
            if birth_datetime.month == key[0] and birth_datetime.day <= key[1] or birth_datetime.month == \
                    key[0] + 1 and birth_datetime.day >= key[1]:
                zodiac_sign = zodiac_signs[key]
                break

        result = addict.Dict(age=age, zodiac_sign=zodiac_sign)
        return result





# код для создания экземпляра класса Task и вызова его методов
a = Task()
print(a.get_time_diff("Europe/Kiev", "America/Argentina/Buenos_Aires"))
timezone1 = pytz.timezone("Europe/Kiev")
timezone2 = pytz.timezone("America/Los_Angeles")
print(a.get_time_diff2(timezone1, timezone2))
print(a.get_age_and_sign("01-01-2020"))
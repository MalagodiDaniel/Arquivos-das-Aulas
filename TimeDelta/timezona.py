import pytz
from datetime import datetime

data = datetime.now(pytz.timezone("Europe/Oslo"))
print(data)

data_1 = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(data_1)

data_2 = datetime.now(pytz.timezone("Europe/Paris"))
print(data_2)
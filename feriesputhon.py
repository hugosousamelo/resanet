import datetime
import time

liste = []
d = datetime.date.today()
year = d.year
a = year % 4
b = year % 7
c = year % 19
m = 24
n = 5
d = (19 * c + m ) % 30
e = (2 * a + 4 * b + 6 * d + n) % 7
easterdate = 22 + d + e;

if(easterdate > 31):
	day = d + e - 9;
	month = 4;
			
else:
	day = 22 + d + e;
	month = 3;
			

if (d == 29 and e == 6):
	day = 10;
	month = 04;
		
elif (d == 28 and e == 6):
	day = 18;
	month = 04;
	
if (year == None):
	year = time.strftime('%Y');

premierjanvier = datetime.date(year, 1, 1)
fetetravail = datetime.date(year, 5, 1)
victoirealiee = datetime.date(year, 5, 8)
fetenationale = datetime.date(year, 7, 14)
assomption = datetime.date(year, 8, 15)
toussaint = datetime.date(year, 11, 1)
armistice = datetime.date(year, 11, 11)
noel = datetime.date(year, 12, 25)
paque = datetime.date(year, month, day)
lundipaque = paque + datetime.timedelta(1)
ascension = paque + datetime.timedelta(39)
pentecote = paque + datetime.timedelta(50)

liste.append(str(premierjanvier))
liste.append(str(fetetravail))
liste.append(str(victoirealiee))
liste.append(str(fetenationale))
liste.append(str(assomption))
liste.append(str(toussaint))
liste.append(str(armistice))
liste.append(str(noel)) 
liste.append(str(lundipaque))
liste.append(str(ascension))
liste.append(str(pentecote))

print liste

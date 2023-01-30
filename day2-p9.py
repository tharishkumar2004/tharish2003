month=input("enter month:")
day=int(input("enter no.of days:"))

if month in ('january','february','march'):
    season='winter'
elif month in('april','may','june'):
    season='summer'
elif month in('july','augest','september'):
    season='spring'

else:
    season='autumn'
if(month=='march')and(day>19):
    season='summer'
elif(month=='june')and(day>20):
    season='spring'
elif(month=='december')and(day>20):
    season='winter'
print("sesaon is",season)

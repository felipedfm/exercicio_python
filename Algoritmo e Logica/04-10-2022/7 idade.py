idd = int ( input ("digite sua idade em dias"))
ida = idd//365
idm = idd%365
idm = idm//30
idds = (idd%365)%30
print (f"você tem {ida} anos , que no total são {idm} meses ou {idds} dias")

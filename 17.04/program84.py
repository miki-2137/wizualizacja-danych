import numpy as np

imiona = np.array(['Anna','Zofia','Sylwia','Katarzyna','Teresa',
                   'Tomasz','Cezary','Zenon','Filip','Adrian'])
wiek = np.array([21,40,13,31,34,14,13,28,20,15])
plec = np.array(['K','K','K','K','K','M','M','M','M','M'])
waga = np.array([65,80,64,69,74,61,66,61,69,77])
wzrost = np.array([179,179,151,177,170,157,151,153,160,160])
okulary = np.array([False,True,False,True,False,True,False,True,False,True])

print(np.sort([imiona]))

nosza_okulary = np.array(imiona[okulary==True])
print(nosza_okulary)

kobiety2030 = np.array(imiona[np.where((wiek>=20)&(wiek<=30)&(plec=='K'))])
print(kobiety2030)

waga_wzrost = np.array(imiona[np.where((waga>=60)&(waga<=80)&(wzrost>=160)&(wzrost<=180)
                                        &(okulary==False))])
waga_wzrost = np.array(imiona[(waga>=60)|(waga<=80)|(wzrost>=160)|(wzrost<=180)
                                        |(okulary==False)])
print(waga_wzrost)

bmi = np.array([waga/((wzrost/100)**2)])
print(bmi)

sredni_wiek = (np.sum(wiek)/len(wiek))
print(sredni_wiek)
print(imiona[np.isclose(sredni_wiek,wiek,atol=2)])

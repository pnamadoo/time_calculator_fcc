import sys
from datetime import date, time, datetime, timedelta
def add_time(horainicial="",horafinal="",dw=""):
    dw=dw.upper()
    horaini = datetime.strptime(horainicial, '%I:%M %p')
    horaformat= horaini.strftime('%H:%M')
    hformatprint=horaini.strftime('%H:%M %p')
#Convertir fechas
    dict={}
    if dw !='':
        
            if dw == 'MONDAY':
                dw='Monday'
            elif dw == 'TUESDAY':
                dw='Tuesday'
            elif dw == 'WEDNESDAY':
                dw='Wednesday'
            elif dw == 'THURSDAY':
                dw='Thursday'
            elif dw == 'FRIDAY':
                dw='Friday'
            elif dw == 'SATURDAY':
                dw='Saturday'
            elif dw == 'SUNDAY':
                dw='Sunday'
            dict={'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
      
            horaini=horaini+timedelta(days=dict[dw])#1900-01-04 22:15:00

    hf=[]
    hf=horafinal.split(":")
    hfini=hf[0]
    hfn=int(hfini)
    mfini=hf[1]
    mfn=int(mfini)
    if mfn <60:
        horafinalformat=horaini+ timedelta(hours=hfn,minutes=mfn)
        horafinformat=horafinalformat.strftime("%I:%M %p")
    
    else:
        sys.exit()
    #Diferencia en dias
    dini= horaini.strftime('%d')
    di=int(dini)
    difi=horafinalformat.strftime('%d')
    dfi=int(difi)
    difdia=dfi-di
    #Dias de la semana
    diaIni=horaini.strftime("%A")
    diaFin=horafinalformat.strftime("%A")
    #Resultado
    if (difdia==0 and dw==''):
        return print(horafinformat)
    elif (difdia==1 and dw==''):
        return print(horafinformat +' (next day)')
    elif (difdia>1 and dw==''):
        return print(horafinformat +' ('+str(difdia)+' days later)')    
    elif (difdia==0 and dw!=''):
        return print(horafinformat,', ',diaFin)
    elif (difdia==1 and dw!=''):
        print(horafinformat,', ',diaFin,' (next day)')
    elif (difdia>1 and dw!=''):
        print(horafinformat,', ',diaFin,' ( '+str(difdia)+' days later)')
#EjercicioClase
import requests,re,json
ipsAlmacenadas = []

def extractFromRegularExpresion(regex,data):
    if data:
      return re.findall(regex,data)
    return None

file=open(r"C:\Users\julid\Downloads\access.log\access.log")
for i in range(30):
    data = file.readline()
    regex=r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(\d{2}\/\b[a-zA-Z]{3}\b\/\d{4})\:(\d{2}\:\d{2}:\d{2})\s\+\d{4}\]\s\"(\b[a-zA-Z]{3,7}\b)"

    resultado = extractFromRegularExpresion(regex,data)
    for ip,fecha,hora,get in resultado:
     print(f"IP: {ip} Fecha: {fecha} Hora: {hora} MÉTODO: {get}")
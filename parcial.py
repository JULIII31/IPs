#parcial
import requests,re,json
ipsAlmacenadas = []

def extractFromRegularExpresion(regex,data):
    if data:
      return re.findall(regex,data)
    return None

data=open(r"C:\Users\julid\Downloads\access.log\access.log").read()
regex=r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[\d{2}\/\b[a-zA-Z]{3}\b\/\d{4}\:\d{2}\:\d{2}:\d{2}\s\+\d{4}\]\s\"\b[a-zA-Z]{3,7}\b\s\/\S+\sHTTP\/\d{1}\.\d{1}\"\s(\d{3})"

resultado = extractFromRegularExpresion(regex,data)
for i in range(2):
    if resultado[i][0] not in ipsAlmacenadas:
        otros = []
    for j in range(len(resultado)):
        if resultado[i][0]==resultado[j][0]:
            otros.append(f"{resultado[j][1]}")
    ipsAlmacenadas.append({resultado[i][0] : otros})
print(json.dumps(ipsAlmacenadas,indent=4))
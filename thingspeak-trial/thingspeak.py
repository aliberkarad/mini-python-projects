import urllib
deger=03.42
url_yazma="https://api.thingspeak.com/update?api_key=VMCEYLQG9HKKFDSA&field1="+str(deger)
connect1=urllib.request.urlopen(url_yazma)

url_okuma="https://api.thingspeak.com/channels/1131201/feeds.json?api_key=XH6JCOXRG3R24NYP&results=2"
connect2=urllib.request.urlopen(url_okuma)
okuma = connect2.read().decode("utf-8")
str(okuma)
sayi=okuma.rfind(":")
sayi += 2
okuma=okuma[sayi:-4]
print(okuma)
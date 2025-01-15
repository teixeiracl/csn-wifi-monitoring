#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Programa que filtra as informções provindas da coleta pelo site Carterpillar
import os
import glob
import csv
import pandas as pd

#Insira o caminho do diretório
#caminho_diretorio = "C:/Users/emanu/OneDrive/Documentos/IC/Final/Filtragem_Cater"
caminho_diretorio = "../GPS/"

# Obtém a lista de arquivos .log no diretório especificado
arquivos = glob.glob(os.path.join(caminho_diretorio, "172.23.72.134.log"))


fieldnames = ['IP','Data','Hora','Lat','Lon','Rssi','Ipv4Address']

Num_ip = []
Data =[]
Hora = []
Latitude = []
Longitude = []
rssis = []
Ipv4Address = []

# Loop através de cada arquivo
for arquivo in arquivos:
    with open(arquivo, 'r') as fin:
        for line in fin:
            line = line.strip()
           
            num_ip = line[0:13]
            data = line[14:24]
            hora = line[25:33]
            latitude = line[41:54]
            longitude = line[55:67]
            rssi = ""
            Ipv4Addres = ""
                
            Num_ip.append(num_ip)
            Data.append(data)
            Hora.append(hora)
            Latitude.append(latitude)
            Longitude.append(longitude)
            rssis.append(rssi)
            Ipv4Address.append(Ipv4Addres)
        

        #conteudo = file.read()
        #linhas = conteudo.split("\n")
        
        # Define o nome do arquivo CSV de saída
        nome_arquivo_csv = os.path.splitext(arquivo)[0] + ".csv"
        
        # Abre o arquivo CSV para escrita
        #with open(nome_arquivo_csv, 'w', newline='') as csv_file:
            #writer = csv.writer(csv_file)
            
            # Escreve cada linha no arquivo CSV
            #for linha in linhas:
                #writer.writerow([linha])
        
        
        with open(nome_arquivo_csv, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(Num_ip)):
                writer.writerow({'IP':Num_ip[i],'Data':Data[i],'Hora':Hora[i],'Lat':Latitude[i],'Lon':Longitude[i],'Rssi':rssis[i],'Ipv4Address':Ipv4Address[i]})
        
        print(f"Arquivo CSV salvo: {nome_arquivo_csv}")


# In[ ]:





import zipfile
import csv
import pandas as pd
import pandas
import MapaCalor
import Equipamentos as Data 
import CsvReader  
import csvToApi
#ipRadio = "125"
#ipGps = "234"
#euipamentoMap = Data.nomeMap
path_ip  = '../logs/2023-11-22/'
path_gps = '../logs/2023-11-22/GPS/'    
path_out ='../dados2/2023-11-22/'    
ipsCoordenadasProcessadas = list()

def hasGPSFile(ip):
    ipGps = Data.ipMap[ip]
    try:
        with open(path_gps+ipGps+'.log', 'r') as fin:
            return 1
    except:
        return 0
#Intervalo horário
#h1 = "10:00"
#h2 = "11:00"
coordAll = dict()
ipsComGpsERadio = set()
def getCoordenadas(ip,horario:Data.Horario,lat,lon):
    if(lat!=0.0 and lon !=0.0):
        ipsCoordenadasProcessadas.append(ip)
        return Data.Coordenada(lat,lon)
    else:
        try:
            if(ip in ipsCoordenadasProcessadas):
                return coordAll[horario]
            else: 
                ipsCoordenadasProcessadas.append(ip)
                ipGps = Data.ipMap[ip]
                file = path_gps+ipGps+'.log'
                f = open(file, "r")
                lines = f.read().split("\n") # "\r\n" if needed
                for line in lines:
                    if (line != "" and 'Erro' not in line 
                        and 'Not Found' not in line 
                        and '0.000000000' not in line) : # add other needed checks to skip titles
                            ipsComGpsERadio.add(ip)
                            cols = line.split(";")
                            num_ip = cols[0]
                            try: #check if is a valid latitude
                                horario = cols[1][0:16]
                                lat = float(cols[2])
                                lon = float(cols[3])
                                coordenada = Data.Coordenada(lat,lon)
                                coordAll[horario] =  coordenada
                                #return coordenada
                                #print(str(data)+" "+str(hora)+" "+str(lat)+" "+str(lon))
                            except:
                                print("Erro ao processar coordendada:\n"+line)
                                return 0
                #print (cols)
                """
                with open(path_gps+ipGps+'.log', 'r') as fin:
                   for line in fin:
                       line = line.strip()
                       num_ip = line[0:13]
                       data = line[15:29]
                       latitude = line[40:52]
                       longitude = line[54:65]
                       try: #check if is a valid latitude
                            lat = float(latitude)
                            lon = float(longitude)
                            if(lat!=0.0 and lon != 0.0): 
                                coordenada = Data.Coordenada(lat,lon)
                                coordAll[data] =  coordenada
                       except:
                           continue
                """
                #print (coordAll)
                return coordAll[horario]
        except:
            return 0
        

def get_substring(input_string, delim, nth, delims):
    # Recupera o índice de n-ésimo delim 
    idx_nth = idx_delims[nth-1]
    #print (idx_nth)
    # Encontra o índice do enésimo + 1 delim
    idx_nth_p1 = input_string.index(delim, idx_nth+1)
    # Retorna a substring entre essas duas posições
    return input_string[idx_nth+1:idx_nth_p1]

def convertLat(lat):
    degree_Lat  = (lat[:2])
    minutes_Lat = (lat[2:4])
    sec_Lat     = (lat[4:9])
    degree_Lat = pd.to_numeric(degree_Lat, errors='coerce')
    minutes_Lat = pd.to_numeric(minutes_Lat, errors='coerce')
    sec_Lat = pd.to_numeric(sec_Lat, errors='coerce')
    lat_dd = -(degree_Lat + (minutes_Lat/60)+((sec_Lat*60)/3600))
    return lat_dd

def convertLon(lon):
    degree_Lon  = (lon[1:3])
    minutes_Lon = (lon[3:5])
    sec_Lon     = (lon[5:10])
    degree_Lon = pd.to_numeric(degree_Lon, errors='coerce')
    minutes_Lon = pd.to_numeric(minutes_Lon, errors='coerce')
    sec_Lon = pd.to_numeric(sec_Lon, errors='coerce')
    lon_dd = -(degree_Lon + (minutes_Lon/60)+((sec_Lon*60)/3600))
    return lon_dd
def geraPontoMapaCalor(horarioFoco:Data.Horario,logRadio:Data.LogRadio):
        print("Horário mudou")
        if(logRadio.coordenada == None):
           print("Erro: coordenada vazia")
           return 
        pontoMapaCalor = Data.MapaCalorPonto(logRadio.coordenada,
                                             logRadio.horario,
                                             logRadio.getMelhorRssi(),
                                             logRadio.bestRssiParName,
                                             logRadio.getMelhorCusto(),
                                             logRadio.bestCustoParName)
        try:
            #mapaCalorEquipamentoDaHora[data+"-"+hora].append(ponto)
            mapaCalorEquipamentoDaHora[horarioFoco.toString()].append(pontoMapaCalor)
        except:
            mapaCalorEquipamentoDaHora[horarioFoco.toString()] = list()
            mapaCalorEquipamentoDaHora[horarioFoco.toString()].append(pontoMapaCalor) 
        finally:
            logRadio = Data.LogRadio()
            horarioFoco = horario

coordenadasRadio = dict()
#for k,v in ipMap.items()
#    coordenadasRadio[k]=getCoordenadas(k)
    #print(coordenadasRadio)

delims = [';']

mapaCalorEquipamentoDaHora = dict()
ipsSemDadosCoordenada = set()
ipsSemDadosRadio = set([])
#def processaArquivo(k):
#ipMap["172.23.67.123"]="172.23.72.214"  #CM-7921
for ip,v in Data.ipMap.items():
#for x in range(1):
#    k =  "172.23.67.123"  #CM-7921
    print(ip)
    coordAll = dict()
#for k,v in equipamentoMap.items():

    #data,hora,lat,lon,alt,radio,custo,rssi,ipv4Address,ip,macsource,macdestination,action,enabled,rate,signal_ok,age,stats,encapId,txpower,version,linkLocalAddress
    fieldnames = ['data','hora','lat','lon','alt','radio','custo','rssi','ipv4Address','ip', 
                  'macsource','macdestination','action','enabled','rate','signal_ok','age','stats','encapId','txpower','version','linkLocalAddress']
#    fieldnames = ['IP','Data','Hora','Radio','Lat','Lon','Temperatura','Custo','Rssi','Ipv4Address','Equipamento-Par']
    #fieldnames = ['IP','Data','Hora','Radio','Lat','Lon','Alt','Temperatura','Rssi','Ipv4Address']

    horas = []
    datas = []
    ips = []
    lats = []
    lons = []
    alts = []
    radios = []
    #temperaturas = []
    custos = []
    rssis = []
    Ipv4Address = []
    macsource= []
    macdestination = []
    action = []
    enabled = []
    rate = []
    signal_ok = []
    age = []
    stats = []
    encapId = []
    txpower = []
    versions = []
    linkLocalAddress = []
    #equipamentos = []

    pares = list();
    horaAnterior = "XXXXX";
    dataAnterior = "XXXXX";
    rssiEquipamento=0;
    rssiAntena=0;

    mapaCalorAntenaDaHora= dict()
    mapaCalorEquipamento = dict()
    mapaCalorAntena= dict()
    horaDaHora=''
    dataDaHora=''
    latDaHora=0
    lonDaHora=0
    rssiDaHora=-200
    equipamentoOrigemDaHora = ""
    equipamentoDestinoDaHora = ""
    pontosDaHora=[]
    
    #try:
    if(1):
        try:
            lines = CsvReader.getLines(path_ip,ip)
            horarioFoco=Data.Horario(lines[0][0:10],lines[0][11:16])
            logRadio = Data.LogRadio()
        except:
            continue
        for line in lines:
            if('Logging' not in line and 'Stopping receiver' not in line and len(line)>200):
                cols = line.split(';')
                data = cols[0][0:10]
                hora = cols[0][11:16]
                if(horarioFoco.mudou(data,hora)==1): # mudou horário do log
                    geraPontoMapaCalor(horarioFoco,logRadio)
                    horarioFoco = Data.Horario(data,hora)
                else:
                    print("Horário não mudou"+data+" "+hora)        
                horario = Data.Horario(data,hora)
                temperatura=cols[2]
                modeloRadio=cols[3]
                version=cols[8]
                ip = cols[13]
                if('W' in line and 'S' in line): # Rádio da Rajant tem seu próprio GPS
                    ipPar = cols[34] 
                    rssi = int(cols[40])  
                    custo = int(cols[43]) 
                    lat = convertLat(cols[29])   
                    lon = convertLon(cols[30]) 
                else:  # Coordena deve ser pega via GPS da Caterpilar 
                    ipPar = cols[31] 
                    rssi = int(cols[37])  
                    custo = int(cols[40]) 
                    lat =  0.0   
                    lon =  0.0   
                coordenada = getCoordenadas(ip,horario,lat,lon)
                if(coordenada == 0 or coordenada == None):
                    continue
                logRadio.addCoordenada(coordenada)
                equipamento = Data.Equipamento(ip,modeloRadio)
                logRadio.setHorario(horario)
                logRadio.setEquipamento(equipamento)
                logRadio.setTemperatura(temperatura)
                destino = Data.Equipamento(ipPar,modeloRadio)
                par = Data.Par(equipamento,destino,rssi,custo,horario)
                logRadio.addPar(par)
                horas.append(hora)
                datas.append(data)
                lats.append(lat)
                lons.append(lon)
                alts.append(100) #TODO ver como ler a altitude corretamente
                radios.append(modeloRadio)
                #temperaturas.append(temperatura)
                custos.append(custo)
                rssis.append(rssi)
                ips.append(par.getDestino().ipRadio) # na API do Rone ficou trocado origem x destino 
                Ipv4Address.append(ip)
                #equipamentos.append(par.getDestino().nome)
                macsource.append(" ")
                macdestination.append(" ")
                action.append(0)
                enabled.append(1)
                rate.append(0)
                signal_ok.append(0)
                age.append(0)
                stats.append(0)
                encapId.append(0)
                txpower.append(0)
                versions.append(version)
                linkLocalAddress.append(" ")
                horaAnterior = hora;
                dataAnterior = data;

        geraPontoMapaCalor(horarioFoco,logRadio)
        """ 
        with open(path_ip+k+'.log', 'r') as fin:
          for line in fin:
              line = line.strip()
              #print(str(len(line))+line)
              if len(line) > 300:            
                  # Índices de todas as ocorrências de delims 
                  idx_delims = [i for i, x in enumerate(line) if x in delims]
                  #print (len(idx_delims))
                  hora = line[11:16]
                  data = line[0:10]
                  horario = Data.Horario(data,hora)
                  ip = get_substring(line, ';', 13, delims)
                  temperatura = get_substring(line, ';', 2, delims)
                  modeloRadio = get_substring(line, ';', 3, delims)
                  equipamento = Data.Equipamento(ip,modeloRadio)
                  logRadio = Data.LogRadio(horario,equipamento,temperatura)
                  coordenada = Data.Coordenada()
                  if(len(idx_delims)>43):
                      lat = convertLat(get_substring(line, ';',29, delims))
                      lon = convertLon(get_substring(line, ';', 30, delims))
                      alt = get_substring(line, ';', 31, delims)
                      coordenada = Data.Coordenada(lat,lon,alt)
                      logRadio.setCoordenada(coordenada)
                      cost = get_substring(line, ';', 43, delims)
                      rssi = get_substring(line, ';', 40, delims)
                      ip_conectado = get_substring(line, ';', 34, delims)
                      destino = Data.Equipamento(ip_conectado)
                      par = Data.Par(equipamento,destino,rssi,cost)
                      logRadio.addPar(par)
                  else:
                    if(getCoordenadas(ip)==1):
                        try:
                            coordenada = coordAll[data+" "+hora]
                        except:
                            #print('Coordenada GPS não encontrada')
                            continue
                        cost = get_substring(line, ';', 41, delims)
                        rssi = get_substring(line, ';', 38, delims)
                        ip_conectado = get_substring(line, ';', 42, delims)
                        destino = Data.Equipamento(ip_conectado)
                        par = Data.Par(equipamento,destino,rssi,cost)
                        logRadio.addPar(par)
                    else:
                        ipsSemDadosCoordenada.add(k) 
                        break # pára a análise se não tiver coordenadas:6
                  if(horario.mudou(data,hora)==1): # mudou horário do log
                      pontoMapaCalor = Data.MapaCalorPonto(logRadio.coordenada,
                                                           logRadio.horario,
                                                           logRadio.getMelhorRssi,
                                                           logRadio.getMelhorCusto)
                      try:
                        #mapaCalorEquipamentoDaHora[data+"-"+hora].append(ponto)
                        mapaCalorEquipamentoDaHora[horario.toString()].append(pontoMapaCalor)
                      except:
                        mapaCalorEquipamentoDaHora[horario.toString()] = list()
                        mapaCalorEquipamentoDaHora[horario.toString()].append(pontoMapaCalor) 
                  horas.append(hora)
                  datas.append(data)
                  ips.append(ip)
                  lats.append(lat)
                  lons.append(lon)
                  alts.append(alt)
                  radios.append(radio)
                  temperaturas.append(temperatura)
                  custos.append(cost)
                  rssis.append(rssi)
                  Ipv4Address.append(ip_conectado)
                  equipamentos.append(equipamento)
                  horaAnterior = hora;
                  dataAnterior = data;
       #print (pares)
       #par["172.23.67.197"]
        """
        
        file1 =  path_out + Data.nomeMap[ip] + '.csv'
        #print(file1)
        if(len(ips)>0):
            with open(file1, 'w') as csvfile:
              writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
              writer.writeheader()
              for i in range(len(ips)):
#    fieldnames = ['data','hora','lat','lon','alt','radio','custo','rssi','ipv4Address','ip', 
#                  'macsource','macdestination','action','enabled','rate','signal_ok','age','stats','encapId','txpower','version','linkLocalAddress']
                  writer.writerow({
                                   'data':datas[i],
                                   'hora':horas[i],
                                   'lat':lats[i],
                                   'lon':lons[i],
                                   'alt':alts[i],
                                   'radio':radios[i],
                                   'custo':custos[i],
                                   'rssi':rssis[i],
                                   'ipv4Address':Ipv4Address[i],
                                   'ip':ips[i],
                                   'macsource':macsource[i],
                                   'macdestination':macdestination[i],
                                   'action':action[i],
                                   'enabled':enabled[i],
                                   'rate':rate[i],
                                   'signal_ok':signal_ok[i],
                                   'age':age[i],
                                   'stats':stats[i],
                                   'encapId':encapId[i],
                                   'txpower':txpower[i],
                                   'version':versions[i],
                                   'linkLocalAddress':linkLocalAddress[i]
#                                  'temperatura':temperaturas[i],
#                                  'equipamento-Par':equipamentos[i]
                   })
            
    #except:
    #   print('File Not Found' + path_ip+ip+'.log')
    #   ipsSemDadosRadio.add(ip)
        
print('Ips sem Dados de Rádio')
print(ipsSemDadosRadio)
print('Ips sem Dados de GPS')        
print(ipsSemDadosCoordenada)        
print('Ips Dados de Rádio e GPS')        
print (ipsComGpsERadio)
for k in ipsComGpsERadio:
    print (k + " " +  Data.ipMap[k])      
fieldnames=['lat','lon','rssi','equipamento-origem','equipamento-destino','data hora']
for k,v in mapaCalorEquipamentoDaHora.items():
    #print(k)
    #print(v)
    MapaCalor.salvaMapaCalor(path_out,k,fieldnames,v)
#    processaArquivo(k)

csvToApi.loadToApi(path_out)
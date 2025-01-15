import csv
import Equipamentos
def salvaMapaCalor(path_out,filePrefix,fieldnames,mapaCalor:Equipamentos.MapaCalor):
    fieldnames=['Horario','Lat','Lon','Rssi','Custo','Equipamento Melhor RSSI','Equipamento Melhor Custo']
    #fieldnames=['Horario','Lat','Lon','Rssi','Custo']
    file2 = path_out+filePrefix+"-mapa-calor.csv"
    with open(file2, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        pontos = mapaCalor
        for i in range(len(pontos)):
              writer.writerow({'Horario':filePrefix,
                               'Lat':pontos[i].coordenada.lat,
                               'Lon':pontos[i].coordenada.lon,
                               'Rssi':pontos[i].rssi,
                               'Custo':pontos[i].custo,
                               'Equipamento Melhor RSSI':pontos[i].nomeParMelhorRssi,
                               'Equipamento Melhor Custo':pontos[i].nomeParMelhorCusto
                            })

#path_out = '../dados/2023-11-21/' 

#fieldnames=['Item','Lat','Lon','RSSI','Equipamento']
#mapaCalor = [
#           {'Item':1,'Lat':-20.468805903     ,'Lon':-43.91928963,      'RSSI':-53, 'Equipamento':'CM-7912'},
#           {'Item':1,'Lat':-20.47607833333333,'Lon':-43.91863333333333,'RSSI':-54, 'Equipamento':'PM-9906'},
#]
#salvaMapaCalor(path_out,fieldnames,mapaCalor)

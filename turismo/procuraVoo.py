import http.client , json
import psycopg2
from . import Voo

def buscaVoos(cidade_saida,pais_saida,cidade_entrada,pais_entrada,data):
    
    cidade_entrada = str(cidade_entrada)
    cidade_saida = str(cidade_saida)
    pais_saida = str(pais_saida)
    pais_entrada = str(pais_entrada)
    data = str(data)
    idsaida = "a"
    identrada = "a"

    con = psycopg2.connect(host='trabagenciaviagem.cxr1ekmvfm4k.sa-east-1.rds.amazonaws.com', port=5432, timeout=None, database="postgres", user="DSID2020",password="AdamSandler")

    cur=con.cursor()
    
    Voo.buscaCidadeAeroporto(str.lower(cidade_saida))
    Voo.buscaCidadeAeroporto(str.lower(cidade_entrada))

    cur.execute("SELECT id FROM aeroportos WHERE nomeaeroporto =%s and pais =%s",(cidade_saida,pais_saida))
    idsaida = str(cur.fetchone()[0])
    
    cur.execute("SELECT id FROM aeroportos WHERE nomeaeroporto =%s and pais =%s",(cidade_entrada,pais_entrada))
    identrada = str(cur.fetchone()[0])
    
    conn = http.client.HTTPSConnection("skyscanner-skyscanner-flight-search-v1.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "b031d355c8msh02e887b2b3e5eecp1f8df2jsn06d7ba544170"
    }
    a = "/apiservices/browsequotes/v1.0/BR/BRL/pt-BR/"+idsaida+"/"+identrada+"/"+data
    conn.request("GET", a, headers=headers)

    res = conn.getresponse()
    data = res.read()
    Resposta = json.loads(data)
    NomeCompanhia = 'a'
    NomeEntrada= 'a'
    NomeSaida='a'
    idcompanhia = Resposta['Quotes'][0]['OutboundLeg']['CarrierIds'][0]
    i = len(Resposta['Carriers'])
    for b in range (0,i,+1):
        if(Resposta['Carriers'][b]['CarrierId']== idcompanhia):
            NomeCompanhia = Resposta['Carriers'][b]['Name']
    idsaida1 = Resposta['Quotes'][0]['OutboundLeg']['OriginId']
    identrada1 = Resposta['Quotes'][0]['OutboundLeg']['DestinationId']
    it = len(Resposta['Places'])
    for k in range(0,it,+1):
        if (Resposta['Places'][k]['PlaceId']==idsaida1):
            NomeSaida = Resposta['Places'][k]['Name']
        if (Resposta['Places'][k]['PlaceId']==identrada1):
            NomeEntrada = Resposta['Places'][k]['Name']
    precoapagar  = Resposta['Quotes'][0]['MinPrice']
    datavoo = identrada1 = Resposta['Quotes'][0]['OutboundLeg']['DepartureDate']
    jason = {'voo':[]}
    jason['voo'].append({'Origem':NomeSaida,'Destino':NomeEntrada,'Companhia Aerea':NomeCompanhia,'Preco':precoapagar,'Data':datavoo})
    python2json = json.dumps(jason)
    return python2json

import http.client
import json
from . import procuraCodCid

def achaHotel(cidade,adultos,noites,quartos,checkin,pais):

    codcidade = procuraCodCid.recebeCidade(cidade,pais)
    conn = http.client.HTTPSConnection("tripadvisor1.p.rapidapi.com")
    URL ="/hotels/list?offset=0&currency=BRL&limit=30&order=asc&lang=pt-BR&sort=recommended&location_id="+ codcidade+"&adults="+adultos+"&checkin="+checkin+"&rooms="+quartos+"&nights="+noites
    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "793e2b63bdmsh960472bc7b849ddp102d4bjsn03173d2e47e1"
        }

    conn.request("GET", URL, headers=headers)

    res = conn.getresponse()
    data = res.read()
    Resposta = json.loads(data)

    i = len(Resposta['data'])
    b = {"hotel":[]}
    for a in range (0,i,+1):
       
        try: 
             nome = str(Resposta['data'][a]['name'])
             nota= str(Resposta['data'][a]['rating'])
             preco = str(Resposta['data'][a]['price'])
             b['hotel'].append({'nome':nome,'nota':nota,'preco':preco})
        except:
             pass
    python2json = json.dumps(b,ensure_ascii=False)
    return python2json


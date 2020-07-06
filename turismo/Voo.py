import http.client , json
import psycopg2


def buscaCidadeAeroporto(cidade):
#cidade = "londres"
    cidade = cidade.replace(" ","%20")
    cidade = cidade.replace("á","%25C3%25A1")
    cidade = cidade.replace("ã","%25C3%25A3")
    cidade = cidade.replace("é","%25C3%25A9")
    cidade = cidade.replace("ó","%25C3%25B3")
    cidade = cidade.replace("í","%25C3%25AD")
    cidade = cidade.replace("â","%25C3%25A2")
    cidade = cidade.replace("ê","%25C3%25AA")
    con = psycopg2.connect(host='trabagenciaviagem.cxr1ekmvfm4k.sa-east-1.rds.amazonaws.com', port=5432, timeout=None, database="postgres", user="DSID2020",password="AdamSandler")

    cur=con.cursor()

    conn = http.client.HTTPSConnection("skyscanner-skyscanner-flight-search-v1.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "793e2b63bdmsh960472bc7b849ddp102d4bjsn03173d2e47e1"
            }
    URL = "/apiservices/autosuggest/v1.0/BR/USD/pt-BR/?query="+ cidade

    conn.request("GET",URL,headers=headers)


    res = conn.getresponse()
    data = res.read()

    Resposta = json.loads(data)

    i = len(Resposta['Places'])

    for a in range(0, i, +1):
        id = str.lower(Resposta['Places'][a]['PlaceId'])
        NomeAeroporto = str.lower(Resposta['Places'][a]['PlaceName'])
        pais = str.lower(Resposta['Places'][a]['CountryName'])
        try:
            cur.execute("insert into public.aeroportos (id,nomeaeroporto,pais) values (%s,%s,%s)",(id,NomeAeroporto,pais))
        except psycopg2.IntegrityError:
            con.rollback()
        else:
            con.commit()
    con.close()

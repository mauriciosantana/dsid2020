import psycopg2
import http.client,json
def procuraIdCidade(cidade):
    con = psycopg2.connect(host='trabagenciaviagem.cxr1ekmvfm4k.sa-east-1.rds.amazonaws.com', port=5432, timeout=None, database="postgres", user="DSID2020",password="AdamSandler")

    cur=con.cursor()
    conn = http.client.HTTPSConnection("tripadvisor1.p.rapidapi.com")

#cidade = "londres "
    cidade = cidade.replace(" ","%20")
    cidade = cidade.replace("á","%25C3%25A1")
    cidade = cidade.replace("ã","%25C3%25A3")
    cidade = cidade.replace("é","%25C3%25A9")
    cidade = cidade.replace("ó","%25C3%25B3")
    cidade = cidade.replace("í","%25C3%25AD")
    cidade = cidade.replace("â","%25C3%25A2")
    cidade = cidade.replace("ê","%25C3%25AA")
    URL = "/locations/search?location_id=1&limit=30&sort=relevance&offset=0&lang=pt-BR&currency=BRL&units=km&query=" + cidade

    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "793e2b63bdmsh960472bc7b849ddp102d4bjsn03173d2e47e1"
        }

    conn.request("GET",URL,headers=headers)

    res = conn.getresponse()
    data = res.read()
    Resposta = json.loads(data)

    d = len(Resposta['data'])
    for j in range (0,d,+1):
        if (Resposta['data'][j]['result_type'] == "geos"):
            id = str.lower(Resposta['data'][j]['result_object']['location_id'])
            nome   = str.lower(Resposta['data'][j]['result_object']['name'])
            i = len(Resposta['data'][j]['result_object']['ancestors'])
            for a in range (0,i,+1):
                b= str.lower(Resposta['data'][j]['result_object']['ancestors'][a]['subcategory'][0]['key']) 
                if (b == 'country'):
                    pais  = str.lower(Resposta['data'][j]['result_object']['ancestors'][a]['name'])

            try:
                cur.execute("insert into public.cidade (locationid,nome,pais) values (%s,%s,%s)",(id,nome,pais))       
            except:
                con.rollback()
        

    con.commit()
    con.close()
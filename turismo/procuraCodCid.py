import psycopg2
from . import cidade
def recebeCidade(nomeCidade,pais):
    nomeCidade = str.lower(nomeCidade)
    pais = str.lower(pais)
    
    con = psycopg2.connect(host='trabagenciaviagem.cxr1ekmvfm4k.sa-east-1.rds.amazonaws.com', port=5432, timeout=None, database="postgres", user="DSID2020",password="AdamSandler")

    cur=con.cursor()

    id ='batata'
    cur.execute("SELECT locationid FROM cidade WHERE nome =%s and pais =%s",(nomeCidade,pais))
    try: 
        id=cur.fetchone()[0]
        return str(id)
    except :
        cidade.procuraIdCidade(nomeCidade)
            
        cur.execute("SELECT locationid FROM cidade WHERE nome =%s and pais =%s",(nomeCidade,pais))
        idd= cur.fetchone()[0]
        return str(idd)

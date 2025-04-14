from database.DB_connect import DBConnect
from model.situazione import Situazione

''' note per il database: il database è "sporco", ad esempio, nel mese di gennaio manca
    il dato per il primo giorno. Devo scrivere il codice in funzione delle possibili
    complicazioni che possono accadere nei diversi database, es dati corrotti, linee non
    leggibili. Sarebbe utile impostare una linea di default per superare questi errori
'''
class MeteoDao():

    @staticmethod
    def get_all_situazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s 
                        ORDER BY s.Data ASC"""
            cursor.execute(query)
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result



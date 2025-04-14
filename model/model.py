

from database.meteo_dao import MeteoDao
class Model:
    def __init__(self):
        pass
    def calcola_sequenza(self, mese):
        situazioni = MeteoDao.get_situazioni_meta_mese(mese)

    #parte di soluzione con la ricorsione!
    def _ricorsione(self, parziale, liata_situazioni):

        #condizione terminale
        # NB la lunghezza del parziale indica il giorno di cui cerco le soulzioni.

        if (len(parziale))==15:
            print(parziale)

        #condizione ricorsiva
        else:
            #devo cercare le città per il girno che mi serve
            #provo ad aggiungere una di queste citta e vado avanti.

            '''
            [1:MILANO][2]
            [][][][][][][][] ... [] : 44 dati
            '''
            #candidati=trova_possibili_step(self, parziale, liata_situazioni)

            for candidato in candidati:
                parziale.append(candidato)
                self._ricorsione(parziale,liata_situazioni)
                parziale.pop()
                #nota bene, dato che ogni giorno ha un numero limite di soluzioni (es il giorno uno
                #una sola e così via, posso fare dei check per limitare le iterazioni!

#per usare la ricorsione, tengo un codice in ricorsione pulito, e imposto all'esterno i vincoli!

#esempio di vincolo:
#[T][T][T][M][M][M][M][G][G][G]
"""se gli ultimi tre non sono uguali, il prossimo step dell'algoritmo deve inserire per forza
    una città uguale all'ultima soluzione,
    Osservazione: in pratica devo generare tutte le sequenze di viaggio ammissibili, escludendo quelle
    impossibili per limitare le iterazioni con i vincoli assegnati.
    In seguito, calcolo il costo per ogni sequenza per trovare la sequenza ottima.
"""
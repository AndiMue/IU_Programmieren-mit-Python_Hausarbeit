from Lib.Data_import import DataToImport
import sqlalchemy as sql
from Lib.DataWriteToDB import DataToDatabase
import os


def extract_tablename(path):
    result = os.path.basename(path)
    result = result[:-4]
    return result


DataBaseName = "T2.db"

engine = sql.create_engine("sqlite+pysqlite:///" + DataBaseName, echo=True)
connection = engine.connect()

DI = DataToImport()
DW = DataToDatabase()
print("TEST.csv")
DI.importieren("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\test.csv")
Tablename = extract_tablename("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\test.csv")
DW.create_table(Tablename, DI, connection)
DW.data_to_table(Tablename, DI, connection)
del DI

DI = DataToImport()
DI.importieren("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\train.csv")
Tablename = extract_tablename("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\train.csv")
DW.create_table(Tablename, DI, connection)
DW.data_to_table(Tablename, DI, connection)
del DI

DI = DataToImport()
print("IDEAL.csv")
DI.importieren("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\ideal.csv")
Tablename = extract_tablename("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\ideal.csv")
DW.create_table(Tablename, DI, connection)
DW.data_to_table(Tablename, DI, connection)
del DI

print("DONE")

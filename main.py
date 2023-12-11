from Lib.Data_import import DataToImport
import sqlalchemy as sql
from Lib.DataWriteToDB import DataToDatabase
import os
from Lib.Search_Function import lookupthings


def extract_tablename(path):
    result = os.path.basename(path)
    result = result[:-4]
    return result


DataBaseName = "T3.db"

engine = sql.create_engine("sqlite+pysqlite:///" + DataBaseName, echo=True)
connection = engine.connect()

train_data = DataToImport()
ideal_data = DataToDatabase()

''' ideal.csv importieren und in DB bringen'''

print("IDEAL.csv")
ideal_data.importieren("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\ideal.csv")
Tablename = extract_tablename("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\ideal.csv")
ideal_data.create_table(Tablename, ideal_data, connection)
ideal_data.data_to_table(Tablename, ideal_data, connection)
# del ideal_data

''' Trainingsdaten importieren und in DB bringen'''
train_data.importieren("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\train.csv")
Tablename = extract_tablename("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\train.csv")
train_data_to_DB = DataToDatabase()
train_data_to_DB.create_table(Tablename, train_data, connection)
train_data_to_DB.data_to_table(Tablename, train_data, connection)


''' Trainingsdaten in ideal.csv suchen '''

ideal_4_data = lookupthings()
ideal_4_data.lookup_train_in_ideal(train_data, ideal_data)
ideal_4_data_to_DB = DataToDatabase()
ideal_4_data_to_DB.create_table_id4('four_of_ideal', ideal_4_data, connection)  # eigtl nicht nötig
ideal_4_data_to_DB.data_to_table_id4('four_of_ideal', ideal_4_data, connection)     # eigtl nicht nötig


''' Testdaten importieren um mit idealen 4 zu vergleichen'''
test_data = DataToImport()
test_data_to_DB = DataToDatabase()
test_data_compare = lookupthings()
''' import und Weiterverarbeitung mit Kind-Klasse '''
test_data_to_DB.importieren("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\test.csv")
Tablename = extract_tablename("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\test.csv")
test_data_compare.lookup_train_in_ideal(test_data, ideal_4_data)

# test_data_to_DB.create_table(Tablename, test_data_to_DB, connection)
# test_data_to_DB.data_to_table(Tablename, test_data_to_DB, connection)
del test_data

''' import und Weiterverarbeitung mit Eltern-Klasse '''
DI = DataToImport()
DI.importieren("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\train.csv")
Tablename = extract_tablename("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\train.csv")
# DW.create_table(Tablename, DI, connection)
# DW.data_to_table(Tablename, DI, connection)
del DI

DI = DataToImport()
print("IDEAL.csv")
DI.importieren("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\ideal.csv")
Tablename = extract_tablename("C:\\_Data\\IU_Python-Kurs\\Git_Repos\\Beispiel-Datensaetze\\ideal.csv")
# DW.create_table(Tablename, DI, connection)
# DW.data_to_table(Tablename, DI, connection)
del DI

print("DONE")

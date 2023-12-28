# Hausarbeit IU Akademie Programmieren mit Python

# Benötigte Importe
from Lib.Data_import import DataToImport
import sqlalchemy as sql
from Lib.DataWriteToDB import DataToDatabase
import os
from Lib.Search_Function import lookupthings
from Lib.Visualize import ShowInPlot


def extract_tablename(path):
    result = os.path.basename(path)
    result = result[:-4]
    return result


DataBaseName = "IU_Hausarbeit.db"

engine = sql.create_engine("sqlite+pysqlite:///" + DataBaseName, echo=True)
connection = engine.connect()

train_data = DataToImport()
ideal_data = DataToDatabase()

''' ideal.csv importieren und in DB bringen'''
ideal_data.importieren("ideal.csv")
Tablename = extract_tablename("ideal.csv")
ideal_data.create_table(Tablename, ideal_data, connection)
ideal_data.data_to_table(Tablename, ideal_data, connection)

''' Trainingsdaten importieren und in DB bringen'''
train_data.importieren("train.csv")
Tablename = extract_tablename("train.csv")
train_data_to_DB = DataToDatabase()
train_data_to_DB.create_table(Tablename, train_data, connection)
train_data_to_DB.data_to_table(Tablename, train_data, connection)

''' Trainingsdaten in ideal.csv suchen '''
ideal_4_data = lookupthings()
ideal_4_data.lookup_train_in_ideal(train_data, ideal_data)
ideal_4_data_to_DB = DataToDatabase()
ideal_4_data_to_DB.create_table('four_of_ideal', ideal_4_data, connection)  # eigtl nicht nötig
ideal_4_data_to_DB.data_to_table('four_of_ideal', ideal_4_data, connection)     # eigtl nicht nötig


''' Testdaten importieren um mit idealen 4 zu vergleichen'''
test_data_to_DB = DataToDatabase()
test_data_compare = lookupthings()
''' import und Weiterverarbeitung mit Kind-Klasse '''
test_data_to_DB.importieren("test.csv")
Tablename = extract_tablename("test.csv")

test_data_compare.lookup_test_in_ideal4(test_data_to_DB, ideal_4_data)
test_data_to_DB.create_table(Tablename, test_data_compare, connection)
test_data_to_DB.data_to_table(Tablename, test_data_compare, connection)

ShowData = ShowInPlot()
test_data_to_DB.y[0] = test_data_to_DB.x
train_data.y[0] = train_data.x
ShowData.show_id4_plus_test(ideal_4_data, test_data_to_DB, train_data, 'x', 'y', 'ideal 4 vs test Data')

print("Saved plotts to folder")
print("DONE")

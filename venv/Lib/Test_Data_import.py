import unittest
from Data_import import DataToImport
import os


class UnitTestImport(unittest.TestCase):
    def test_extract_tablename(self):
        ''' Rückgabewert des Dateinamens prüfen '''
        print("START TEST Tabellenname aus Pfad extrahieren")
        testpath = "C:\\Data\\Unterordner_1\\Unterordner_2\\Tabelle.csv"
        print("Testpfad: "+ testpath)
        result = DataToImport.extract_tablename(self, testpath)
        print("Extrahierter Name: " + result)
        self.assertEqual(result, 'Tabelle', "Der Dateiname ist Tabelle")
        print("Finish Test Tabellenname")


    def test_separate_lines(self):
        ''' Rückgabe Soll: zwei Werte x und y '''
        ''' Eingabe: ein zweispaltiger Wert und die Anzahl der Spalten '''
        print("START TEST Zeilen separieren")
        testvalue = [['x', 'y1', 'y2', 'y3'], [1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]]     # Wert zum "zerlegen"
        print("Testmatrix: " + str(testvalue))
        testspalten = 4
        testresult_1 = ['x', 1.0, 5.0, 9.0]
        testresult_2 = [[], ['y1', 2.0, 6.0, 10.0], ['y2', 3.0, 7.0, 11.0], ['y3', 4.0, 8.0, 12.0]]
        result1, result2 = DataToImport.separate_lines(self, testvalue, testspalten)
        print("Ergebnis 1: " + str(result1))
        print("Ergebnis 2: " + str(result2))
        self.assertEqual(result1, testresult_1, "Result 1 OK")
        self.assertEqual(result2, testresult_2, "Result 2 OK")
        print("Finish Test separieren")

'''
    def test_importieren(self):
        # Datei einlesen
        self.Anzahl_Spalten = 5
        file = "unittest.csv"
        testresult_0 = [['x', 'y1', 'y2', 'y3', 'y4'], [-20.0, 100, -19.7, 0.3, 11.7], [-19.9, 99, -19.7, 0.6, 11.7], [-19.8, 98, -19.5, 0.1, 11.4], [-19.7, 97, -19.8, 0.7, 11.8], [-19.6, 96, -19.8, 0.2, 11.8]]
        testresult_1 = ['x', -20.0, -19.9, -19.8, -19.7, -19.6]
        testresult_2 = [[], ['y1', 100, 99, 98, 97, 96],['y2', -19.7, -19.7, -19.5, -19.8, -19.8], ['y3', 0.3, 0.6, 0.1, 0.7, 0.2], ['y4', 11.7, 11.7, 11.4, 11.8, 11.8]]
        result = DataToImport.importieren(self, file)

        pass
'''

    #def extract_tablename(self, path):
    #    """
    #    Funktion extrahiert den Dateinamen aus demDateipfad
    #    :param path: Dateipfad
    #    :return: result: Dateiname
    #    """
    #    result = os.path.basename(path)
    #    result = result[:-4]
    #    return result

if __name__ == '__main__':
    unittest.main()
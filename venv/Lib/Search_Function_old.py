    def lookup_test_in_ideal4(self, source, destination):
        """
        testdaten mit den 4 gefundenen idealen Funktionen vergleichen
        :param source: testdaten
        :param destination: 4 ideale funktionen
        """
        self.x = []
        self.y = [[], [], [], []]
        # Ueberschriften anlegen
        self.y[0].append('x')
        self.y[1].append('y')
        self.y[2].append('Differenz')
        self.y[3].append('QuellFunktion')
        found = False

        # lenFileContent = len(source.file_content)
        for i in range(len(source.file_content)):
            xTest = source.file_content[i][0]   # x Wert suchen

            # lenDestY0 = len(destination.y[0])
            for j in range(1, len(destination.y[0])):
                xDest = destination.y[0][j]
                found = False
                if destination.y[0][j] == xTest:
                    # berechne Differenz
                    # index = destination.y[0][j].index()
                    for z in range(1, len(destination.y)):  # für alle y se in y bei x
                        yDest = destination.y[z][j]
                        yTest = source.file_content[i][1]
                        middleValue = (destination.y[z][j] + source.file_content[i][1]) / 2.0
                        difference = math.sqrt(0.5 * ((source.file_content[i][1] - middleValue) ** 2 + (destination.y[z][j] - middleValue) ** 2))  # quadr. mittlere Abweichung
                        if difference < self.criterion_Test_in_ideal4:
                            self.y[0].append(xTest)
                            self.y[1].append(yTest)
                            self.y[2].append(difference)
                            self.y[3].append(destination.y[z][0])
                            found = True
                        elif found == False and z == len(destination.y)-1:
                            self.y[0].append(xTest)
                            self.y[1].append('no')
                            self.y[2].append('Match')
                            self.y[3].append('found')
                            pass
                    pass
                else:
                    print("else Pfad")
                    if xDest > xTest:
                        break       # Schleife beenden, wenn x aus Destination > als x aus Testdaten, da Daten sortiert sind
                    pass
                pass
        self.x = self.y[0]
        self.Anzahl_Spalten = len(self.y)
        print("DONE test in ideal 4")
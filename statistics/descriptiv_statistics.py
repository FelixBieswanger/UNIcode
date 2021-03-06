import math

class Desc_stat:
    def __init__(self, array):
        self.data = array
        self.leng = len(array)
        self.mittelwert = self.calc_mittelwert()
        self.varianz = self.calc_varianz()
        self.standardabweichung = self.calc_standardabweichung()
        self.norm_standardabweichung = self.calc_norm_stand()

    def print(self):
        print("=====")
        print("mittel", self.mittelwert)
        print("mittel_relativ",self.calc_mittelwert_rel())
        print("varianz", self.varianz)
        print("stand", self.standardabweichung)
        print("norm_stand", self.norm_standardabweichung)
        print()
        print()
        print()

    def calc_mittelwert(self):
        sum = 0
        for el in self.data:
            sum += el
        return sum/self.leng

    def absolute_frequenzy(self,a):
        return self.data.count(a)

    def relativ_frequenzy(self,a):
        return self.absolute_frequenzy(a)/self.leng
        
    def calc_mittelwert_rel(self):
        mittel = 0
        for a in self.data:
            mittel += (a * self.relativ_frequenzy(a)) 
        return mittel

    def calc_varianz(self):
        abweich = 0
        for el in self.data:
            abweich += math.pow(abs(el-self.mittelwert), 2)

        return abweich/(self.leng-1)

    def calc_standardabweichung(self):
        return math.sqrt(self.varianz)

    def calc_norm_stand(self):
        return self.standardabweichung / self.mittelwert


a = [[1, 2, 3], [99, 100, 101], [50, 100, 150], [1, 100, 199]]


for el in a: 
    obj = Desc_stat(el)
    obj.print()
    

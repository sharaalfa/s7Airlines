import os

# interim calculations function of projects
class Determinator:

    def createTemporaryFile(self, col):
        self.column= col

        try:
            os.remove('temporary.csv')
        except:
            pass

        with open('temporary.csv', 'a') as f:
            f.write(self.column)


    def maxAndMin(self, n, y):
        self.value = n
        self.text=y
        print "max " + self.text, "= ",\
            str(max(self.value)), "\n",\
            "min " + self.text, "= ", str(min(self.value))

    def writeToFile(self, ctg):
        self.value=ctg
        f = open('temporary.csv', 'a')
        f.write('\n' + str(self.value))
        f.close()


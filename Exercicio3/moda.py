import statistics

empresa1 = [1000,6000,1200,8000,1400]

empresa2 = [5000,4000,3000,2000,7000]

empresa3 = [1200,1300,8000,3000,15000]

empresa4 = [1400,1750,2000,4500,5900,7000]

empresa5 = [1400,1750,2000,4500,5900,7000]

def moda():
    moda_empresa1 = statistics.mode(empresa1)
    print ("Moda empresa1:", moda_empresa1)

def moda(empresa2):
    moda_empresa2 = statistics.mode(empresa2)
    print ("Moda empresa2:", moda_empresa2)

def moda(empresa3):
    moda_empresa3 = statistics.mode(empresa3)
    print ("Moda empresa3:", moda_empresa3)

def moda(empresa4):
    moda_empresa4 = statistics.mode(empresa4)
    print ("Moda empresa4:", moda_empresa4)

def moda(empresa5):
    moda_empresa5 = statistics.mode(empresa5)
    print ("Moda empresa5:", moda_empresa5)

moda(empresa3)
moda(empresa4)
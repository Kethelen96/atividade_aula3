import statistics
empresa1 = [1000,6000,1200,8000,1400]

empresa2 = [5000,4000,3000,2000,7000]

empresa3 = [1200,1300,8000,3000,15000]

empresa4 = [1400,1750,2000,4500,5900,7000]

empresa5 = [1400,1750,2000,4500,5900,7000]


def desvio(empresa1):
    desvio_empresa1 = statistics.stdev(empresa1)
    print ("Desvio Padrão $ empresa1:" , desvio_empresa1)

def desvio(empresa2):
    desvio_empresa2 = statistics.stdev(empresa2)
    print ("Desvio Padrão $ empresa2:" , desvio_empresa2)

def desvio(empresa3):
    desvio_empresa3 = statistics.stdev(empresa3)
    print ("Desvio Padrão $ empresa3:" , desvio_empresa3)

def desvio(empresa4):
    desvio_empresa4 = statistics.stdev(empresa4)
    print ("Desvio Padrão $ empresa4:" , desvio_empresa4)

def desvio(empresa5):
    desvio_empresa5 = statistics.stdev(empresa5)
    print ("Desvio Padrão $ empresa5:" , desvio_empresa5)
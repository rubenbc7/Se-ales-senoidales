import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import CosSignal
from thinkdsp import decorate

#Módulo para graficar
import matplotlib.pyplot as plt

#Crear señal senoidal
seno = SinSignal(freq=329.628, amp=50,offset=0)
coseno = CosSignal(freq=41.2035,amp=30,offset=0)

#Crear gráfica en memoria y damos propiedades
seno.plot()
decorate(xlabel='Tiempo (s)')
decorate(ylabel='Amplitud')

coseno.plot()

plt.show()
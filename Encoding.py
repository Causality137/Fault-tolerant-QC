!pip install qiskit[visualization]==1.0.2
!pip install qiskit_aer
!pip install qiskit_ibm_runtime
!pip install matplotlib
!pip install pylatexenc
!pip install qiskit-transpiler-service

import numpy as np
from typing import List, Callable
from scipy.optimize import minimize
from scipy.optimize._optimize import OptimizeResult
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler

"""# Steane code encoding"""

qc = QuantumCircuit(7)
qc.draw('mpl')

qc.h(0)
qc.draw('mpl')

qc.h(1)
qc.draw('mpl')

qc.cx(0, 2)
qc.cx(1, 2)
qc.draw('mpl')

qc.h(3)
qc.draw('mpl')

qc.cx(3, 4)
qc.draw('mpl')

qc.cx(3, 5)
qc.cx(1, 5)
qc.draw('mpl')

qc.cx(3, 6)
qc.cx(1, 6)
qc.cx(0, 6)
qc.draw('mpl')

qc.barrier()
qc.draw('mpl')

def Steane(qc):
  qc.h(0)
  qc.h(1)
  qc.cx(0, 2)
  qc.cx(1, 2)
  qc.h(3)
  qc.cx(3, 4)
  qc.cx(3, 5)
  qc.cx(1, 5)
  qc.cx(3, 6)
  qc.cx(1, 6)
  return qc

"""# Stabilizer measurement to check any errors"""

q = QuantumRegister(13)
c = ClassicalRegister(6)
qc = QuantumCircuit(q, c)
qc = Steane(qc)
for i in range(7, 13):
  qc.h(i)
qc.barrier()
qc.cx(7, 0)
qc.cx(7, 4)
qc.cx(7, 5)
qc.cx(7, 6)
qc.barrier()
qc.cx(8, 1)
qc.cx(8, 3)
qc.cx(8, 5)
qc.cx(8, 6)
qc.barrier()
qc.cx(9, 2)
qc.cx(9, 3)
qc.cx(9, 4)
qc.cx(9, 5)
qc.barrier()
qc.cz(10, 0)
qc.cz(10, 2)
qc.cz(10, 3)
qc.cz(10, 6)
qc.barrier()
qc.cz(11, 1)
qc.cz(11, 3)
qc.cz(11, 4)
qc.cz(11, 6)
qc.barrier()
qc.cz(12, 0)
qc.cz(12, 1)
qc.cz(12, 2)
qc.cz(12, 5)
qc.barrier()
for i in range(7, 13):
  qc.h(i)

qc.draw('mpl')

for i in range(6):
  qc.measure(i+7, i)
  
  

sampler = StatevectorSampler()
pub =(qc)
job_sampler =sampler.run([pub], shots=1)

result_sampler = job_sampler.result()
counts_sampler = result_sampler[0].data.meas.get_counts()

print(counts_sampler)

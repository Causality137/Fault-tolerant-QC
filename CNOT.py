# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:01:53 2024

@author: Dr. Sutapa B. Neogi
"""

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

"""# Fault tolerant CNOT operator"""

qc = QuantumCircuit(14)
qc = Steane(qc)
qc.barrier()
qc.h(7)
qc.h(8)
qc.cx(7, 9)
qc.cx(8, 9)
qc.h(10)
qc.cx(10, 11)
qc.cx(10, 12)
qc.cx(8, 12)
qc.cx(10, 13)
qc.cx(8, 13)
qc.barrier()
for i in range(7):
  qc.cx(i, i+7)

qc.draw('mpl')
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import random
from .Value import Value

class Neuron:
    def __init__(self, n_inputs):
        self.w = [Value(random.uniform(-1, 1)) for _ in range(n_inputs)]
        self.b = Value(random.uniform(-1, 1))
        
    def __call__(self, x):
        return self.forward(x)
    def forward(self, x):
        #w * x + b
        print(list(zip(self.w, x)))
        return 0.0

    
        
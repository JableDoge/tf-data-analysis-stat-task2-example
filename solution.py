import pandas as pd
import numpy as np

import math
import scipy.stats

chat_id = 707776914 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    time_68 = 68
    alpha = 1 - p
    semians = 0
    for i in range(len(x)): #x_i ~ teta - exp(1)
      semians += x[i] #teta = (a*t^2)/2 + 1/2
    semians /= len(x) #G(x,teta)= -(sum(x_i)-n*teta) ~ Gamma(1,n)
    # (u_alpha/2)/n + x.mean < teta < u_(1-alpha/2)/n + x.mean 
    left = semians + scipy.stats.gamma.ppf((alpha)/2, len(x))/len(x) 
    right = semians + scipy.stats.gamma.ppf(1-alpha/2, len(x))/len(x)
    left -= 1/2
    right -= 1/2
    left /= (time_68**2)
    right /= (time_68**2)
    left *= 2
    right *= 2

    return left, \
           right

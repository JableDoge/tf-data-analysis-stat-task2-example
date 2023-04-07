import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 707776914 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    s = np.sum(x)
    x_mean = s / n
    left = (-np.log(alpha/2 + 1/2) - x_mean)/(68**2)
    right = (-np.log(3/2 - alpha/2) - x_mean)/(68**2)
    return left, \
           right

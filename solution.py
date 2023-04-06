import pandas as pd
import numpy as np

from scipy.stats import t, norm


chat_id = 707776914 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    mean = np.mean(x)
    std_error = np.std(x, ddof=1) / np.sqrt(n)
    t_value = t.ppf(1 - (1 - p) / 2, n - 1)
    margin_of_error = t_value * std_error
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return (lower_bound, upper_bound)

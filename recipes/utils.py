from fractions import Fraction
from typing import Tuple

def number_str_to_float(amount_str:str) -> Tuple[float, bool]:
    """
    Take in an amount string to return float (if possible).
    
    Added 7/5/2022 via source: "https://gist.github.com/codingforentrepreneurs/bcac6c1a047aec031f58984d5188e57d.js"
    
    Valid string returns:
    Float
    Boolean -> True
    Invalid string Returns
    Original String
    Boolean -> False
    
    Examples:
    1 1/2 -> 1.5, True
    32 -> 32.0, True
    Abc -> Abc, False
    """
    success = False
    number_as_float = amount_str
    try:
        number_as_float = float(sum(Fraction(s) for s in f"{amount_str}".split()))
    except:
        pass
    if isinstance(number_as_float, float):
        success = True
    return number_as_float, success

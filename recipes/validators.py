from pint import UnitRegistry, UndefinedUnitError
from django.core.exceptions import ValidationError
from .utils import number_str_to_float

def validate_unit_of_measurement(test_unit:str):
    try:
        UnitRegistry()[test_unit]
    except UndefinedUnitError:
        raise ValidationError(f'{test_unit} is not a valid unit of measurement')
    except:
        raise ValidationError(f'Something went wrong. Try again or cantact admin if necessary.')

def validate_quantity_measurement(amount:str):
    print(number_str_to_float(amount)[1])
    if not number_str_to_float(amount)[1]:
        raise ValidationError(f'{amount} is not a valid quantity format please try again.')

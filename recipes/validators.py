from pint import UnitRegistry, UndefinedUnitError
from django.core.exceptions import ValidationError

def validate_unit_of_measurement(test_unit):
    try:
        UnitRegistry()[test_unit]
    except UndefinedUnitError:
        raise ValidationError(f'{test_unit} is not a valid unit of measurement')
    except:
        raise ValidationError(f'Something went wrong. Try again or cantact admin if necessary.')

from django.utils import timezone
from django.core.exceptions import ValidationError


def custom_year_validator(value):
    if value > timezone.now().year:
        raise ValidationError(
            (f'{value} не может быть больше текущего года!'),
            params={'value': value},
        )

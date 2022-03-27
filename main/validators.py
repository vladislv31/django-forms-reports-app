from django.core.exceptions import ValidationError


def validate_questionnaire_fields(value):
    if len(value) < 3:
        raise ValidationError('test error')

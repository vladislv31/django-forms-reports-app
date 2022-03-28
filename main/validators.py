from django.core.exceptions import ValidationError

import json


def validate_questionnaire_fields(fields_json):
    try:
        fields = json.loads(fields_json)
    except ValueError as err:
        raise ValidationError('Not valid JSON')

    for field in fields:
        field_keys = field.keys()

        for x in ['title', 'designation', 'questions']:
            if x not in field_keys:
                raise ValidationError('Not valid fields')

        if not isinstance(field['questions'], list):
            raise ValidationError('Not valid fields')

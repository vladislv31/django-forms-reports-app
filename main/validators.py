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

        for x in field['questions']:
            if not isinstance(x, dict):
                raise ValidationError('Not valid fields')

            question_keys = x.keys()
            for y in ['number', 'question_text', 'recommendation_text']:
                if y not in question_keys:
                    raise ValidationError('Not valid fields')

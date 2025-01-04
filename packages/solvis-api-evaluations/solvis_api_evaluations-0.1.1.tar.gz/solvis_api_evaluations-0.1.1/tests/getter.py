# Imports
import pandas as pd
from api_evaluations import GetEvaluations


# Init mod
api = GetEvaluations()


# Request API
result1 = api.get_evaluations(
    user='',
    password='',
    survey_id='',
    start_datetime='2023-07-01T16:00:00',
    end_datetime='2023-07-01T16:02:00',
    scope='started_at',
)
result2 = api.get_evaluations(
    user='',
    password='',
    survey_id='',
    start_datetime='2023-07-01T16:00:00',
    end_datetime='2023-07-01T16:02:00',
    scope='started_at',
)


# evaluations = result1[0][82].copy()


# questions = evaluations.pop('formatted_answers')
# record = {**pd.json_normalize(evaluations, sep='__').iloc[0].to_dict()}


# records = []
# for question in questions:
#     if question['answer_type'] == 'Multiple Choice':
#         for choices in question['answers']:
#             # print(choices)
#             for choice in choices:
#                 key = f"{question_text}_{choices['choice_text']}"
#                 records[key] = 1
#                 if 'additional_field' in choice and 'additional_field_answer' in choice:
#                     additional_field_key = choice['additional_field']
#                     additional_field_value = choice['additional_field_answer']
#                     records[f"{key}_{additional_field_key}"] = additional_field_value


# records = []
# for question in questions:
#     answer_type = question['answer_type']
#     for answer in question['answers']:
#         if isinstance(answer, dict):
#             base_key = answer['question_text']
#         elif isinstance(answer, list):
#             answer = answer[0]
#             base_key = answer['question_text']

#         if answer_type == 'Multiple Choice':
#             for field in answer:
#                 if 'additional_field_answer' in field:
#                     key = f"{answer['question_text']}_{answer['choice_text']}"
#                     additional_field_key = answer['additional_field']
#                     additional_field_value = answer['additional_field_answer']
#                     record[f"{key}_{additional_field_key}"] = additional_field_value
#                 else:
#                     record[base_key] = answer.get('choice_text', None)

# records.append(record)



def data_processing_old(evaluations: list) -> pd.DataFrame:
    """Receives a list of dictionaries and return a processed dataframe

    Args:
        evaluations (list): A list of dictionaries

    Returns:
        pd.DataFrame: Processed dataframe
    """
    print('Iniciando processamento de dados...')
    records = []

    if evaluations:
        for page, eval_page in enumerate(evaluations):
            for idx, evaluation in enumerate(eval_page):
                questions = evaluation.pop('formatted_answers')
                record = {**pd.json_normalize(evaluation, sep='__').iloc[0].to_dict()}

                for question in questions:
                    answer_type = question['answer_type']
                    for answer in question['answers']:
                        if isinstance(answer, dict):
                            base_key = answer['question_text']
                        elif isinstance(answer, list):
                            answer = answer[0]
                            base_key = answer['question_text']

                        if answer_type == 'NPS':
                            record[base_key] = answer.get('answer_text', None)
                            record[f'{base_key}_valor'] = answer.get('answer_value', None)

                        elif answer_type == 'Scale':
                            record[base_key] = answer.get('choice_text', None)
                            record[f'{base_key}_valor'] = float(answer.get('choice_value', 0)) if answer.get('choice_value') is not None else None

                        # TODO: Adicionar possibilidade de campo additional_field e additional_field_answer
                        elif answer_type == 'Multiple Choice':
                            record[base_key] = answer.get('choice_text', None)
                        # TODO: Adicionar possibilidade de campo additional_field e additional_field_answer

                        elif answer_type in ['Text', 'Short Text']:
                            record[f'{base_key}'] = answer.get('choice_value', None)

                        elif answer_type in ['Phone', 'CPF', 'CNPJ', 'Email']:
                            record[f'{base_key}'] = answer.get('choice_text', None)

                        elif answer_type == 'Multiple Response':
                            for question_text, choices in question['answers'].items():
                                for choice in choices:
                                    key = f"{question_text}_{choice['choice_text']}"
                                    record[key] = 1
                                    if 'additional_field' in choice and 'additional_field_answer' in choice:
                                        additional_field_key = choice['additional_field']
                                        additional_field_value = choice['additional_field_answer']
                                        record[f"{key}_{additional_field_key}"] = additional_field_value

                records.append(record)
            print(f'Página: {page + 1} - OK!')

        print('Fim do processamento de dados!')

    return pd.DataFrame(records)


def data_processing_new(evaluations: list) -> pd.DataFrame:
    """Receives a list of dictionaries and return a processed dataframe

    Args:
        evaluations (list): A list of dictionaries

    Returns:
        pd.DataFrame: Processed dataframe
    """
    print('Iniciando processamento de dados...')
    records = []

    if evaluations:
        for page, eval_page in enumerate(evaluations):
            for idx, evaluation in enumerate(eval_page):
                questions = evaluation.pop('formatted_answers')
                record = {**pd.json_normalize(evaluation, sep='__').iloc[0].to_dict()}

                for question in questions:
                    answer_type = question['answer_type']
                    for answer in question['answers']:
                        if isinstance(answer, dict):
                            base_key = answer['question_text']
                        elif isinstance(answer, list):
                            answer = answer[0]
                            base_key = answer['question_text']

                        if answer_type == 'NPS':
                            record[base_key] = answer.get('answer_text', None)
                            record[f'{base_key}_valor'] = answer.get('answer_value', None)

                        elif answer_type == 'Scale':
                            record[base_key] = answer.get('choice_text', None)
                            record[f'{base_key}_valor'] = float(answer.get('choice_value', 0)) if answer.get('choice_value') is not None else None

                        elif answer_type == 'Multiple Choice':
                            for field in answer:
                                if 'additional_field_answer' in field:
                                    key = f"{answer['question_text']}_{answer['choice_text']}"
                                    additional_field_key = answer['additional_field']
                                    additional_field_value = answer['additional_field_answer']
                                    record[f"{key}_{additional_field_key}"] = additional_field_value
                                else:
                                    record[base_key] = answer.get('choice_text', None)

                        elif answer_type in ['Text', 'Short Text']:
                            record[f'{base_key}'] = answer.get('choice_value', None)

                        elif answer_type in ['Phone', 'CPF', 'CNPJ', 'Email']:
                            record[f'{base_key}'] = answer.get('choice_text', None)

                        elif answer_type == 'Multiple Response':
                            for question_text, choices in question['answers'].items():
                                for choice in choices:
                                    key = f"{question_text}_{choice['choice_text']}"
                                    record[key] = 1
                                    if 'additional_field' in choice and 'additional_field_answer' in choice:
                                        additional_field_key = choice['additional_field']
                                        additional_field_value = choice['additional_field_answer']
                                        record[f"{key}_{additional_field_key}"] = additional_field_value

                records.append(record)
            print(f'Página: {page + 1} - OK!')

        print('Fim do processamento de dados!')

    return pd.DataFrame(records)


test1 = data_processing_old(result1)
test2 = data_processing_new(result2)



set(test2.columns.tolist()).difference(test1.columns.tolist())
# test2.columns.tolist()

test1['Na compra de hoje, faltou algum produto ou marca que você procurava?'].value_counts()
test2['Na compra de hoje, faltou algum produto ou marca que você procurava?'].value_counts()
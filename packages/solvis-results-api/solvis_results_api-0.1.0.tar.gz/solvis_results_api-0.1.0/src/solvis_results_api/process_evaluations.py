import logging
import pandas as pd
from typing import List, Dict


class ProcessEvaluations:
    """
    A class to process evaluation data from a list of dictionaries into a structured Pandas DataFrame.
    """

    def __init__(self) -> None:
        """
        Initialize the ProcessEvaluations class with default attributes.
        """
        logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

    def process_evaluations(self, evaluations: List[List[Dict]]) -> pd.DataFrame:
        """
        Receives a list of dictionaries and returns a processed DataFrame.

        Args:
            evaluations (List[List[Dict]]): A list of dictionaries representing evaluation data.

        Returns:
            pd.DataFrame: Processed DataFrame.
        """

        logging.info('Starting data processing...')
        records = []

        if evaluations:
            for page, eval_page in enumerate(evaluations):
                for idx, evaluation in enumerate(eval_page):
                    questions = evaluation.pop('formatted_answers')
                    record = {
                        **pd.json_normalize(evaluation, sep='__').iloc[0].to_dict()
                    }

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
                                record[f'{base_key}_value'] = answer.get(
                                    'answer_value', None
                                )

                            elif answer_type == 'Scale':
                                record[base_key] = answer.get('choice_text', None)
                                record[f'{base_key}_value'] = (
                                    float(answer.get('choice_value', 0))
                                    if answer.get('choice_value') is not None
                                    else None
                                )

                            elif answer_type == 'Multiple Choice':
                                for field in answer:
                                    if 'additional_field_answer' in field:
                                        key = f"{answer['question_text']}_{answer['choice_text']}"
                                        additional_field_key = answer['additional_field']
                                        additional_field_value = answer['additional_field_answer']
                                        record[f'{key}_{additional_field_key}'] = (additional_field_value)
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
                                        if ('additional_field' in choice and 'additional_field_answer' in choice):
                                            additional_field_key = choice['additional_field']
                                            additional_field_value = choice['additional_field_answer']
                                            record[f'{key}_{additional_field_key}'] = (additional_field_value)

                    records.append(record)
            logging.info('Data processing completed!')
        df_final = pd.DataFrame(records)

        return df_final

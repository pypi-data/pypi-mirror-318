from solvis_results_api import GetEvaluations, ProcessEvaluations


api = GetEvaluations()
process = ProcessEvaluations()


evaluations = api.get_evaluations(
    user='',
    password='',
    survey_id='',
    start_datetime='2024-12-01T00:00:00',
    end_datetime='2024-12-10T23:59:59',
)

df = process.process_evaluations(evaluations)
df

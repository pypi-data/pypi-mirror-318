# Solvis Results API

This is a package for requesting and processing data from Solvis's results API.
The package is designed to handle complex nested data structures, efficiently transforming them into a tabular format (pandas dataframe) suitable for analysis.


## Features

- Request data from the following endpoints:
  - Devices
  - Evaluations
  - Questionnaire
  - Surveyed Units
  - Suspicious Occurrences
- Converts nested data into a flat pandas dataframe.
- Handles various evaluations question types, including:
  - **NPS (Net Promoter Score)**
  - **Scale**
  - **Multiple Choice**
  - **Text and Short Text**
  - **Multiple Response**
  - **Special Types** (Phone, CPF, CNPJ, Email)
- Robust handling of unexpected or malformed data.
- Logging for process tracking and debugging.


## Installation

Install the package via pip (or your favorite package manager):

```bash
pip install solvis-results-api
```


## Usage

### Importing the Module

```python
from solvis_results_api import GetEvaluations, ProcessEvaluations
```

### Example

```python
# Initialize modules
api = GetEvaluations()
processor = ProcessEvaluations()

# Request API
evaluations = api.get_evaluations(
    user='',
    password='',
    survey_id='',
    start_datetime='2025-01-01T00:00:00',
    end_datetime='2025-01-31T23:59:59',
)

# Process the data
df = processor.process_evaluations(evaluations)

# Print output
print(df)
```


## Dependencies

- Python 3.12+
- Pandas
- Requests


## Contact

For questions or feedback, feel free to reach out:

- Author: Paulo Victor
- Email: paulo.barbosa@solvis.com.br

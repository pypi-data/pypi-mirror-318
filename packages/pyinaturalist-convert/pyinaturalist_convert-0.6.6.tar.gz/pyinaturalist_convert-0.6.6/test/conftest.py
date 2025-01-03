# flake8: noqa: F401
import json
import logging
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.absolute()
SAMPLE_DATA_DIR = PROJECT_DIR / 'test' / 'sample_data'

# logging.basicConfig(level='DEBUG')


def load_sample_data(filename):
    with open(SAMPLE_DATA_DIR / filename, encoding='utf-8') as f:
        if filename.endswith('json'):
            return json.load(f)
        else:
            return f.read()

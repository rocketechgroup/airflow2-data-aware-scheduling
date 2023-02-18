import os


def get_core_project_id():
    return os.environ.get('GCP_PROJECT_ID')

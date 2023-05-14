from phishing_domain_detection.data_access.phishing_data import PhishingData
from phishing_domain_detection.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from main import set_env_variable
import os
env_file_path = os.path.join(os.getcwd(), "env.yaml")
print(env_file_path)
if __name__ == '__main__':
    data_file_path = "/home/ali/anaconda3/Coding Playground/PHISHING_DOMAIN_DETECTION/dataset_full.csv"
    env_file_path = "/home/ali/anaconda3/Coding Playground/PHISHING_DOMAIN_DETECTION/env.yaml"
    set_env_variable(env_file_path)
    print(os.environ['MONGO_DB_URL'])
    ed = PhishingData()
    if DATA_INGESTION_COLLECTION_NAME in ed.mongo_client.database.list_collection_names():
        ed.mongo_client.database[DATA_INGESTION_COLLECTION_NAME].drop()
    ed.save_csv_file(file_path=data_file_path, collection_name=DATA_INGESTION_COLLECTION_NAME)


from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Starting data ingestion")
        dataframe = data_ingestion.initiate_data_ingestion()
        print(dataframe)
    except Exception as e:
        raise NetworkSecurityException(e, sys)    
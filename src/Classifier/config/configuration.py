from src.Classifier.constants import *
from src.Classifier.utils.common import read_yaml, create_directories
from src.Classifier.entity.entity_config import (DataIngestionEntityConfig)

# Configuration Manager of the classifier
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        
    
    # Data Ingestion Function
    def get_data_ingestion_config(self) -> DataIngestionEntityConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionEntityConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    
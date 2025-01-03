# testing/base_test_config.py

import os
from datetime import datetime
from .helpers import create_spark_session, register_all_tables, clear_directory, get_git_root


class BaseTestConfig:
    """
    Base configuration for test setup. Defines shared constants and utilities.
    Can be extended by specific test suites to override settings.
    """
    # Shared constants
    PROJECT_PATH = get_git_root(os.getcwd())
    HIVE_LOCATION = os.path.join(PROJECT_PATH, 'hive-warehouse')
    WAREHOUSE_LOCATION = os.path.join(PROJECT_PATH, 'spark-warehouse')
    DATASETS_LOCATION = os.path.join(PROJECT_PATH, 'tests/datasets.yml')

    # Normalize paths for Windows
    if os.name == 'nt':
        HIVE_LOCATION = HIVE_LOCATION.replace('\\', '/')
        WAREHOUSE_LOCATION = WAREHOUSE_LOCATION.replace('\\', '/')
        DATASETS_LOCATION = DATASETS_LOCATION.replace('\\', '/')

    # Default timestamp for mocking. It can be overwritten in test suit.
    mock_now = datetime(2025, 1, 1, 0, 0, 0)

    def create_spark_session(self):
        """
        Create a Spark session with warehouse and Hive configuration.
        """
        return create_spark_session(self.WAREHOUSE_LOCATION, self.HIVE_LOCATION)

    def register_tables(self, spark_session):
        """
        Registers all tables in the Spark session using the YAML configuration file.
        """
        register_all_tables(spark_session, self.DATASETS_LOCATION)

    def clean_hive_directory(self):
        """
        Cleans Hive warehouse directory after tests to ensure a clean state.
        """
        clear_directory(self.HIVE_LOCATION)
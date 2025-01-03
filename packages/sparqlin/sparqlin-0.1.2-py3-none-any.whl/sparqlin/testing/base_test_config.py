# testing/base_test_config.py

import os
from datetime import datetime
from .helpers import create_spark_session, register_all_tables, clear_directory


class BaseTestConfig:
    """
    Base configuration for test setup. Defines shared constants and utilities.
    Can be extended by specific test suites to override settings.
    """
    # Default timestamp for mocking. It can be overwritten in test suit.
    mock_now = datetime(2025, 1, 1, 0, 0, 0)

    def __init__(self, tmp_path_factory):
        """
        Initialize BaseTestConfig with a temporary directory provided by pytest.

        Args:
            tmp_path_factory: pytest's tmp_path_factory fixture for creating temporary directories.
        """
        # Create a unique temporary `hive_test` directory for this configuration
        tmp_path = tmp_path_factory.mktemp("hive_test")
        print(f"Created temporary directory: {tmp_path}")

        # Define locations for Hive and Spark warehouse
        self.HIVE_LOCATION = tmp_path / "hive-warehouse"
        self.WAREHOUSE_LOCATION = tmp_path / "spark-warehouse"
        self.DATASETS_LOCATION = tmp_path / "datasets.yml"

        # Ensure directories exist
        self.HIVE_LOCATION.mkdir(parents=True, exist_ok=True)
        self.WAREHOUSE_LOCATION.mkdir(parents=True, exist_ok=True)

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

    #def clean_hive_directory(self):
    #    """
    #    Cleans Hive warehouse directory after tests to ensure a clean state.
    #    """
    #    clear_directory(self.HIVE_LOCATION)
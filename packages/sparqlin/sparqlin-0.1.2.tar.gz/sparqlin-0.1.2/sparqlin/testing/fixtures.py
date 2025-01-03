# testing/fixtures.py

import pytest
from pyspark.sql.types import TimestampType
from ..testing.base_test_config import BaseTestConfig

@pytest.fixture(scope="module")
def spark_session():
    """
    Centralized spark_session fixture for creating and managing Spark sessions.
    Uses the BaseTestConfig class for configuration.
    """
    # Create a default configuration object (can be subclassed if needed)
    config = BaseTestConfig()

    # Create SparkSession
    spark = config.create_spark_session()

    # Register the mock `now()` function
    spark.udf.register("now", lambda: config.mock_now, TimestampType())

    # Register all tables from the dataset
    config.register_tables(spark)

    # Yield SparkSession to tests
    yield spark

    # Teardown logic stop SparkSession and clean directories
    spark.stop()
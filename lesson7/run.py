import time
import logging

class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        logging.info(f"Execution time: {elapsed_time:.2f} seconds")

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

with TimerContext():
    time.sleep(2)

# Managing Temporary In-Memory Data Structures

GLOBAL_CONFIG = {
    "feature_a": True,
    "feature_b": False,
    "max_retries": 3
}

class Configuration:
    def __init__(self, updates, validator=None):
        self.updates = updates
        self.validator = validator
        self.original_config = None

    def __enter__(self):
        self.original_config = GLOBAL_CONFIG.copy()
        GLOBAL_CONFIG.update(self.updates)
        logging.info(f"Configuration updated: {self.updates}")

    def __exit__(self, exc_type, exc_value, traceback):
        if self.validator:
            if not self.validator(GLOBAL_CONFIG):
                logging.error("Validation failed. Restoring original configuration.")
                GLOBAL_CONFIG.clear()
                GLOBAL_CONFIG.update(self.original_config)
                return

        if exc_type:
            logging.error("Exception occurred. Restoring original configuration.")

        GLOBAL_CONFIG.clear()
        GLOBAL_CONFIG.update(self.original_config)
        logging.info("Configuration restored.")

# Example validator function
def validate_config(config: dict) -> bool:
    if not isinstance(config.get("max_retries"), int) or config.get("max_retries", 0) < 0:
        logging.error("Invalid max_retries value: Must be a non-negative integer.")
        return False
    if not isinstance(config.get("feature_a"), bool):
        logging.error("Invalid feature_a value: Must be a boolean.")
        return False
    return True

# Example usage
if __name__ == "__main__":
    logging.info("Initial GLOBAL_CONFIG: %s", GLOBAL_CONFIG)

    # Example 1: Successful configuration update
    try:
        with Configuration({"feature_a": False, "max_retries": 5}):
            logging.info("Inside context: %s", GLOBAL_CONFIG)
    except Exception as e:
        logging.error("Error: %s", e)

    logging.info("After context: %s", GLOBAL_CONFIG)

    # Example 2: Configuration update with validation failure
    try:
        with Configuration({"feature_a": "invalid_value", "max_retries": -1}, validator=validate_config):
            logging.info("This should not be printed if validation fails.")
    except Exception as e:
        logging.error("Caught exception: %s", e)

    logging.info("After failed context: %s", GLOBAL_CONFIG)

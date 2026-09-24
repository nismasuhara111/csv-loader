import time
from logging_config import setup_logging


logger = setup_logging()


def run_pipeline():
    logger.info("Pipeline execution started")

    start_time = time.time()

    try:
        logger.info("Loading input data")

        # Simulate pipeline processing
        time.sleep(0.5)

        record_count = 10

        logger.info(f"Records processed: {record_count}")

        duration = time.time() - start_time

        logger.info(
            f"Pipeline execution completed in {duration:.4f} seconds"
        )

    except Exception:
        logger.exception("Pipeline execution failed")


if __name__ == "__main__":
    run_pipeline()
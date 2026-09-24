from logging_config import setup_logging


logger = setup_logging()


def run_failed_pipeline():
    logger.info("Starting deliberately failed pipeline")

    try:
        logger.info("Attempting to load missing file")

        with open("data/not_found.csv", "r", encoding="utf-8") as file:
            file.read()

    except FileNotFoundError:
        logger.exception("Pipeline failed while loading input file")


if __name__ == "__main__":
    run_failed_pipeline()
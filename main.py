from src import database, config
import logging
import importlib
import time
import sys
import argparse


def process_handler(handler: str) -> None:
    delta = time.time()
    with database.Database() as db:
        try:
            module = importlib.import_module(f"src.handlers.{handler}")
            handler_class = getattr(module, f"{handler.capitalize()}Source")
            handler = handler_class()
        except Exception as e:
            logging.error(f"Error importing handler {handler}: {e}")
            return

        handler.source_id = db.insert_source(vars(handler))["source_id"]

        logging.info(f"Running handler {handler.source_name} ...")

        if handler.type == "url":
            for url in handler:
                db.insert_url(handler.source_id, url)
        elif handler.type == "ip":
            for ip in handler:
                db.insert_ip(handler.source_id, ip)
        else:
            logging.error(f"Handler {handler.source_name} has invalid type {handler.type}")
            return

    logging.info(f"Finished handler {handler.source_name} in {time.time() - delta} seconds")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        stream=sys.stdout)

    for source in config.valid_handlers(config.CONFIG):
        process_handler(source)

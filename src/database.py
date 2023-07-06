import logging

from psycopg2 import connect, sql, Error
from typing import Dict

from src.config import CONFIG


class Database(object):
    def __init__(self) -> None:
        self.connection = None
        self.cursor = None

    def __enter__(self) -> "Database":
        try:
            self.connection = connect(**CONFIG["database"])
            self.cursor = self.connection.cursor()
            logging.debug("Connected to database")
            self.__initialize()
            return self
        except Error as e:
            logging.error(f"Error creating connection to the database.")
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        logging.debug("Closed database connection")

    def __initialize(self) -> None:
        with open("src/schema.sql") as f:
            self.cursor.execute(sql.SQL(f.read()))
        logging.debug("Initialized database")

    def __source_exists(self, source: Dict) -> int:
        self.cursor.execute(
            sql.SQL("SELECT id FROM sources WHERE name = %s"),
            (source["source_name"],)
        )
        return self.cursor.fetchone()

    def insert_source(self, source: Dict) -> Dict:
        """
        Inserts a source into the database if it does not already exist.
        :param source:
        :return: data source vars dict with updated source_id either from the database or from the insert
        """
        sid = self.__source_exists(source)
        if sid:
            logging.debug(f"Source {source['source_name']} already exists")
            source["source_id"] = sid
            return source

        self.cursor.execute(
            sql.SQL("INSERT INTO sources (name, url) VALUES (%s, %s) ON CONFLICT DO NOTHING RETURNING id"),
            (source["source_name"], source["source_url"])
        )
        source["source_id"] = self.cursor.fetchone()
        self.connection.commit()
        logging.debug(f"Inserted source {source['source_name']}")
        return source

    def insert_url(self, source_id: int, url: str) -> None:
        self.cursor.execute(
            sql.SQL("INSERT INTO urls (source, url) VALUES (%s, %s) ON CONFLICT DO NOTHING"),
            (source_id, url)
        )
        logging.debug(f"Inserted url {url}")

    def insert_ip(self, source_id: int, ip: str) -> None:
        self.cursor.execute(
            sql.SQL("INSERT INTO ip_addresses (source, address) VALUES (%s, %s) ON CONFLICT DO NOTHING"),
            (source_id, ip)
        )
        logging.debug(f"Inserted ip {ip}")

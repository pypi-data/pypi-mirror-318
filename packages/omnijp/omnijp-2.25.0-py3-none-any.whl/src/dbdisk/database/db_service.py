from abc import abstractmethod
import logging

import psycopg2
import pymssql


class DbService:

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.logger = logging.getLogger(__name__)

    def execute(self, query):
        connection = None
        cursor = None
        try:
            self.logger.info("Executing query: ", query)
            self.logger.info("Connecting to database...")
            connection = self.connect()
            self.logger.info("Connected to database")
            cursor = connection.cursor()
            self.logger.info("Executing query...")
            cursor.execute(query)
            header = [desc[0] for desc in cursor.description]
            result = cursor.fetchall()
            self.logger.info("Query executed")
        except Exception as e:
            self.handle_error(e)
            result = None
            header = None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return header, result

    @abstractmethod
    def connect(self):
        pass

    @staticmethod
    def handle_error(error):
        error_messages = {
            psycopg2.Error: "Error connecting to PostgresSQL:",
            pymssql.Error: "Error connecting to Sybase:"
        }
        error_type = type(error)
        message = error_messages.get(error_type, "Unknown error")
        raise Exception(message, error)
    @abstractmethod
    def get_all_tables_query(self):
        pass

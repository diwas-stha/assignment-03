'''
Build a logging system using the Factory Design Pattern.
Create a LoggerFactory class that generates different types of loggers (e.g., FileLogger,
ConsoleLogger, DatabaseLogger). Implement methods in each logger to write logs to
their respective destinations. Show how the Factory Design Pattern helps to decouple
the logging system from the application and allows for flexible log handling.

'''

from abc import ABC, abstractmethod

class Logger(ABC):
    """
    Abstract base class representing a Logger.

    Attributes:
        None

    Methods:
        write_log(message: str):
            Abstract method to write a log message.

    """

    @abstractmethod
    def write_log(self, message: str):
        """
        Abstract method to write a log message.

        Parameters:
            message (str): The log message to be written.
        """
        pass

class FileLogger(Logger):
    """
    Concrete Logger class that writes logs to a file.

    Attributes:
        None

    Methods:
        write_log(message: str) -> None:
            Writes the log message to a file.

    """

    def write_log(self, message: str):
        """
        Writes the log message to a file.

        Parameters:
            message (str): The log message to be written.

        """
        with open("log.txt", "a") as file:
            file.write(f"[FileLogger] {message}\n")

class ConsoleLogger(Logger):
    """
    Concrete Logger class that writes logs to the console.

    Attributes:
        None

    Methods:
        write_log(message: str):
            Prints the log message to the console.

    """

    def write_log(self, message: str):
        """
        Prints the log message to the console.

        Parameters:
            message (str): The log message to be printed.

        """
        print(f"[ConsoleLogger] {message}")

class DatabaseLogger(Logger):
    """
    Concrete Logger class that writes logs to a database.

    Attributes:
        None

    Methods:
        write_log(message: str) -> None:
            Writes the log message to a database.

    """

    def write_log(self, message: str) -> None:
        """
        Writes the log message to a database.

        Parameters:
            message (str): The log message to be written.
        """
        # Code to write log to a database
        print(f"[DatabaseLogger] {message}")

class LoggerFactory:
    """
    Factory class to generate different types of loggers.

    Attributes:
        None

    Methods:
        get_logger(logger_type: str) -> Logger:
            Returns the logger instance based on the provided logger_type.

    """

    @staticmethod
    def get_logger(logger_type: str) -> Logger:
        """
        Returns the logger instance based on the provided logger_type.

        Parameters:
            logger_type (str): The type of logger to be created ("file", "console", or "database").

        Returns:
            Logger: An instance of the requested Logger.
        
        Raises:
            ValueError: If an invalid logger_type is provided.
        """
        if logger_type == "file":
            return FileLogger()
        elif logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "database":
            return DatabaseLogger()
        else:
            raise ValueError("Invalid logger type. Available types: file, console, database")

if __name__ == "__main__":
    logger_type = input("Enter the logger type (file, console, database): ")

    try:
        logger = LoggerFactory.get_logger(logger_type)
    except ValueError as e:
        print(e)
        exit()

    logger.write_log("This is a log message.")
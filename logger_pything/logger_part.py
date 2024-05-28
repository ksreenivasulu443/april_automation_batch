import logging

import pandas as pd

# 1. CRITICAL==>50==>Represents a very serious problem that needs high attention
# 2. ERROR===>40===>Represents a serious error
# 3. WARNING==>30==>Represents a warning message, some caution needed. It is alert to
# the programmer
# 4. INFO===>20===>Represents a message with some important information
# 5. DEBUG===>10==>Represents a message with debugging information
# 6. NOTSET==>0==>Rrepresents that the level is not set.


# %(asctime)s: The timestamp of the log message in the format specified by the datefmt parameter (if provided).
# %(levelname)s: The log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
# %(message)s: The log message itself.
# %(name)s: The name of the logger.
# %(filename)s: The name of the file containing the logger call.
# %(lineno)d: The line number where the logger call occurred.
# %(funcName)s: The name of the function/method where the logger call occurred.

# Default level is Warning

logging.basicConfig(filename='log2.txt',filemode='w',level=logging.CRITICAL,
    format='%(asctime)s-%(levelname)s - %(message)s - %(name)s-%(funcName)s-%(lineno)d')

logger = logging.getLogger()
# print("starting...")
# logger.debug("debug") #
# print("print debug")
# logger.info("km travelled")
# print("print km travelled")
# logger.warning("had to diversion")
# print("print had to take diversion")
# logger.error("car type puncture")
# print("print car puncture")
# logger.critical("print taken another mode of travel")
# print("taken another mode of tarvel")
# logger.info("this second info")
# print("end of journey....")



def read_file(file_type, path):
    if file_type =='csv':
        df = pd.read_csv(path)
        print("Data has been read successfully and file path is " , path )
        logger.info(f"Data has been read successfully and path is {path}")
        return df

    elif file_type == 'excel':
        df = pd.read_excel(path)
        #print("Data has been read successfully and file path is " , path )
        logger.info("Data has been read successfully ")
        return df
    else:
        logger.error(f"please enter correct file format, Current {file_type} file is not handled")
        logger.critical("file path not foundit is critical")


df = read_file('csv', r"/Users/harish/PycharmProjects/april_automation_batch/FIles/Contact_info.csv")
print(df.head())

df2 = read_file('json','json.file')

# df3 = read("parquet", 'xyz.parquet')


import logging



def main():
    logging.info('Application started.')

    try:
        logging.debug('Attempting to perform a complex calculation.')
        result = complex_calculation(3, 4)
        logging.info(f'Calculation result: {result}')
    except Exception as e:
        logging.error(f'Error during calculation: {e}')

    check_disk_space()
    process_file('non_existent_file.txt')


def complex_calculation(x, y):
    logging.debug(f'Starting complex calculation with x={x} and y={y}')
    result = x * y + 42
    logging.debug(f'Result of calculation: {result}')
    return result


def check_disk_space():
    disk_space = 5  # Assume we got this value from a system call
    if disk_space < 10:
        logging.warning(f'Disk space is low: {disk_space}GB remaining.')


def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        # Process the file
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
    except Exception as e:
        logging.error(f'An error occurred: {e}')


def initialize_database():
    try:
        raise ConnectionError('Failed to connect to the database.')
    except ConnectionError as e:
        logging.critical(f'Critical error: {e}. Shutting down the application.')
        exit(1)


if __name__ == '__main__':
    main()
    initialize_database()

from pandas import read_csv
from os import getcwd
from pathlib import Path

def time_parser(time: str) -> int:
    """Converts the time col for comparison purpose"""
    hours, minutes = time.split(':')
    return int(hours) * 100 + int(minutes)

def open_csv_file():
    file_location: str = "res/train_revised.csv"
    chunk_size: int = 1000
    convertors: list = {
        "travel_time": time_parser
    }   
    actual_location = Path(__file__).parent.parent / file_location
    return read_csv(actual_location, chunksize=chunk_size, header=0, index_col=0, converters=convertors)


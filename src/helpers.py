from pandas import read_csv

def time_parser(time: str) -> int:
    """Converts the time col for comparison purpose"""
    hours, minutes = time.split(':')
    return int(hours) * 100 + int(minutes)

def open_csv_file():
    file_location: str = "./res/train_revised.csv"
    chunk_size: int = 1000
    convertors: list = {
        "travel_time": time_parser
    }   
    return read_csv(file_location, chunksize=chunk_size, header=0, index_col=0, converters=convertors)


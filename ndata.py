from io import TextIOWrapper
from typing import List, Union
import os
import csv
from dataclasses import dataclass
import tqdm
@dataclass
class NsmcRawData:
    id: int
    document: str
    label: int

class NsmcRawDataReader:
    def __init__(self, file: Union[str, TextIOWrapper]):
        self.fp = file
        self.need_close = isinstance(file,str)
        if self.need_close:
            self.fp = open(file,"r",encoding="utf-8",newline='\n')
        self.rd = csv.DictReader(self.fp,delimiter='\t')

    def __iter__(self):
        mapper = lambda data: NsmcRawData(int(data["id"]),data["document"],int(data["label"]))
        return iter(map(mapper,self.rd))
    
    def close(self):
        if self.need_close:
            self.fp.close()
    
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def readNsmcRawData(file: Union[str, TextIOWrapper], use_tqdm = False, total: int = 0) -> List[NsmcRawData]:
    dataset = []
    with NsmcRawDataReader(file) as dataReader:
        if use_tqdm and total > 0:
            for d in tqdm.tqdm(dataReader, total=total):
                dataset.append(d)
        else:
            for data in dataReader:
                dataset.append(data)
    return dataset

BASE_PATH = "nsmc/nsmc-master"

if __name__ == "__main__":
    dataset = []
    raw = readNsmcRawData(f"{BASE_PATH}/ratings.txt", use_tqdm= True, total = 200000)
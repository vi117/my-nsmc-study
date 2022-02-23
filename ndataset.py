import sys
from typing import List
from torch.utils.data import Dataset
import torch
from transformers import PreTrainedTokenizer
from ndata import readNsmcRawData, NsmcRawData

def readNsmcDataAll():
    """
    Returns: train, test
    """
    print("read train set", file=sys.stderr)
    train = readNsmcRawData("nsmc/nsmc-master/ratings_train.txt",use_tqdm=True,total=150_000)
    print("read test set", file=sys.stderr)
    test = readNsmcRawData("nsmc/nsmc-master/ratings_test.txt",use_tqdm=True,total=50_000)
    return NsmcDataset(train),NsmcDataset(test)

class NsmcDataset(Dataset):
    def __init__(self, data: List[NsmcRawData]):
        self.x = data
    def __len__(self):
        return len(self.x)
    def __getitem__(self, idx):
        return self.x[idx]

def make_collate_fn(tokenizer: PreTrainedTokenizer):
    def collate_fn(batch: List[NsmcRawData]):
        labels = [s.label for s in batch]
        return tokenizer([s.document for s in batch], return_tensors='pt', padding='longest', truncation=True), torch.tensor(labels)
    return collate_fn

if __name__ == "__main__":
    from transformers import BertTokenizer
    print("load bert tokenizer...")
    PRETAINED_MODEL_NAME = 'bert-base-multilingual-cased'
    tokenizer = BertTokenizer.from_pretrained(PRETAINED_MODEL_NAME)

    data = readNsmcRawData("nsmc/nsmc-master/ratings_train.txt",use_tqdm=True,total=150000)

    collate = make_collate_fn(tokenizer)
    print(collate(data[0:2]))

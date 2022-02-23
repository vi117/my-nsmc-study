import requests
import tqdm
import zipfile
import os

def downloadNsmc(filename = "nsmc.zip"):
    URL = "https://github.com/e9t/nsmc/archive/refs/heads/master.zip"
    
    headReq = requests.head(URL, headers={'Accept-Encoding': None})
    length = headReq.headers["Content-Length"]
    with requests.get(URL, stream= True) as nsmc:
        nsmc.raise_for_status()
        with open(filename ,"wb") as fp:
            t = tqdm.tqdm(total=int(length), unit='byte', desc=filename)
            for chunk in nsmc.iter_content(chunk_size = 8192):
                fp.write(chunk)
                t.update(len(chunk))
            t.close()

if __name__ == "__main__":
    os.makedirs("nsmc", exist_ok=True)
    if not os.path.exists("nsmc.zip"):
        downloadNsmc()
    with zipfile.ZipFile("nsmc.zip") as nsmc:
        for member in tqdm.tqdm(nsmc.infolist(), desc="Extracting", unit="files"):
            nsmc.extract(member,"nsmc")
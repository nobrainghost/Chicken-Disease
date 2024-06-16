import os
from box.exceptions import BoxValueError
import yaml
from src.chickendisease import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: path) -> ConfigBox:
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Reading yaml file from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError(f"Error reading yaml file from {path_to_yaml}")
    except Exception as e:
        raise e

@ensure_annotations
def create_directory(path_directories: list, verbose=True):
    for path in path_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")    

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
        logger.info(f"Saved json file at {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path,'r') as f:
        data=json.load(f)
    logger.info(f"Loaded json file from {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(data:Any,path:Path):
        joblib.dump(value=data,filename=path)
        logger.info(f"Saved binary file at {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    data=joblib.load(path)
    logger.info(f"Loaded binary file from {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    size_in_kb=round(os.path.getsize(path)/1024)

def decodeImage(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedimagePath):
    with open(croppedimagePath, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string
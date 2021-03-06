import numpy as np
import json


def load_json(json_filename):
    with open(json_filename, 'r', encoding='utf-8', errors='ignore') as f:
        rows = json.load(f)
    return rows


def to_nparray(requisite_vector):
    paragraphs_vector = np.array(requisite_vector)
    return paragraphs_vector


def nmslib_to_nparray(index):
    return to_nparray(index)

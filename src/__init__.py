INDEX_FILE_NAME = 'index.nmslib'
JSON_FILE_NAME = 'score_matrix.json'
MAPPING_FILE_NAME = 'mapping.json'
OUTPUT_PATH = 'data'
DISTANCE_THRESHOLD = 0.5

BUILD_MODEL_ENDPOINT = 'http://localhost:9405/upc/Compare/BuildModel'
COMPUTE_CLUSTERS_ENDPOINT = 'http://localhost:9405/upc/Compare/ComputeClusters'


__all__ = [
    'INDEX_FILE_NAME',
    'JSON_FILE_NAME',
    'MAPPING_FILE_NAME',
    'OUTPUT_PATH',
    'DISTANCE_THRESHOLD',
    'BUILD_MODEL_ENDPOINT',
    'COMPUTE_CLUSTERS_ENDPOINT'
]

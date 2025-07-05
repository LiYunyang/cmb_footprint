import importlib
import os

def get_data_path(path):
    out = None
    with importlib.resources.path('cmb_footprint', 'data') as f:
        out = os.path.join(str(f), path)
    return out
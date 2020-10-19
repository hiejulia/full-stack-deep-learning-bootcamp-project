"""Utility functions for text_recognizer module."""

from concurrent.futures import as_completed, ThreadPoolExecutor
from pathlib import Path
from typing import Union
from urllib.request import urlopen, urlretrieve
import hashlib
import os

import numpy as np
import cv2
from tqdm import tqdm


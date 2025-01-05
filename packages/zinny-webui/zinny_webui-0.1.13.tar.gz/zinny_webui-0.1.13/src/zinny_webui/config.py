"""app locations"""

import os
from importlib.metadata import version, PackageNotFoundError

# pylint: disable=missing-function-docstring

APP_DATA_PATH = "zinny-api/data"
SURVEY_PATHS = {
    "shared": os.path.join(APP_DATA_PATH, "surveys", "shared"),
    "local": os.path.join(APP_DATA_PATH, "surveys", "local")
}

WEIGHTS_PATHS = {
    "shared": os.path.join(APP_DATA_PATH, "weights", "shared"),
    "local": os.path.join(APP_DATA_PATH, "weights", "local")
}

COLLECTION_PATHS = {
    "shared": os.path.join(APP_DATA_PATH, "collections", "shared"),
    "local": os.path.join(APP_DATA_PATH, "collections", "local")
}


def get_package_version(package_name):
    try:
        return version(package_name)
    except PackageNotFoundError:
        return "unknown"

# Retrieve version numbers
ZINNY_API_VERSION = get_package_version("zinny-api")
ZINNY_WEBUI_VERSION = get_package_version("zinny-webui")

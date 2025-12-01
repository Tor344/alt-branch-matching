import requests

from src.branch_matching.log import logger


PATH_BRANCH_BINARY_PACKAGES = "https://rdb.altlinux.org/api/export/branch_binary_packages/{branch}"


def get_from_branch_binary_packages(branch:str)->list:
    try:
        url = PATH_BRANCH_BINARY_PACKAGES.format(branch=branch)

        response = requests.get(url=url,timeout=60)
        response.raise_for_status()

        data = response.json()
        return data.get("packages")

    except requests.exceptions.RequestException as e:
        logger.error(f"Произошла ошибка {e}")
        return []
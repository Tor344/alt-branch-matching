import requests


PATH_BRANCH_BINARY_PACKAGES = "https://rdb.altlinux.org/api/export/branch_binary_packages/"


def get_from_branch_binary_packages(branch:str)->dict:
    try:
        url = PATH_BRANCH_BINARY_PACKAGES + branch

        response = requests.get(url=url,timeout=60)
        response.raise_for_status()

        data = response.json()
        return data.get("packages")

    except requests.exceptions.RequestException as e:
        raise e
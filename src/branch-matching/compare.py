
def sort_by_architecture(branch: list[dict]):
    packages_by_arch = {}
    for package in branch:
        arch = package['arch']
        name = package['name']
        if arch not in packages_by_arch:
            packages_by_arch[arch] = {}
        packages_by_arch[arch][name] = package
    return packages_by_arch


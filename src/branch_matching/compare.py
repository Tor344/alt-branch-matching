from rpm_vercmp import vercmp


def sort_by_architecture(branch: list[dict]):
    packages_by_arch = {}
    for package in branch:
        arch = package['arch']
        name = package['name']
        if arch not in packages_by_arch:
            packages_by_arch[arch] = {}
        packages_by_arch[arch][name] = package
    return packages_by_arch


def evr_greater(e1, v1, r1, e2, v2, r2) -> bool:
    e1 = e1 or "0"
    e2 = e2 or "0"
    s1 = f"{e1}:{v1}-{r1}"
    s2 = f"{e2}:{v2}-{r2}"
    return vercmp(s1, s2) > 0


def compare_packages(branch1: dict, branch2: dict) -> dict:
    all_arches = set(branch1.keys()) | set(branch2.keys())
    comparison_result = {}

    for arch in all_arches:
        packages1 = branch1.get(arch, {})
        packages2 = branch2.get(arch, {})

        set1 = set(packages1.keys())
        set2 = set(packages2.keys())

        only_in_1 = list(set1 - set2)
        only_in_2 = list(set2 - set1)

        greater_in_1 = []

        common = set1 & set2
        for name in common:
            p1 = packages1[name]
            p2 = packages2[name]

            if evr_greater(
                p1.get('epoch'),
                p1['version'],
                p1['release'],
                p2.get('epoch'),
                p2['version'],
                p2['release'],
            ):
                greater_in_1.append(name)

        comparison_result[arch] = {
            "only_branch1": only_in_1,
            "only_branch2": only_in_2,
            "higher_version_in_branch1": greater_in_1,
        }

    return comparison_result

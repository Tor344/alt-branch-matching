from math import ceil

import click
from tabulate import tabulate

import src.branch_matching.api as api
import src.branch_matching.compare as compare


def echo_compact_table(result: dict) -> None:
    """
    Выводит пакеты в виде таблицы
    """
    for arch, info in result.items():
        click.secho(f"\nАрхитектура: {arch}", fg="cyan", bold=True)

        only1 = info.get("only_in_branch1", [])
        only2 = info.get("only_in_branch2", [])
        higher = info.get("higher_version_in_branch1", [])

        max_show = lambda lst: max(1, ceil(len(lst)/100))

        rows = []
        for pkg in only1[:max_show(only1)]:
            rows.append([pkg, "Только в первой ветке"])
        for pkg in only2[:max_show(only2)]:
            rows.append([pkg, "Только во второй ветке"])
        for pkg in higher[:max_show(higher)]:
            rows.append([pkg, "Версия выше в первой"])

        table = tabulate(rows, headers=["Пакет", "Категория"], tablefmt="github", showindex=True)
        click.echo(table)
        click.secho(f"Всего: в первой={len(only1)}, во второй={len(only2)}, выше версий={len(higher)}\n", fg="yellow")


@click.command()
@click.argument("branch1")
@click.argument("branch2")
def cli(branch1, branch2):
    packages1 = compare.sort_by_architecture(api.get_from_branch_binary_packages(branch1))
    packages2 = compare.sort_by_architecture(api.get_from_branch_binary_packages(branch2))

    result = compare.compare_packages(packages1, packages2)

    echo_compact_table(result)
    return result


if __name__ == "__main__":
    cli()


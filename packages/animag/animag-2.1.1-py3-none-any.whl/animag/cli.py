import argparse
import time
from typing import Dict, Any

from rich.console import Console
from rich.table import Table

from . import Anime, Searcher

console = Console()


def print_results(animes: list[Anime]) -> None:
    if not animes:
        console.print("[bold yellow]搜索结果为空[/bold yellow]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("序号", style="dim", justify="right", width=4)
    table.add_column("标题", style="dim", width=60, overflow="fold")
    table.add_column("大小", style="cyan", justify="right", width=10)

    for idx, anime in enumerate(animes, start=1):
        table.add_row(str(idx), anime.title, anime.size)

    console.print(table)


def get_user_selection(max_index: int) -> int:
    while True:
        try:
            index = int(input("选择一个并输入其序号 (输入 0 退出): "))
            if 0 <= index <= max_index:
                return index
            console.print(f"[bold red]请输入 0 到 {max_index} 之间的数字[/bold red]")

        except (ValueError, IndexError):
            console.print("[bold red]请输入有效的数字[/bold red]")


def main() -> None:
    parser = argparse.ArgumentParser(description="动漫磁力搜索工具:")

    parser.add_argument('-s', '--search', type=str, help='搜索关键词', required=True)
    parser.add_argument('-p', '--plugin', type=str, help='搜索使用的插件', default='dmhy')
    parser.add_argument('-c', '--collected', action='store_true', help='是否启用季度全集搜索')

    args = parser.parse_args()
    search_params: Dict[str, Any] = {'keyword': args.search, 'collected': args.collected}

    start_time = time.time()
    searcher = Searcher(plugin_name=args.plugin, no_search_errors=True)
    animes = searcher.search(**search_params)
    end_time = time.time()

    elapsed_time = end_time - start_time

    if animes:
        print_results(animes)
        console.print(f"[bold blue]搜索耗时: {elapsed_time:.2f} 秒[/bold blue]")

        selection = get_user_selection(len(searcher.animes))

        if selection > 0:
            anime = animes[selection - 1]
            console.print(f"[bold green]已选择 {anime.title}[/bold green]")
            console.print("[bold green]其磁链为: [/bold green][bold yellow]"
                          f"{anime.magnet if anime.magnet else '空'}[/bold yellow]",
                          overflow="fold")
            console.print("[bold green]其种子链接为: [/bold green][bold yellow]"
                          f"{anime.torrent if anime.torrent else '空'}[/bold yellow]",
                          overflow="fold")

        else:
            console.print("[bold yellow]已退出选择[/bold yellow]")
    else:
        console.print("[bold yellow]搜索结果为空[/bold yellow]")


if __name__ == '__main__':
    main()

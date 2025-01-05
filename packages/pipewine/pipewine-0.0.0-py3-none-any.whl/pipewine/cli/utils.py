import traceback
from collections import deque
from collections.abc import Sequence
from datetime import datetime
from typing import Any, overload

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from pipewine.cli.sinks import SinkCLIRegistry
from pipewine.cli.sources import SourceCLIRegistry
from pipewine.grabber import Grabber
from pipewine.sample import Sample
from pipewine.sinks import DatasetSink
from pipewine.sources import DatasetSource
from pipewine.workflows import CursesTracker, NoTracker, Workflow, run_workflow


def deep_get(sample: Sample, key: str) -> Any:
    sep = "."
    sub_keys = key.split(sep)
    item_key, other_keys = sub_keys[0], deque(sub_keys[1:])
    current = sample[item_key]()
    while len(other_keys) > 0:
        current_key = other_keys.popleft()
        if isinstance(current, Sequence):
            current = current[int(current_key)]
        else:
            current = current[current_key]
    return current


@overload
def _parse_source_or_sink(
    format_: str, text: str, reg: type[SourceCLIRegistry], grabber: Grabber
) -> DatasetSource: ...


@overload
def _parse_source_or_sink(
    format_: str, text: str, reg: type[SinkCLIRegistry], grabber: Grabber
) -> DatasetSink: ...


def _parse_source_or_sink(
    format_: str,
    text: str,
    reg: type[SourceCLIRegistry] | type[SinkCLIRegistry],
    grabber: Grabber,
) -> DatasetSource | DatasetSink:
    if format_ not in reg.registered:
        print(
            f"Format '{format_}' not found, use "
            "'pipewine op --format-help' to print available i/o formats."
        )
        exit(1)
    try:
        result = reg.registered[format_](text, grabber)
    except:
        print(
            f"Failed to parse string '{text}' into a '{format_}' format, use "
            "'pipewine op --format-help' to print available i/o formats and their "
            "usage."
        )
        exit(1)
    return result


def parse_source(format_: str, text: str, grabber: Grabber) -> DatasetSource:
    return _parse_source_or_sink(format_, text, SourceCLIRegistry, grabber)


def parse_sink(format_: str, text: str, grabber: Grabber) -> DatasetSink:
    return _parse_source_or_sink(format_, text, SinkCLIRegistry, grabber)


def parse_grabber(value: str) -> Grabber:
    sep = ","
    if sep in value:
        worker_str, _, prefetch_str = value.partition(sep)
        return Grabber(num_workers=int(worker_str), prefetch=int(prefetch_str))
    else:
        return Grabber(num_workers=int(value))


def _print_workflow_panel(
    start_time: datetime, text: str, style: str, body: str | None = None
) -> None:
    end_time = datetime.now()
    duration = end_time - start_time
    console = Console()
    message = Text(text, style=style)
    if body is not None:
        message.append(f"\n\n{body}", style="white not bold")
    message.append(f"\nStarted:  ")
    message.append(start_time.strftime("%Y-%m-%d %H:%M:%S"), style="white not bold")
    message.append(f"\nFinished: ")
    message.append(end_time.strftime("%Y-%m-%d %H:%M:%S"), style="white not bold")
    message.append(f"\nTotal duration: ")
    message.append(str(duration), style="white not bold")
    panel = Panel(
        message, title="Workflow Status", title_align="left", expand=False, style=style
    )
    console.print(panel)


def run_cli_workflow(workflow: Workflow, tui: bool = True) -> None:
    start_time = datetime.now()
    try:
        run_workflow(workflow, tracker=CursesTracker() if tui else NoTracker())
    except KeyboardInterrupt:
        _print_workflow_panel(start_time, "Workflow canceled.", "bold bright_black")
        exit(1)
    except Exception:
        _print_workflow_panel(
            start_time, "Workflow failed.", "bold red", body=traceback.format_exc()
        )
        exit(1)

    _print_workflow_panel(start_time, "Workflow completed successfully.", "bold green")

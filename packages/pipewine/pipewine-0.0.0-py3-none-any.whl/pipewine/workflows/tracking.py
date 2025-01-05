import curses
import time
from abc import ABC, abstractmethod
from collections import OrderedDict
from curses import window, wrapper
from dataclasses import dataclass, field
from threading import Thread

from pipewine.workflows.events import Event, EventQueue


@dataclass
class TrackingEvent(Event):
    task_id: str


@dataclass
class TaskStartEvent(TrackingEvent):
    total: int


@dataclass
class TaskUpdateEvent(TrackingEvent):
    unit: int


@dataclass
class TaskCompleteEvent(TrackingEvent):
    pass


class Tracker(ABC):
    @abstractmethod
    def attach(self, event_queue: EventQueue) -> None: ...

    @abstractmethod
    def detach(self) -> None: ...


@dataclass
class Task:
    name: str
    units: list[bool]
    complete: bool = False


@dataclass
class TaskGroup:
    name: str
    groups: OrderedDict[str, "TaskGroup"] = field(default_factory=OrderedDict)
    tasks: OrderedDict[str, Task] = field(default_factory=OrderedDict)


class NoTracker(Tracker):  # pragma: no cover (useless)
    def attach(self, event_queue: EventQueue) -> None:
        return

    def detach(self) -> None:
        return


class CursesTracker(Tracker):
    MAX_COLOR = 1000

    def __init__(self, refresh_rate: float = 0.1) -> None:
        super().__init__()
        self._refresh_rate = refresh_rate
        self._n_shades = 10

        self._eq: EventQueue | None = None
        self._thread: Thread | None = None
        self._stop_flag = False

    def attach(self, event_queue: EventQueue) -> None:
        if self._eq is not None or self._thread is not None:
            raise RuntimeError("Already attached to another event queue.")
        self._eq = event_queue
        self._thread = Thread(target=self._loop)
        self._stop_flag = False
        self._thread.start()

    def detach(self) -> None:
        if self._eq is None or self._thread is None:
            raise RuntimeError("Not attached to any event queue.")
        self._stop_flag = True
        self._thread.join()
        self._thread = None
        self._eq = None

    def _get_group(self, group: TaskGroup, path: str) -> TaskGroup:
        path_chunks = path.split("/")
        for p in path_chunks:
            if p not in group.groups:
                group.groups[p] = TaskGroup(p)
            group = group.groups[p]
        return group

    def _spawn_task(self, group: TaskGroup, path: str, total: int) -> Task:
        group_path, _, task_name = path.rpartition("/")
        units = [False for _ in range(total)]
        task = Task(task_name, units)
        group = self._get_group(group, group_path)
        group.tasks[task_name] = task
        return task

    def _get_task(self, group: TaskGroup, path: str) -> Task:
        group_path, _, task_name = path.rpartition("/")
        group = self._get_group(group, group_path)
        return group.tasks[task_name]

    def _preorder(
        self, group: TaskGroup, depth: int
    ) -> list[tuple[int, Task | TaskGroup]]:
        next = depth + 1
        result: list[tuple[int, Task | TaskGroup]] = [(depth, group)]
        for tg in group.groups.values():
            result.extend(self._preorder(tg, depth=next))
        for task in group.tasks.values():
            result.append((next, task))
        return result

    def _compute_bar(self, units: list[bool], width: int) -> list[list[int]]:
        if len(units) < width:
            bar = []
            div = width // len(units)
            rem = width % len(units)
            for ui, unit in enumerate(units):
                bar.append([div + int(ui < rem), int(unit), 1])
        else:
            bar = [[1, 0, 0] for _ in range(width)]
            for ui, unit in enumerate(units):
                cell = bar[int(ui / len(units) * len(bar))]
                cell[1] += int(unit)
                cell[2] += 1
        return bar

    def _init_colors(self) -> None:
        curses.start_color()
        curses.use_default_colors()
        if curses.can_change_color():
            for i in range(self._n_shades):
                c = int((float(i + 1) / self._n_shades) * self.MAX_COLOR)
                curses.init_color(i + 1, c, c, c)
                curses.init_pair(i + 1, i + 1, -1)
        else:
            self._n_shades = 5
            curses.init_pair(1, curses.COLOR_BLACK, -1)
            curses.init_pair(2, curses.COLOR_RED, -1)
            curses.init_pair(3, curses.COLOR_YELLOW, -1)
            curses.init_pair(4, curses.COLOR_GREEN, -1)
            curses.init_pair(5, curses.COLOR_WHITE, -1)

    def _color_of(self, frac: float) -> int:
        return curses.color_pair(1 + int(frac * (self._n_shades - 1)))

    def _render_tasks(
        self,
        screen: window,
        tasks: list[tuple[int, Task | TaskGroup]],
        global_step: int,
    ) -> None:
        screen.clear()
        bar_elem = "██"
        H, W = screen.getmaxyx()
        TITLE_H, TITLE_W = len(tasks), min(20, W - 1)
        PROG_H = TITLE_H
        PROG_W = W - TITLE_W
        padding = 0
        for _, entry in tasks:
            if isinstance(entry, Task):
                padding_i = len(str(len(entry.units))) * 2 + 1 + 11
                padding = max(padding, padding_i)
        bar_w = (PROG_W - padding) // len(bar_elem)
        title_pad = curses.newpad(TITLE_H, TITLE_W)
        prog_pad = curses.newpad(PROG_H, PROG_W)
        for i, (depth, entry) in enumerate(tasks):
            space = TITLE_W - 2 * depth - 1
            text = entry.name
            if len(text) > space:
                start = (global_step // 2) % (len(text) - space)
                text = text[start : start + space]
            title_pad.addstr(i, 2 * depth, text)
            if isinstance(entry, Task):
                j = 0
                if entry.complete:
                    color = self._color_of(1.0)
                    if bar_w > 0:
                        prog_pad.addstr(i, 0, bar_elem * bar_w, color)
                        j += len(bar_elem) * bar_w
                    sum_ = len(entry.units)
                else:
                    if bar_w > 0:
                        for size, comp, total in self._compute_bar(entry.units, bar_w):
                            color = self._color_of(comp / total)
                            prog_pad.addstr(i, j, bar_elem * size, color)
                            j += size * len(bar_elem)
                    sum_ = sum(entry.units)
                total = len(entry.units)
                perc = round((sum_ / total) * 100, 2)
                text = f"{sum_}/{total} {perc}%"
                if len(text) + 2 < PROG_W:
                    prog_pad.addstr(i, j + 2, text)

        title_pad.noutrefresh(max(0, TITLE_H - H), 0, 0, 0, H - 1, W - 1)
        prog_pad.noutrefresh(max(0, TITLE_H - H), 0, 0, TITLE_W, H - 1, W - 1)
        curses.doupdate()

    def _curses(self, stdscr: window) -> None:
        self._init_colors()
        em = self._eq
        assert em is not None
        root = TaskGroup("__root__")
        global_step = -1
        while not self._stop_flag:
            time.sleep(self._refresh_rate)
            global_step = global_step + 1 % 10000
            while (event := em.capture()) is not None:
                if isinstance(event, TaskStartEvent):
                    task = self._spawn_task(root, event.task_id, event.total)
                elif isinstance(event, TaskUpdateEvent):
                    task = self._get_task(root, event.task_id)
                    task.units[event.unit] = True
                elif isinstance(event, TaskCompleteEvent):
                    task = self._get_task(root, event.task_id)
                    task.complete = True

            list_of_tasks = self._preorder(root, -1)[1:]
            if len(list_of_tasks) == 0:
                continue

            self._render_tasks(stdscr, list_of_tasks, global_step)

    def _loop(self) -> None:
        wrapper(self._curses)

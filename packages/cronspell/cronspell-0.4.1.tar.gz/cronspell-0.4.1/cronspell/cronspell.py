# SPDX-FileCopyrightText: 2024-present iilei • jochen preusche <922226+iilei@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT


import calendar
import functools
from datetime import datetime, timedelta
from pathlib import Path
from typing import Callable, Optional
from zoneinfo import ZoneInfo

from textx import metamodel_from_file

from cronspell.exceptions import CronpellMathException

TIMEZONE_DEFAULT = "UTC"

with calendar.different_locale(locale=("EN_US", "UTF-8")):
    # first day of the week: Monday as per ISO Standard
    WEEKDAYS = [*calendar.day_abbr]


DELTA_MAP = {"d": 86400, "H": 3600, "M": 60, "S": 1}
TIME_RESETS_MAP: list = [
    ["Y", ["year", 1970]],
    ["m", ["month", 1]],
    ["CW", [None, None]],
    ["W", [None, None]],
    ["d", ["day", 1]],
    ["H", ["hour", 0]],
    ["M", ["minute", 0]],
    ["S", ["second", 0]],
]
FLOOR_CW_MAX = 52
FLOOR_Y_MAX = 9999
TIME_UNITS_SHORT = [x[0] for x in TIME_RESETS_MAP]


def find_by_isoweek(current, resolution):
    year_boundary_safe_max_checks = resolution * 2
    # backwards iterate / find a date satisfiying the resolution request
    return next(
        filter(
            lambda date: date.isocalendar().week % resolution == 0,
            [current - timedelta(days=(7 * x)) for x in range(0, year_boundary_safe_max_checks)],
        )
    )


def get_delta(unit, multiplier):
    return timedelta(0, multiplier * (DELTA_MAP[unit]))


class Cronspell:
    def __init__(self, timezone: Optional[ZoneInfo] = None):
        if timezone is None:
            timezone = ZoneInfo(TIMEZONE_DEFAULT)

        self.meta_model_src = Path.joinpath(Path(__file__).parent, "cronspell.tx")
        self.meta_model = metamodel_from_file(self.meta_model_src, use_regexp_group=True)
        self.timezone = timezone
        self._now_fun = datetime.now

    def parse_anchor(self):
        anchor = getattr(self.model, "anchor", None)
        isodate = getattr(anchor, "isodate", None)
        if isodate:
            return datetime.fromisoformat(isodate).astimezone(self.timezone)

        tz = getattr(getattr(anchor, "tznow", None), "tz", None)
        return self._now_fun().astimezone(ZoneInfo(tz) if tz else self.timezone)

    @property
    def now_func(self) -> Callable[..., datetime]:
        return self._now_fun

    @now_func.setter
    def now_func(self, fun: Callable[..., datetime]):
        self._now_fun = fun

    @staticmethod
    def get_time_unit(alias):
        return next(name for name in [*TIME_UNITS_SHORT, *WEEKDAYS] if getattr(alias, name, None))

    def step(self, current, step):
        # operation ~> Minus|Plus|Floor|Ceil
        operation = step.statement._tx_fqn.rpartition(".")[-1]

        # Year Modulo
        if operation == "YModulo":
            resolution = max(step.statement.value, 1)

            if resolution > FLOOR_Y_MAX:
                msg = f"Year Modulo needed lower than {FLOOR_Y_MAX + 1}! Got {resolution}."
                raise CronpellMathException(msg)

            year = current.isocalendar().year // resolution * resolution

            return datetime(year, 1, 1, tzinfo=ZoneInfo(self.tz))

        # Calendar Week Modulo
        elif operation == "CwModulo":
            resolution = max(step.statement.value, 1)

            if resolution > FLOOR_CW_MAX:
                msg = f"Calendar Week Modulo needed lower than {FLOOR_CW_MAX + 1}! Got {resolution}."
                raise CronpellMathException(msg)

            # find date in isoweek matching the desired resolution
            current = find_by_isoweek(current, resolution)
            current -= timedelta(days=current.timetuple().tm_wday)
            return current.replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            resolution = step.statement.res._tx_fqn.rpartition(".")[-1]
            time_unit = self.get_time_unit(step.statement.res)

        if operation in {"Plus", "Minus"}:
            """
            Determine the Delta first
            """
            if time_unit == "W":
                delta = (datetime.strptime("2", "%d") - datetime.strptime("1", "%d")) * (
                    (-7 if operation == "Minus" else 7) * step.statement.steps
                )
            else:
                delta = get_delta(time_unit, ((-1 if operation == "Minus" else 1) * step.statement.steps))

            """
            Return with added delta
            """
            return current + delta

        """
        At this stage, the operation to be done cannot be other than "Floor".
        If a specific day of the week is desired, we need to take the offset
        into account:
        """
        if resolution == "WeekDay":
            offset_abs = (7 + (current.weekday() - WEEKDAYS.index(time_unit))) % 7
            offset = (-1 * offset_abs) if operation == "Floor" else (7 - offset_abs)
            current += timedelta(days=offset)

            # operation "Floor" to be performed as per day, therefor:
            time_unit = "d"

        """
        Flooring by 'prune' the units of time that are more specific than needed:
        """
        prune = TIME_UNITS_SHORT[TIME_UNITS_SHORT.index(time_unit) + 1 :]
        current = current.replace(**dict([x[1] for x in TIME_RESETS_MAP if x[0] in prune and x[1][0]]))
        return current

    def parse(self, expression: str = "now") -> datetime:
        self.expression = expression
        self.model = self.meta_model.model_from_str(expression)
        self.anchor = self.parse_anchor().replace(microsecond=0)

        self.tz = self.anchor.tzinfo.key

        if getattr(getattr(self.model, "formula", None), "_tx_fqn", None) == "cronspell.DateMatSet":
            candidates = sorted(
                [
                    functools.reduce(self.step, [*getattr(formula, "date_math_term", [])], self.anchor)
                    for formula in self.model.formula.set
                ]
            )

            # get candidate closest to anchor, prioritizing the past
            return [None, *[c for c in candidates if c <= self.anchor]].pop() or candidates[0]

        return functools.reduce(
            self.step, [*getattr(getattr(self.model, "formula", None), "date_math_term", [])], self.anchor
        )

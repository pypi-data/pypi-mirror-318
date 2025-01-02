# python-snaptime

<!-- ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-snaptime) -->
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/dtomlinson91/python-snaptime/codacy.yml?style=flat-square)
![Codacy coverage](https://img.shields.io/codacy/coverage/d252742da60f4d90b72aa7d7de1a7a2f?style=flat-square)
![Codacy grade](https://img.shields.io/codacy/grade/d252742da60f4d90b72aa7d7de1a7a2f?style=flat-square)


Inspired by Splunk's [relative time modifiers](http://docs.splunk.com/Documentation/Splunk/latest/SearchReference/SearchTimeModifiers#How_to_specify_relative_time_modifiers), `python-snaptime` will transform `datetime` objects using relative time modifiers.

For example, `@d-2h` will give you two hours ago from the start of the day.

- Use snaptime strings to get relative dates/times for a given datetime.
- Timezone aware.
- Effortlessly handles daylight savings using [pendulum](https://github.com/python-pendulum/pendulum).
- Can snap backwards in time to the nearest second, minute, hour, day, week, month, quarter or year.
- Can add/subtract microseconds, milliseconds, seconds, minutes, hours, days, weeks, months, quarters or years.
- Chain snaps together as needed e.g `@d-12h+10m@h`.
- Use either a snaptime string, or use Python to define snaptimes ([see advanced example](#advanced)).
- Fully type annotated for IDE completion.

> [!NOTE]
> This package was created as a more up to date replacement for [zartstrom/snaptime](https://github.com/zartstrom/snaptime), which is long since abandoned.

## Snaptime strings

| Unit          | Strings                                   | Supports Snapping? | Supports Delta? |
| :------------ | :---------------------------------------- | :----------------: | :-------------: |
| `MICROSECOND` | `us`, `microsecond`, `microseconds`       |         ❌         |       ✅        |
| `MILLISECOND` | `ms`, `millisecond`, `milliseconds`       |         ❌         |       ✅        |
| `SECOND`      | `s`, `sec`, `secs`, `second`, `seconds`   |         ✅         |       ✅        |
| `MINUTE`      | `m`, `min`, `mins`, `minute`, `minutes`   |         ✅         |       ✅        |
| `HOUR`        | `h`, `hr`, `hrs`, `hour`, `hours`         |         ✅         |       ✅        |
| `DAY`         | `d`, `day`, `days`                        |         ✅         |       ✅        |
| `WEEK`        | `w`, `week`, `weeks`                      |         ✅         |       ✅        |
| `MONTH`       | `mon`, `month`, `months`                  |         ✅         |       ✅        |
| `QUARTER`     | `q`, `qtr`, `qtrs`, `quarter`, `quarters` |         ✅         |       ✅        |
| `YEAR`        | `y`, `yr`, `yrs`, `year`, `years`         |         ✅         |       ✅        |

## Examples

### Timezones

Using `pendulum` timezones are handled easily.

```python
>>> import pendulum
>>> from python_snaptime import snap

>>> dtm = pendulum.datetime(2024, 12, 30, 18, 0, 0)
>>> snap(dtm, "@d-12h")
DateTime(2024, 12, 29, 12, 0, 0, tzinfo=Timezone('UTC'))
```

```python
>>> import pendulum
>>> from python_snaptime import snap

>>> dtm = pendulum.datetime(2024, 12, 30, 18, 0, 0, tz=pendulum.timezone("Europe/London"))
>>> snap(dtm, "@d-12h")
DateTime(2024, 12, 29, 12, 0, 0, tzinfo=Timezone('Europe/London'))
```

### DST

`pendulum` makes working around DST easy

```python
>>> import pendulum
>>> from python_snaptime import snap

>>> dtm = pendulum.datetime(2024, 10, 27, 1, 59, 59, tz="Europe/London", fold=0)
>>> snap(dtm, "+1s")
DateTime(2024, 10, 27, 1, 0, 0, tzinfo=Timezone('Europe/London'))  # pre-transition
```

```python
>>> import pendulum
>>> from python_snaptime import snap

>>> dtm = pendulum.datetime(2024, 10, 27, 1, 59, 59, tz="Europe/London", fold=1)
>>> snap(dtm, "+1s")
DateTime(2024, 10, 27, 2, 0, 0, tzinfo=Timezone('Europe/London'))  # post-transition (default)
```

### datetime

Don't care about timezones/want to use builtin `datetime.datetime`?

```python
>>> from datetime import datetime
>>> from python_snaptime import snap

>>> dtm = datetime(2024, 12, 30, 18, 0, 0)
>>> snap(dtm, "@d-12h")
datetime.datetime(2024, 12, 29, 12, 0)
```

Can also work with builtin timezone aware datetimes

```python
>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo
>>> from python_snaptime import snap

>>> dtm = datetime(2024, 12, 30, 18, 0, 0, tzinfo=ZoneInfo("Europe/London"))
>>> snap(dtm, "@d-12h")
datetime.datetime(2024, 12, 29, 12, 0, tzinfo=Timezone('Europe/London'))
```

## Installation

### pypi

```sh
# using poetry
poetry add python-snaptime

# using pip
pip install python-snaptime
```

## Usage

```python
import pendulum
from python_snaptime import snap

snapped_datetime = snap(pendulum.now(), "@d-2h+10m")
```

### Advanced

You can programmatically calculate snaptimes without a snaptime string, e.g the equivalent of `@d-2h+10m` is:

```python
import pendulum

from python_snaptime.handlers import handle_timesnapping
from python_snaptime.models import Action, Snaptime, Unit


def main():
    datetime = pendulum.now()
    time_snapping_operations = [
        Snaptime(action=Action.SNAP, unit=Unit.DAY),
        Snaptime(action=Action.SUB, unit=Unit.HOUR, time_int=2),
        Snaptime(action=Action.ADD, unit=Unit.MINUTE, time_int=10),
    ]
    for operation in time_snapping_operations:
        datetime = handle_timesnapping(operation, datetime)
    print(datetime)  # `@d-2h+10m`


if __name__ == "__main__":
    main()

```

import pendulum


def now(tz: str | pendulum.Timezone = None) -> pendulum.DateTime:
    return pendulum.now(tz=tz)


def past(
    years: int | None = 0,
    months: int | None = 0,
    weeks: int | None = 0,
    days: int | None = 0,
    hours: int | None = 0,
    minutes: int | None = 0,
    seconds: float | None = 0,
    microseconds: int | None = 0,
    tz: pendulum.Timezone | None = None,
) -> pendulum.DateTime:
    """
    Return a datetime in the past.

    The returned datetime is the result of subtracting the given duration from the
    current datetime. The duration can be specified in years, months, weeks, days,
    hours, minutes, seconds, or microseconds. If a duration is not specified, it
    is assumed to be zero.

    Args:
        years: The number of years to subtract.
        months: The number of months to subtract.
        weeks: The number of weeks to subtract.
        days: The number of days to subtract.
        hours: The number of hours to subtract.
        minutes: The number of minutes to subtract.
        seconds: The number of seconds to subtract.
        microseconds: The number of microseconds to subtract.
        tz: The timezone to use for the returned datetime. If ``None``, the local
            timezone is used.

    Returns:
        A datetime in the past, calculated by subtracting the given duration from
        the current datetime.
    """
    return pendulum.now(tz=tz).subtract(
        years=years,
        months=months,
        weeks=weeks,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=microseconds,
    )


def future(
    years: int | None = 0,
    months: int | None = 0,
    weeks: int | None = 0,
    days: int | None = 0,
    hours: int | None = 0,
    minutes: int | None = 0,
    seconds: float | None = 0,
    microseconds: int | None = 0,
    tz: pendulum.Timezone | None = None,
) -> pendulum.DateTime:
    """
    Return a datetime in the future.

    The returned datetime is the result of adding the given duration to the current
    datetime. The duration can be specified in years, months, weeks, days, hours,
    minutes, seconds, or microseconds. If a duration is not specified, it is assumed
    to be zero.

    Args:
        years: The number of years to add.
        months: The number of months to add.
        weeks: The number of weeks to add.
        days: The number of days to add.
        hours: The number of hours to add.
        minutes: The number of minutes to add.
        seconds: The number of seconds to add.
        microseconds: The number of microseconds to add.
        tz: The timezone to use for the returned datetime. If ``None``, the local
            timezone is used.

    Returns:
        A datetime in the future, calculated by adding the given duration to the
        current datetime.
    """
    return pendulum.now(tz=tz).add(
        years=years,
        months=months,
        weeks=weeks,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=microseconds,
    )

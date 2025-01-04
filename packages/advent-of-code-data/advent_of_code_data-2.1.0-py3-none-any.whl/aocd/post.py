from __future__ import annotations

import logging
import typing as t

from .get import current_day
from .get import most_recent_year
from .models import default_user
from .models import Puzzle
from .models import User
from .types import AnswerValue
from .types import PuzzlePart

if t.TYPE_CHECKING:
    from urllib3 import BaseHTTPResponse


log: logging.Logger = logging.getLogger(__name__)


def submit(
    answer: AnswerValue,
    part: PuzzlePart | None = None,
    day: int | None = None,
    year: int | None = None,
    session: str | None = None,
    reopen: bool = True,
    quiet: bool = False,
) -> BaseHTTPResponse | None:
    """
    Submit your answer to adventofcode.com, and print the response to the terminal.
    The only required argument is `answer`, all others can usually be introspected
    from the caller of submit, and whether part b has already been unlocked.
    `answer` can be a string or a number (numbers will be coerced into strings).

    Results are only submitted to the server if the puzzle has not been solved already.
    Additionally, aocd has some internal checks to prevent submitting the same answer
    twice, and to prevent submitting answers which are certain to be incorrect.

    The result of the submission is printed to the terminal. Pass `quiet=True` to
    suppress the printout.

    If it was necessary to POST to adventofcode.com, the HTTP response from the server
    is returned as a `urllib3.HTTPResponse` instance, otherwise the return is None.

    When `reopen` is True (the default), and the puzzle was just solved correctly, this
    function will automatically open/refresh the puzzle page in a new browser tab so
    that you can read the next part quickly. Pass `reopen=False` to suppress this
    feature.
    """
    if session is None:
        user = default_user()
    else:
        user = User(token=session)
    if day is None:
        day = current_day()
    if year is None:
        year = most_recent_year()
    puzzle = Puzzle(year=year, day=day, user=user)
    if part is None:
        # guess if user is submitting for part a or part b,
        # based on whether part a is already solved or not
        answer_a = getattr(puzzle, "answer_a", None)
        if answer_a is None:
            log.warning("submitting for part a")
            part = "a"
        else:
            log.warning(
                "submitting for part b (part a already completed with %r)",
                answer_a,
            )
            part = "b"
    response = puzzle._submit(value=answer, part=part, reopen=reopen, quiet=quiet)
    return response

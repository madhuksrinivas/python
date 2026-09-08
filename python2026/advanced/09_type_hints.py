# ─────────────────────────────────────────────
# ADV 09 — Type Hints (Python 3.5+)
# ─────────────────────────────────────────────
#
# WHAT ARE TYPE HINTS?
#   Type hints let you annotate variables and functions with
#   their expected types: def greet(name: str) -> str
#   Python itself does NOT enforce them at runtime — they are
#   documentation for humans and tools. Static analysers like
#   mypy and pyright read them to catch bugs before you even
#   run the code. Type hints are now standard practice in
#   professional Python development.
# ─────────────────────────────────────────────

# Type hints do NOT enforce types at runtime — they are hints for
# static analysers (mypy, pyright) and human readers.

from typing import Optional, Union, Any, Callable
from typing import List, Dict, Tuple, Set   # pre-3.9 style
# From Python 3.9+ you can write list[str], dict[str, int] directly.


# ── 1. Basic variable & function annotations ─

name:  str  = "Alice"
age:   int  = 30
score: float = 9.5
flag:  bool = True


def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def no_return() -> None:
    print("side effect only")


# ── 2. Collection types ──────────────────────

def sum_list(numbers: list[int]) -> int:
    return sum(numbers)

def get_capitals() -> dict[str, str]:
    return {"Kenya": "Nairobi", "France": "Paris"}

def first_last(items: list[str]) -> tuple[str, str]:
    return items[0], items[-1]

def unique_tags(tags: list[str]) -> set[str]:
    return set(tags)


# ── 3. Optional — value or None ──────────────

def find_user(user_id: int) -> Optional[str]:   # str | None
    db = {1: "Alice", 2: "Bob"}
    return db.get(user_id)                      # returns None if missing

print(find_user(1))    # Alice
print(find_user(99))   # None


# ── 4. Union — one of several types ──────────

def double(value: Union[int, float]) -> Union[int, float]:
    return value * 2

# Python 3.10+ shorthand with |
def double_modern(value: int | float) -> int | float:
    return value * 2


# ── 5. Callable ──────────────────────────────

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

print(apply(add, 3, 7))    # 10


# ── 6. TypeVar — generic functions ───────────

from typing import TypeVar

T = TypeVar("T")

def first_item(items: list[T]) -> T:
    return items[0]

print(first_item([1, 2, 3]))       # 1  (inferred as int)
print(first_item(["a", "b"]))      # a  (inferred as str)


# ── 7. TypedDict — dict with known structure ─

from typing import TypedDict

class Movie(TypedDict):
    title:  str
    year:   int
    rating: float

def display_movie(movie: Movie) -> str:
    return f"{movie['title']} ({movie['year']}) — {movie['rating']:.1f}/10"

m: Movie = {"title": "Inception", "year": 2010, "rating": 8.8}
print(display_movie(m))


# ── 8. Annotated & Literal ────────────────────

from typing import Annotated, Literal

# Annotated — attach metadata (used by FastAPI, Pydantic, etc.)
PositiveInt = Annotated[int, "must be > 0"]

def set_age(age: PositiveInt) -> None:
    if age <= 0:
        raise ValueError("Age must be positive")
    print(f"Age set to {age}")

# Literal — restrict to specific values
Direction = Literal["north", "south", "east", "west"]

def move(direction: Direction, steps: int) -> str:
    return f"Moving {direction} by {steps} steps"

print(move("north", 5))


# ── 9. Protocol — structural subtyping ────────

from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...   # interface definition

class Circle:
    def draw(self) -> str:
        return "Drawing a circle"

class Square:
    def draw(self) -> str:
        return "Drawing a square"

def render(shape: Drawable) -> None:
    print(shape.draw())

render(Circle())    # Drawing a circle
render(Square())    # Drawing a square
# No inheritance needed — just implement the method!


# ── 10. Running mypy ─────────────────────────
# Install:   pip install mypy
# Check:     mypy 09_type_hints.py
#
# Example error mypy would catch:
#
#   def add(a: int, b: int) -> int: return a + b
#   add("hello", 5)  → error: Argument 1 has type "str", expected "int"


# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   var: Type = value               — variable annotation
#   def f(x: int) -> str            — function annotation
#   Optional[T]  / T | None         — nullable type
#   Union[A, B]  / A | B            — multiple types
#   list[T] dict[K,V] tuple[A,B]    — generic collections
#   TypeVar                         — generic functions
#   TypedDict                       — typed dict shape
#   Protocol                        — structural typing
# ─────────────────────────────────────────────

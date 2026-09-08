# ─────────────────────────────────────────────
# ADV 06 — Generators & Iterators
# ─────────────────────────────────────────────
#
# WHAT IS A GENERATOR?
#   A generator is a special function that produces values
#   one at a time using the 'yield' keyword instead of
#   returning them all at once. It pauses after each yield
#   and resumes from the same point when asked for the next
#   value. This makes generators incredibly memory-efficient
#   — you can process a billion-row dataset without loading
#   it all into RAM.
# ─────────────────────────────────────────────

# ── 1. Custom iterator using __iter__ / __next__ ──
class CountUp:
    def __init__(self, start, stop):
        self.current = start
        self.stop    = stop

    def __iter__(self):
        return self           # the object is its own iterator

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for n in CountUp(1, 6):
    print(n, end=" ")       # 1 2 3 4 5
print()


# ── 2. Generator function (yield) ────────────
# A generator function returns a generator object.
# It runs up to the next yield, pauses, then resumes.

def count_up(start, stop):
    current = start
    while current < stop:
        yield current       # pause here, return value to caller
        current += 1

gen = count_up(1, 6)
print(next(gen))            # 1
print(next(gen))            # 2
print(list(gen))            # [3, 4, 5]  — consume the rest

# Generators are lazy — values produced on demand
for n in count_up(1, 100_000_000):
    if n > 5:
        break
    print(n, end=" ")
print()                     # 1 2 3 4 5  — only 6 values computed!


# ── 3. Infinite generator ────────────────────
def integers_from(n):
    while True:
        yield n
        n += 1

gen = integers_from(10)
for _ in range(5):
    print(next(gen), end=" ")   # 10 11 12 13 14
print()


# ── 4. yield from ────────────────────────────
def chain(*iterables):
    for it in iterables:
        yield from it           # delegate to sub-iterable

for x in chain([1, 2], "abc", range(3)):
    print(x, end=" ")           # 1 2 a b c 0 1 2
print()


# ── 5. Generator expressions ─────────────────
squares = (x**2 for x in range(1, 11))   # lazy, no list in memory
print(sum(squares))                       # 385

# Generator pipeline — each stage is lazy
def read_lines(path):
    with open(path) as f:
        yield from f

# (Uncomment with a real file)
# lines  = read_lines("data.csv")
# stripped = (line.strip() for line in lines)
# non_empty = (line for line in stripped if line)
# first_10 = (next(non_empty) for _ in range(10))


# ── 6. send() — two-way generators ──────────
def accumulator():
    total = 0
    while True:
        value = yield total     # yield sends total out, receives value back
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)                       # prime the generator (advance to first yield)
print(acc.send(10))             # 10
print(acc.send(20))             # 30
print(acc.send(5))              # 35


# ── 7. throw() and close() ───────────────────
def gen_with_cleanup():
    try:
        while True:
            yield
    except GeneratorExit:
        print("Generator closed — cleanup done")
    except ValueError as e:
        print(f"ValueError received: {e}")
        yield "recovered"

g = gen_with_cleanup()
next(g)
g.throw(ValueError, "bad data")   # ValueError received: bad data
# next(g)  → StopIteration (after yield "recovered")

g2 = gen_with_cleanup()
next(g2)
g2.close()    # Generator closed — cleanup done


# ── 8. itertools — powerful iterator tools ───
import itertools

# count, cycle, repeat
for n in itertools.islice(itertools.count(1), 5):
    print(n, end=" ")           # 1 2 3 4 5
print()

colors = itertools.cycle(["red", "green", "blue"])
for _ in range(6):
    print(next(colors), end=" ")  # red green blue red green blue
print()

# chain
print(list(itertools.chain([1, 2], [3, 4], [5])))   # [1, 2, 3, 4, 5]

# combinations and permutations
print(list(itertools.combinations("ABC", 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

print(list(itertools.permutations("ABC", 2)))
# [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]

# product (cartesian product)
print(list(itertools.product([0, 1], repeat=3)))
# [(0,0,0), (0,0,1), ... (1,1,1)]  — 8 combos

# groupby — group consecutive equal values
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("A", 5)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# A [('A', 1), ('A', 2)]
# B [('B', 3), ('B', 4)]
# A [('A', 5)]

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   yield              — turn a function into a generator
#   next() / iter()    — advance an iterator
#   yield from         — delegate to sub-iterable
#   send()             — pass values into a generator
#   itertools          — powerful iterator combinators
#   Lazy evaluation    — compute values only when needed
# ─────────────────────────────────────────────

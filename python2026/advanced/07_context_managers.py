# ─────────────────────────────────────────────
# ADV 07 — Context Managers  (with statement)
# ─────────────────────────────────────────────
#
# WHAT IS A CONTEXT MANAGER?
#   A context manager is an object that sets something up
#   before a block of code runs and tears it down afterwards
#   — guaranteed, even if an error occurs.
#   The 'with' statement is how you use one:
#       with open("file.txt") as f:
#           data = f.read()
#   Here the file is automatically closed when the block ends.
#   Context managers eliminate the need for scattered try/finally.
# ─────────────────────────────────────────────

# ── Why context managers? ────────────────────
# They guarantee cleanup code runs even if an exception occurs.
# Replaces try/finally boilerplate.

# ── 1. Built-in: file I/O ────────────────────
with open("/tmp/py2026_ctx.txt", "w") as f:
    f.write("Hello from context manager!\n")
# file is automatically closed here — even if an exception occurred

# ── 2. Multiple resources in one with ────────
with open("/tmp/py2026_src.txt", "w") as src, \
     open("/tmp/py2026_dst.txt", "w") as dst:
    src.write("source file\n")
    dst.write("destination file\n")

# ── 3. Class-based context manager ───────────
# Implement __enter__ and __exit__

class ManagedFile:
    def __init__(self, path, mode="r"):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening {self.path}")
        self.file = open(self.path, self.mode)
        return self.file               # value assigned to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.path}")
        if self.file:
            self.file.close()
        # Return True to suppress the exception; False (default) to propagate
        return False

with ManagedFile("/tmp/py2026_ctx.txt") as f:
    print(f.read())


# ── 4. Timer context manager ─────────────────
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.6f}s")

with Timer() as t:
    result = sum(range(1_000_000))

print(f"Sum: {result}, Time: {t.elapsed:.6f}s")


# ── 5. contextlib.contextmanager decorator ───
# Easier way to write context managers using generators.
from contextlib import contextmanager

@contextmanager
def managed_file(path, mode="r"):
    print(f"Opening {path}")
    f = open(path, mode)
    try:
        yield f                    # code inside 'with' block runs here
    finally:
        print(f"Closing {path}")
        f.close()

with managed_file("/tmp/py2026_ctx.txt") as f:
    print(f.read().strip())


@contextmanager
def timer():
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"Block took {elapsed:.6f}s")

with timer():
    _ = [x**2 for x in range(100_000)]


# ── 6. contextlib utilities ──────────────────
from contextlib import suppress, redirect_stdout
import io

# suppress — silently ignore specific exceptions
with suppress(FileNotFoundError):
    open("/tmp/nonexistent_file_xyz.txt")
print("No crash — FileNotFoundError was suppressed")

# redirect_stdout — capture print output
buffer = io.StringIO()
with redirect_stdout(buffer):
    print("This goes to the buffer, not the console")
captured = buffer.getvalue()
print("Captured:", captured.strip())


# ── 7. Nested context managers with ExitStack ─
from contextlib import ExitStack

files_to_open = ["/tmp/py2026_ctx.txt", "/tmp/py2026_src.txt"]

with ExitStack() as stack:
    handles = [stack.enter_context(open(p)) for p in files_to_open]
    for fh in handles:
        print(fh.readline().strip())
# All files closed automatically when the block exits


# ── 8. Database transaction pattern ──────────
class DatabaseConnection:
    """Simulated DB connection showing the transaction pattern."""
    def __init__(self, dsn):
        self.dsn = dsn

    def __enter__(self):
        print(f"Connecting to {self.dsn}")
        print("BEGIN TRANSACTION")
        return self

    def execute(self, query):
        print(f"  Executing: {query}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("COMMIT")
        else:
            print(f"ROLLBACK (due to {exc_type.__name__})")
        print("Disconnecting")
        return False    # don't suppress exceptions

with DatabaseConnection("postgresql://localhost/mydb") as db:
    db.execute("INSERT INTO users (name) VALUES ('Alice')")
    db.execute("UPDATE accounts SET balance = balance - 100")
# COMMIT and Disconnect happen automatically

import os
for p in ["/tmp/py2026_ctx.txt", "/tmp/py2026_src.txt", "/tmp/py2026_dst.txt"]:
    if os.path.exists(p):
        os.remove(p)

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   with statement        — guarantees __exit__ runs
#   __enter__ / __exit__  — class-based context manager
#   @contextmanager       — generator-based (easier)
#   suppress()            — silence specific exceptions
#   ExitStack             — dynamic number of contexts
# ─────────────────────────────────────────────

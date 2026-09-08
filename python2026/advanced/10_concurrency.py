# ─────────────────────────────────────────────
# ADV 10 — Concurrency & async/await
# ─────────────────────────────────────────────
#
# WHAT IS CONCURRENCY?
#   Concurrency means doing multiple things at (roughly) the
#   same time. A program that downloads 10 files one-by-one
#   takes 10x longer than one that downloads them all at once.
#   Python offers three models:
#     Threading      — multiple threads, good for I/O-bound work
#     Multiprocessing— multiple CPU cores, good for CPU-bound work
#     asyncio        — single thread, cooperative scheduling,
#                       best for huge numbers of I/O operations
# ─────────────────────────────────────────────

# Python has three main concurrency models:
#
#  Threading    — multiple threads share one process
#                 Good for: I/O-bound tasks (network, disk)
#                 Limited by: GIL (Global Interpreter Lock)
#
#  Multiprocessing — multiple OS processes, each with its own GIL
#                 Good for: CPU-bound tasks (number crunching)
#
#  Asyncio (async/await) — single thread, cooperative multitasking
#                 Good for: many concurrent I/O-bound tasks
#                 No GIL issues, very efficient

import threading
import multiprocessing
import asyncio
import time
import concurrent.futures

# ─────────────────────────────────────────────
# PART A — THREADING
# ─────────────────────────────────────────────

def download(url: str, delay: float) -> None:
    """Simulates a network download."""
    print(f"[Thread] Start downloading {url}")
    time.sleep(delay)
    print(f"[Thread] Done:  {url}")

# Sequential (slow)
start = time.perf_counter()
download("img1.jpg", 1.0)
download("img2.jpg", 1.0)
print(f"Sequential: {time.perf_counter() - start:.2f}s\n")

# Threaded (fast — overlapping I/O)
start = time.perf_counter()
t1 = threading.Thread(target=download, args=("img1.jpg", 1.0))
t2 = threading.Thread(target=download, args=("img2.jpg", 1.0))
t1.start()
t2.start()
t1.join()   # wait for t1 to finish
t2.join()   # wait for t2 to finish
print(f"Threaded: {time.perf_counter() - start:.2f}s\n")

# Thread with daemon — dies when main thread dies
def background_task():
    while True:
        time.sleep(1)
        print("[Daemon] still alive")

daemon = threading.Thread(target=background_task, daemon=True)
# daemon.start()  # uncomment to observe; won't block program exit

# ThreadPoolExecutor — simpler thread pool
def fetch(n: int) -> str:
    time.sleep(0.2)
    return f"Result {n}"

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    futures = [pool.submit(fetch, i) for i in range(8)]
    results = [f.result() for f in concurrent.futures.as_completed(futures)]
print(sorted(results))

# Thread safety — use a Lock
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(10_000):
        with lock:              # only one thread at a time
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Counter (thread-safe): {counter}")   # always 40000


# ─────────────────────────────────────────────
# PART B — MULTIPROCESSING
# ─────────────────────────────────────────────

def cpu_task(n: int) -> int:
    """CPU-bound: sum of squares."""
    return sum(i * i for i in range(n))

if __name__ == "__main__":   # required guard for multiprocessing
    numbers = [10_000_000] * 4

    # Sequential
    start = time.perf_counter()
    seq_results = [cpu_task(n) for n in numbers]
    print(f"Sequential CPU: {time.perf_counter() - start:.2f}s")

    # ProcessPoolExecutor
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        par_results = list(pool.map(cpu_task, numbers))
    print(f"Parallel CPU:   {time.perf_counter() - start:.2f}s")
    print("Results match:", seq_results == par_results)


# ─────────────────────────────────────────────
# PART C — ASYNCIO (async / await)
# ─────────────────────────────────────────────

async def async_download(url: str, delay: float) -> str:
    print(f"[Async] Start {url}")
    await asyncio.sleep(delay)     # non-blocking sleep
    print(f"[Async] Done  {url}")
    return f"data from {url}"

async def main_async():
    # Run all downloads concurrently
    start = time.perf_counter()
    results = await asyncio.gather(
        async_download("img1.jpg", 1.0),
        async_download("img2.jpg", 1.0),
        async_download("img3.jpg", 1.0),
    )
    elapsed = time.perf_counter() - start
    print(f"Async gather: {elapsed:.2f}s")   # ~1s, not 3s
    print(results)

asyncio.run(main_async())

# --- asyncio.TaskGroup (Python 3.11+) ---
async def main_taskgroup():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(async_download("a.jpg", 0.5))
        t2 = tg.create_task(async_download("b.jpg", 0.5))
    # both tasks completed
    print(t1.result(), t2.result())

asyncio.run(main_taskgroup())

# --- Async generator ---
async def ticker(delay: float, count: int):
    for i in range(count):
        await asyncio.sleep(delay)
        yield i

async def consume_ticker():
    async for tick in ticker(0.1, 5):
        print(f"Tick {tick}")

asyncio.run(consume_ticker())

# --- Async context manager ---
class AsyncDB:
    async def __aenter__(self):
        print("DB connected")
        return self

    async def __aexit__(self, *args):
        print("DB disconnected")

    async def query(self, sql: str) -> list:
        await asyncio.sleep(0.05)   # simulate query
        return [{"id": 1}]

async def run_query():
    async with AsyncDB() as db:
        rows = await db.query("SELECT * FROM users")
        print(rows)

asyncio.run(run_query())


# ─────────────────────────────────────────────
# WHEN TO USE WHAT
#
#  Many I/O operations, high concurrency → asyncio
#  Legacy blocking I/O libraries          → threading
#  CPU-heavy computation                  → multiprocessing
#  Simple parallel tasks                  → concurrent.futures
#
# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   threading.Thread        — I/O-bound concurrency
#   threading.Lock          — mutual exclusion
#   ProcessPoolExecutor     — CPU-bound parallelism
#   async def / await       — cooperative async
#   asyncio.gather          — run coroutines concurrently
#   asyncio.TaskGroup       — structured concurrency (3.11+)
#   async for / async with  — async iteration & context
# ─────────────────────────────────────────────

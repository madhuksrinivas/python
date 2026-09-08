# ─────────────────────────────────────────────
# ADV 08 — Regular Expressions (re module)
# ─────────────────────────────────────────────
#
# WHAT IS A REGULAR EXPRESSION?
#   A regular expression (regex) is a pattern written in a
#   special mini-language that describes text to search for.
#   For example, \d{3}-\d{4} matches "555-1234" — three digits,
#   a dash, four digits. Regex is used to validate input
#   (emails, phone numbers), extract data, and find-and-replace
#   text. Python's 're' module provides all the tools you need.
# ─────────────────────────────────────────────

import re

# ── 1. Quick reference ───────────────────────
# .       any character except \n
# \d      digit [0-9]
# \D      non-digit
# \w      word char [a-zA-Z0-9_]
# \W      non-word char
# \s      whitespace (\t \n \r \f \v space)
# \S      non-whitespace
# ^       start of string
# $       end of string
# *       0 or more
# +       1 or more
# ?       0 or 1  (also makes quantifiers lazy: *? +? ??)
# {n}     exactly n times
# {n,m}   n to m times
# [abc]   character class — a, b, or c
# [^abc]  negated class
# (abc)   capture group
# (?:abc) non-capture group
# a|b     a or b
# \b      word boundary

# ── 2. Core functions ────────────────────────

text = "The quick brown fox jumps over the lazy dog"

# re.search — first match anywhere in string
m = re.search(r"\b\w{5}\b", text)   # first 5-letter word
if m:
    print(m.group())    # quick
    print(m.start(), m.end())   # 4 9

# re.match — match at the START of the string
m = re.match(r"The", text)
print(bool(m))   # True

# re.fullmatch — entire string must match
print(bool(re.fullmatch(r"\d+", "12345")))   # True
print(bool(re.fullmatch(r"\d+", "123abc")))  # False

# re.findall — list of all matches
words5 = re.findall(r"\b\w{5}\b", text)
print(words5)    # ['quick', 'brown', 'jumps']

# re.finditer — iterator of match objects (more info)
for m in re.finditer(r"\b\w{4}\b", text):
    print(m.group(), "@", m.start())

# re.sub — search and replace
cleaned = re.sub(r"\s+", " ", "too   many    spaces")
print(cleaned)   # too many spaces

result = re.sub(r"(\w+)@(\w+)\.(\w+)",
                r"\1 [at] \2 [dot] \3",
                "contact us at hello@example.com please")
print(result)

# re.split — split on a pattern
parts = re.split(r"[,;\s]+", "one, two; three  four")
print(parts)     # ['one', 'two', 'three', 'four']

# ── 3. Compile for reuse (faster in loops) ───
email_re = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

emails = ["alice@example.com", "not-an-email", "bob.smith@company.org"]
for s in emails:
    if email_re.fullmatch(s):
        print(f"Valid: {s}")

# ── 4. Groups ────────────────────────────────
log = "2026-08-20 14:35:07 ERROR Connection refused"

pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})"
    r"\s+(?P<time>\d{2}:\d{2}:\d{2})"
    r"\s+(?P<level>\w+)"
    r"\s+(?P<message>.*)"
)

m = pattern.match(log)
if m:
    print(m.group("date"))     # 2026-08-20
    print(m.group("level"))    # ERROR
    print(m.group("message"))  # Connection refused
    print(m.groupdict())       # all groups as a dict

# Numbered groups
date_m = re.search(r"(\d{4})-(\d{2})-(\d{2})", log)
if date_m:
    year, month, day = date_m.groups()
    print(year, month, day)    # 2026 08 20

# ── 5. Flags ─────────────────────────────────
# re.IGNORECASE / re.I    — case-insensitive
# re.MULTILINE  / re.M    — ^ and $ match each line
# re.DOTALL     / re.S    — . matches \n too
# re.VERBOSE    / re.X    — allow whitespace + comments

verbose_email = re.compile(r"""
    [a-zA-Z0-9._%+-]+   # username
    @                   # at symbol
    [a-zA-Z0-9.-]+      # domain name
    \.                  # literal dot
    [a-zA-Z]{2,}        # TLD
""", re.VERBOSE)

print(bool(verbose_email.fullmatch("alice@example.com")))   # True

multiline_text = "start line\nstart again"
starts = re.findall(r"^start", multiline_text, re.MULTILINE)
print(starts)   # ['start', 'start']

# ── 6. Lookahead & lookbehind ────────────────
# (?=...)   positive lookahead — must follow
# (?!...)   negative lookahead
# (?<=...)  positive lookbehind — must precede
# (?<!...)  negative lookbehind

# Find numbers followed by "px"
print(re.findall(r"\d+(?=px)", "width: 200px, height: 50em"))  # ['200']

# Find prices (preceded by $)
print(re.findall(r"(?<=\$)\d+\.\d{2}", "Total: $19.99 and $5.50"))
# ['19.99', '5.50']

# ── 7. Practical examples ────────────────────

# Validate phone number
phone_re = re.compile(r"^\+?1?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$")
phones = ["+1 (555) 123-4567", "555.123.4567", "not-a-phone"]
for p in phones:
    print(p, "->", bool(phone_re.match(p)))

# Extract all URLs
url_re = re.compile(r"https?://[^\s]+")
text   = "Visit https://python.org and https://github.com for more."
print(url_re.findall(text))

# Sanitize input — remove anything that's not alphanumeric or spaces
def sanitize(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text)

print(sanitize("Hello, <world>! It's 2026."))  # Hello world Its 2026

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   re.search / match / findall / sub / split
#   (?P<name>…)   — named capture groups
#   re.compile()  — pre-compile for reuse
#   Flags: IGNORECASE, MULTILINE, VERBOSE
#   Lookahead / lookbehind  — zero-width assertions
# ─────────────────────────────────────────────

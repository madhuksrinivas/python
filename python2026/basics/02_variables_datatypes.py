# ─────────────────────────────────────────────
# 02 — Variables & Data Types
# ─────────────────────────────────────────────
#
# WHAT IS A VARIABLE?
#   A variable is a named box that stores a value.
#   In Python you don't declare a type — just assign a value
#   and Python figures out the type automatically.
#
# WHAT IS A DATA TYPE?
#   Every value has a type: int (whole number), float (decimal),
#   str (text), bool (True/False), or None (nothing/empty).
# ─────────────────────────────────────────────

# --- Variable assignment ---
# Python is dynamically typed — no need to declare a type.
name    = "Alice"
age     = 25
height  = 5.6
is_cool = True

print(name, age, height, is_cool)   # Alice 25 5.6 True

# --- Core data types ---
integer  = 42            # int
decimal  = 3.14          # float
text     = "Python"      # str
flag     = False         # bool
nothing  = None          # NoneType

# type() reveals the type of any value
print(type(integer))     # <class 'int'>
print(type(decimal))     # <class 'float'>
print(type(text))        # <class 'str'>
print(type(flag))        # <class 'bool'>
print(type(nothing))     # <class 'NoneType'>

# --- Type conversion (casting) ---
x = "10"
print(int(x) + 5)        # 15  — string → int
print(float(x))          # 10.0
print(str(99))            # '99'  — int → string
print(bool(0))            # False (0, "", None, [] are falsy)
print(bool(42))           # True

# --- Multiple assignment ---
a, b, c = 1, 2, 3
print(a, b, c)            # 1 2 3

x = y = z = 0
print(x, y, z)            # 0 0 0

# --- Variable naming rules ---
my_name   = "valid"       # snake_case is the Python convention
_private  = "valid"
MAX_SPEED = 300           # constants are UPPERCASE by convention
# 2fast = "invalid"       # cannot start with a digit

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   int, float, str, bool, None  — built-in types
#   type()   — inspect a variable's type
#   int(), float(), str(), bool() — type casting
#   snake_case convention for variable names
# ─────────────────────────────────────────────

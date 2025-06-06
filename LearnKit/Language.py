#pythoninit
class Python:

    def __init__(self):
        self.Name = "Python"
        self.Version = self.Version()
        self.AvailableTopics = ["DataTypes", "Methods", "History", "Help"]
        self.Author = "Guido van Rossum"
        self.CreationYear = 1991
        self.Features = [
            "Simple syntax", 
            "High readability", 
            "Interpreted language", 
            "Large standard library"
        ]
    
    def __str__(self):
        """Returns Language class name"""
        return f"<Class langueage:Python at {id(self)}>"
#=====================================================================#

    kw_descriptions = {#keywords with their info.
    "if": {
        "Definition": "Used to execute a block of code only if a specified condition is true.",
        "Key Use": "Conditional branching.",
        "Special Features": "Can be combined with 'elif' and 'else' for multiple conditions.",
        "Syntax": "if condition:\n    # code block",
        "Example": "if x > 0:\n    print('Positive number')"
    },
    "else": {
        "Definition": "Defines a block of code to execute when the condition in the if-statement is false.",
        "Key Use": "Provides fallback logic in conditionals.",
        "Syntax": "if condition:\n    # code block\nelse:\n    # fallback block",
        "Example": "if x > 0:\n    print('Positive')\nelse:\n    print('Non-positive')"
    },
    "elif": {
        "Definition": "Short for 'else if', used to check multiple expressions for True.",
        "Key Use": "Multiple conditional branches.",
        "Syntax": "if condition1:\n    # block\nelif condition2:\n    # block\nelse:\n    # block",
        "Example": "if x > 0:\n    print('Positive')\nelif x == 0:\n    print('Zero')\nelse:\n    print('Negative')"
    },
    "for": {
        "Definition": "Iterates over elements in a sequence like list, tuple, or string.",
        "Key Use": "Looping through collections or ranges.",
        "Special Features": "Supports unpacking and else-clauses.",
        "Syntax": "for variable in iterable:\n    # code block",
        "Example": "for item in [1, 2, 3]:\n    print(item)"
    },
    "while": {
        "Definition": "Executes a block of code repeatedly as long as the condition is true.",
        "Key Use": "Conditional looping.",
        "Special Features": "Can have 'else' after loop completes without 'break'.",
        "Syntax": "while condition:\n    # code block",
        "Example": "x = 0\nwhile x < 3:\n    print(x)\n    x += 1"
    },
    "break": {
        "Definition": "Terminates the nearest enclosing loop.",
        "Key Use": "Prematurely exit a loop.",
        "Syntax": "while True:\n    break",
        "Example": "for i in range(5):\n    if i == 3:\n        break\n    print(i)"
    },
    "continue": {
        "Definition": "Skips the rest of the current loop iteration and continues with the next one.",
        "Key Use": "Skip part of the loop body.",
        "Syntax": "for i in range(5):\n    continue",
        "Example": "for i in range(5):\n    if i == 2:\n        continue\n    print(i)"
    },
    "pass": {
        "Definition": "A null statement that does nothing.",
        "Key Use": "Placeholder where code is syntactically required.",
        "Syntax": "if condition:\n    pass",
        "Example": "def future_function():\n    pass"
    },
    "def": {
        "Definition": "Defines a function.",
        "Key Use": "Reusable blocks of code with optional parameters.",
        "Syntax": "def function_name(params):\n    # code block",
        "Example": "def greet(name):\n    print('Hello,', name)"
    },
    "return": {
        "Definition": "Exits a function and optionally returns a value.",
        "Key Use": "Function output.",
        "Syntax": "return [expression]",
        "Example": "def add(a, b):\n    return a + b"
    },
    "yield": {
        "Definition": "Returns a generator instead of a value.",
        "Key Use": "Used in generator functions to maintain state.",
        "Syntax": "yield [expression]",
        "Example": "def gen():\n    yield 1\n    yield 2"
    },
    "lambda": {
        "Definition": "Creates an anonymous function.",
        "Key Use": "Short throwaway functions.",
        "Syntax": "lambda args: expression",
        "Example": "square = lambda x: x * x"
    },
    "import": {
        "Definition": "Used to import modules.",
        "Key Use": "Modular programming.",
        "Syntax": "import module_name",
        "Example": "import math"
    },
    "from": {
        "Definition": "Imports specific elements from a module.",
        "Key Use": "Selective import.",
        "Syntax": "from module import name",
        "Example": "from math import pi"
    },
    "as": {
        "Definition": "Gives a module or function an alias.",
        "Key Use": "Renaming on import.",
        "Syntax": "import module as alias",
        "Example": "import numpy as np"
    },
    "class": {
        "Definition": "Defines a new user-defined class.",
        "Key Use": "Object-oriented programming.",
        "Special Features": "Supports inheritance and encapsulation.",
        "Syntax": "class ClassName:\n    # body",
        "Example": "class Dog:\n    def bark(self):\n        print('Woof!')"
    },
    "try": {
        "Definition": "Start of exception-handling block.",
        "Key Use": "Catching runtime errors.",
        "Syntax": "try:\n    # code",
        "Example": "try:\n    x = 1 / 0"
    },
    "except": {
        "Definition": "Catches specific exceptions from try block.",
        "Key Use": "Error handling.",
        "Syntax": "except ExceptionType:\n    # handler",
        "Example": "try:\n    x = 1/0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')"
    },
    "finally": {
        "Definition": "Runs code regardless of try/except outcome.",
        "Key Use": "Cleanup actions.",
        "Syntax": "finally:\n    # code",
        "Example": "try:\n    x = 1/0\nfinally:\n    print('Cleaning up')"
    },
    "raise": {
        "Definition": "Raises an exception manually.",
        "Key Use": "Force error condition.",
        "Syntax": "raise Exception('message')",
        "Example": "raise ValueError('Invalid input')"
    },
    "assert": {
        "Definition": "Debugging aid that tests if a condition is true.",
        "Key Use": "Sanity checks in code.",
        "Syntax": "assert condition, 'message'",
        "Example": "assert 2 + 2 == 4"
    },
    "with": {
        "Definition": "Used to wrap the execution of a block with methods defined by a context manager.",
        "Key Use": "Resource management (e.g., file handling).",
        "Syntax": "with open('file.txt') as f:\n    # code",
        "Example": "with open('file.txt') as f:\n    data = f.read()"
    },
    "del": {
        "Definition": "Deletes references to objects.",
        "Key Use": "Memory management.",
        "Syntax": "del variable",
        "Example": "del x"
    },
    "global": {
        "Definition": "Declares a variable as global.",
        "Key Use": "Modify global variables inside functions.",
        "Syntax": "global var_name",
        "Example": "global x\nx = 10"
    },
    "nonlocal": {
        "Definition": "Used to work with variables inside nested functions.",
        "Key Use": "Modify enclosing scope variables.",
        "Syntax": "nonlocal var_name",
        "Example": "def outer():\n    x = 0\n    def inner():\n        nonlocal x\n        x += 1"
    },
    "True": {
        "Definition": "Boolean true value.",
        "Key Use": "Logical operations.",
        "Syntax": "True",
        "Example": "if True:\n    print('Yes')"
    },
    "False": {
        "Definition": "Boolean false value.",
        "Key Use": "Logical operations.",
        "Syntax": "False",
        "Example": "if False:\n    print('No')"
    },
    "None": {
        "Definition": "Represents the absence of a value.",
        "Key Use": "Null-like placeholder.",
        "Syntax": "None",
        "Example": "x = None"
    },
    "in": {
        "Definition": "Checks membership in collections.",
        "Key Use": "Loops and conditions.",
        "Syntax": "if item in list:",
        "Example": "if 'a' in 'apple':\n    print('Found')"
    },
    "is": {
        "Definition": "Tests object identity.",
        "Key Use": "Compare memory references.",
        "Syntax": "if a is b:",
        "Example": "x = None\nif x is None:\n    print('None found')"
    },
    "and": {
        "Definition": "Logical AND operator.",
        "Key Use": "Multiple conditions must be true.",
        "Syntax": "if a and b:",
        "Example": "if x > 0 and y > 0:\n    print('Both positive')"
    },
    "or": {
        "Definition": "Logical OR operator.",
        "Key Use": "At least one condition is true.",
        "Syntax": "if a or b:",
        "Example": "if x > 0 or y > 0:\n    print('One is positive')"
    },
    "not": {
        "Definition": "Logical NOT operator.",
        "Key Use": "Invert condition.",
        "Syntax": "if not condition:",
        "Example": "if not found:\n    print('Not found')"
    },
    "async":{
        "Definition": "Declares an asynchronous function that can use 'await' to pause execution until a result is available.",
        "Key Use": "Used to define functions that use asynchronous features for concurrent execution.",
        "Special Features": "Can only be used with Python's async features (like asyncio).",
        "Syntax": "async def function_name():\n    await some_async_operation()",
        "Example": "async def fetch_data():\n    await asyncio.sleep(1)\n    print('Done')"
    },
    "await":{
        "Definition": "Waits for the result of an asynchronous operation inside an async function.",
        "Key Use": "Used to pause the async function until the awaited task is complete.",
        "Special Features": "Can only be used inside an 'async def' function.",
        "Syntax": "await some_coroutine()",
        "Example": "async def example():\n    await asyncio.sleep(1)"    
    }
    }

    kw_groups = {#keyword acording to their uses.
    "Control Flow": [
        "if", "elif", "else", "while", "for", "break", "continue", "pass"
    ],
    "Definition & Structure": [
        "def", "class", "lambda", "return", "yield", "global", "nonlocal"
    ],
    "Error Handling": [
        "try", "except", "finally", "raise", "assert"
    ],
    "Import & Module": [
        "import", "from", "as"
    ],
    "Boolean & Logical": [
        "True", "False", "None", "and", "or", "not", "is", "in"
    ],
    "Context Management": [
        "with", "as"
    ],
    "Del & Misc": [
        "del", "await", "async"
    ]
    }

    #lists for DataTypes
    Num = ['Numeric', 'Num', 'num','numeric']

    Seq=["Sequence","sequence","Seq","seq"]

    Map=["Map","map"]
    Bool=["bool","Bool","Boolean","boolean"]
    Set=["set","Set"]

    Bin=["Bin","bin","Byte","byte","Bytes","bytes"]

    Numv = [
    "\n>> NUMERIC DATATYPES :\n",
    f">> Integer ({int}): A data type that represents whole numbers, including positive, negative, and zero.",
    f">> Example: 4, -5, 100.",
    f">> Range: The maximum and minimum values depend on system memory.\n\n",

    f">> Float ({float}): A data type that represents numbers with decimal points.",
    f">> Example: 4.5, -3.14, 2.0.",
    f">> Range: Approximately ±1.8 × 10^308.\n\n",

    f">> Complex ({complex}): A data type used to store numbers that have both real and imaginary components.",
    f">> Example: 3+4j, -2-5j.",
    f">> Commonly used in scientific and engineering computations.\n\n"
    ]

    Seqv = [
    "\n>> SEQUENCE DATATYPES :\n",
    f">> String ({str}): A sequence of characters enclosed within single, double, or triple quotes.",
    f">> Example: 'hello', \"Python\".",
    f">> Immutable: Once created, the contents of a string cannot be modified.\n\n",

    f">> List ({list}): A collection of ordered elements that can store multiple data types.",
    f">> Example: [1, 2, 3, 'hello'].",
    f">> Mutable: Elements can be added, removed, or modified after creation.\n\n",

    f">> Tuple ({tuple}): A collection of ordered elements similar to a list but with fixed values.",
    f">> Example: (1, 2, 3, 'data').",
    f">> Immutable: Once created, elements cannot be changed.\n\n"
    ]

    Mapv = [
    "\n>> MAPPING DATATYPE :\n",
    f">> Dictionary ({dict}): A collection of key-value pairs where each key is unique and maps to a specific value.",
    f">> Example: {{'name': 'Alice', 'age': 25}}.",
    f">> Mutable: New key-value pairs can be added, removed, or modified.",
    f">> Keys must be immutable types such as strings, numbers, or tuples.\n\n"
    ]

    Boolv = [
    "\n>> BOOLEAN DATATYPE :\n",
    f">> Boolean ({bool}): A data type that represents two values: True and False.",
    f">> Example: True, False.",
    f">> Used in conditions, comparisons, and logical operations.",
    f">> Example: (5 > 3) → True, (5 < 3) → False.\n\n"
    ]

    Setv = [
    "\n>> SET DATATYPES :\n",
    f">> Set ({set}): A collection of unordered, unique elements.",
    f">> Example: {{1, 2, 3, 'apple'}}.",
    f">> Mutable: New elements can be added, and existing ones can be removed.",
    f">> Elements inside a set must be immutable types (e.g., numbers, strings, tuples).\n\n",

    f">> FrozenSet ({frozenset}): A version of a set where elements cannot be modified after creation.",
    f">> Example: frozenset([1, 2, 3]).",
    f">> Immutable: Once created, elements cannot be added or removed.\n\n"
    ]

    Binv = [
    "\n>> BINARY DATATYPES :\n",
    f">> Bytes ({bytes}): A sequence of numbers where each value represents a byte (ranging from 0 to 255).",
    f">> Example: b'hello'.",
    f">> Immutable: Once created, bytes cannot be modified.\n\n",

    f">> Bytearray ({bytearray}): A sequence of bytes similar to bytes but allows modification of its contents.",
    f">> Example: bytearray([65, 66, 67]).",
    f">> Mutable: The byte values can be changed after creation.\n\n",

    f">> Memoryview ({memoryview}): A data type that allows direct access to the memory of a bytes-like object without creating a copy.",
    f">> Example: memoryview(b'hello').",
    f">> Efficient for handling large binary data without unnecessary duplication.\n\n"
    ]
    
    #Dictionary for DataTypes
    dd = dict.fromkeys(Num, Numv)

    dd.update(dict.fromkeys(Seq, Seqv))

    dd.update(dict.fromkeys(Map,Mapv))

    dd.update(dict.fromkeys(Bool,Boolv))

    dd.update(dict.fromkeys(Set,Setv))

    dd.update(dict.fromkeys(Bin,Binv))


    #history of python
    history = """
===========================================
              Python History
===========================================

🐍 Python was created by "Guido van Rossum" and first released in 1991.
It was designed to emphasize code readability and simplicity.


📌 Key Milestones:

- 1989: Guido van Rossum starts working on Python at CWI (Netherlands).

- 1991: Python 1.0 released with basic features like exception handling, functions, and core data types.

- 2000: Python 2.0 introduced garbage collection and list comprehensions.

- 2008: Python 3.0 released, improving Unicode support and fixing design flaws.

- 2018: Python 2.x officially deprecated (support ended in 2020).

- 2023+: Python 3.x continues evolving with performance boosts, pattern matching, and new features.


🔹 Fun Fact: Python is named after "Monty Python's Flying Circus", not the snake! 🐍

===========================================
"""


    def more(text, lines_per_page=15):
    
        lines = text.split("\n")
    
        for i in range(0, len(lines), lines_per_page):
            print("\n".join(lines[i:i + lines_per_page]))
            if i + lines_per_page < len(lines):  
                input("\n\n--Press Enter to continue to next part--\n\n")

    def MethHelp():
        """Returns help on various methods in this class."""
        pass #TODO: Code it damit
    
    
    def AllMethods(self):
        """Returns List of All Methods"""
        meth=list(i+"()" for i in self.__dir__())
        meth.sort()
        return ("\n".join(meth))    
    
    @classmethod
    def KeyWordList(cls):
        import keyword as k
        return k.kwlist
    
    
    @classmethod
    
    def Keywords(cls, *args):
        """Returns keyword info or group-based keyword list."""

        def format_info(kw, data):
            lines = [f">> {kw}"]
            for key, val in data.items():
                lines.append(f"{key}:")
                lines.append(f"{val}\n")
            return "\n".join(lines)

        if not args:
        # No args: Show all groups with keywords
            result = []
            for group, keywords in cls.kw_groups.items():
                result.append(f"{group}:")
                result.append(", ".join(keywords))
                result.append("")
            return "\n".join(result)

        output = []
        for arg in args:
            arg_lower = arg.lower()

        # Try matching a keyword group
            found_group = False
            for group in cls.kw_groups:
                if arg_lower in group.lower():  # Partial match allowed
                    found_group = True
                    output.append(f"{group}:")
                    for kw in cls.kw_groups[group]:
                        short_def = cls.kw_descriptions.get(kw, {}).get("Definition", "No description.")
                        output.append(f"- {kw}: {short_def}")
                    output.append("")  # Spacer line

        # If not group, try keyword match
            if not found_group:
                if arg in cls.kw_descriptions:
                    output.append(format_info(arg, cls.kw_descriptions[arg]))
                else:
                    output.append(f"{arg} not found. Try a keyword or group like 'Control Flow'.")

        return "\n".join(output)
                
    def Methods(self):
        """Returns List of methods excluding Dunder method"""
        
        meth=list(i+"()" for i in self.__dir__() if "__" not in i)

        meth.sort()
        
        return ("\n".join(meth))
        
    @classmethod
    def DataTypes(self,*ar):
        """Returns Datatypes and their info."""
        if not ar:
            result = []
            for key in ["num", "seq", "map", "bool", "set", "bin"]:
                if key in self.dd:
                    result.extend(self.dd[key])
            return "\n".join(result)

        result = []
        for i in ar:
            if i not in self.dd:
                result.append(f"{i} not found. Perhaps you misspelled it?\n")
            else:
                result.extend(self.dd[i])

        return "\n".join(result)

    @classmethod
    def Help(cls,*context):
        """Returns Help on Context(s) on anything."""
        for i in context:
            try:
            
                help(i)

            except Exception:
                print(f"Help couldnt find anythin on {context}, Try AskAi()")
        
    
    @classmethod
    def Version(cls):
        """Returns Current installed language version."""
        import platform as pt

        return f"Installed python version : {pt.python_version()}"


    @classmethod
    def History(cls):
        """Prints Python History"""
        
        cls.more(cls.history)

    

    def EasterEggs():
        """Returns Some famous Easter eggs in python."""
        pass #TODO: Code it damit
    @classmethod
    def ExampleOn(cls,context):
        """Return AI generated example on given context using Gemini AI"""
        from .gemini import get_gemini_response  # Import inside method to avoid import errors
        
        # Initialize Prompt (which manages Gemini AI requests)
        return get_gemini_response(context+" in Python")

    @staticmethod
    def AskAi():
        """When all else fails, AskAi returns Help from AI"""
        from .gemini import Prompt 
  
        return Prompt()
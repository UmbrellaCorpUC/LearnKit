#pythoninit

def more(text, lines_per_page=15):
    
    lines = text.split("\n")
    
    for i in range(0, len(lines), lines_per_page):
        print("\n".join(lines[i:i + lines_per_page]))
        if i + lines_per_page < len(lines):  
            input("\n\n--Press Enter to continue to next part--\n\n")


#Creating Dictionary for Dt() method
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
    
    
dd = dict.fromkeys(Num, Numv)

dd.update(dict.fromkeys(Seq, Seqv))

dd.update(dict.fromkeys(Map,Mapv))

dd.update(dict.fromkeys(Bool,Boolv))

dd.update(dict.fromkeys(Set,Setv))

dd.update(dict.fromkeys(Bin,Binv))



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


class Python:
    
    def __init__(self):
        pass
    
    
    def __str__(self):
        return f"<Class langueage:Python at {id(self)}>"

    def MethHelp():
        pass
    
    def AllMeth(self):
        meth=list(i+"()" for i in self.__dir__())
        meth.sort()
        return ("\n".join(meth))    
    
            
    
    def Meth(self):
        
        meth=list(i+"()" for i in self.__dir__() if "__" not in i)

        meth.sort()
        
        return ("\n".join(meth))
        
    @staticmethod
    def Dt(*ar):
        if not ar:
            result = []
            for key in ["num", "seq", "map", "bool", "set", "bin"]:
                if key in dd:
                    result.extend(dd[key])
            return "\n".join(result)

        result = []
        for i in ar:
            if i not in dd:
                result.append(f"{i} not found. Perhaps you misspelled it?\n")
            else:
                result.extend(dd[i])

        return "\n".join(result)

    def Help():
        pass
    
    @staticmethod
    def Version():
        import platform as pt

        return f"Installed python version : {pt.python_version()}"


    @staticmethod
    def Hist():
        
        more(history)


    def EasterEggs():
        pass 
    

    def ExampleOn():
        pass

    def askai(promt,mode):
        pass

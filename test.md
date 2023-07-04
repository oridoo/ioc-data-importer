# 1 Python
## Mutable / Immutable 
#### Name at least three mutable and immutable built-in types.
- mutable -> List, Set, Dict
- immutable -> Integer, String, Tuple

####  What is a difference between list and tuple?
- List is mutable, Tuple is immutable
- List is defined with `[...,]`, Tuple is defined with `(...,)`

#### What happens if you pass an argument to a function and modify the argument inside? Will the value of this argument be changed after calling this function?
- mutable types will be changed outside of the function
- immutable types will not be changed

## Shallow / Deep Copy
#### What is a difference between shallow1 and deep copy2 of an object in Python?
- shallow copy -> creates a new object which stores the reference of the original elements
- deep copy -> creates a new object and recursively adds the copies of nested objects present in the original elements 

## Concurrent Computation in Python
#### What are the possibilities of implementing concurrent computation that Python offers? Briefly describe them.
- threading lib -> run multiple (system level) threads within a process
- multiprocessing lib -> run multiple processes
- asyncio lib -> single thread concurrency using coroutines (async/await)

## Design Patterns, Python Idioms, and OOP
#### Briefly describe singleton design pattern. Provide at least one example of practical usage
- Singleton design pattern restricts the instantiation of a class to one global object
- useful for database connections, logging, etc..
```python
class DatabaseConnection:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnection._instance is None:
            DatabaseConnection._instance = DatabaseConnection()
        return DatabaseConnection._instance

    def __init__(self):
        if DatabaseConnection._instance is not None:
            raise Exception("Cannot create another instance")
        DatabaseConnection._instance = self
        pass
```

#### How would you implement an iterator class. What things (e.g. methods) are required?
- the class would have to implement the special `__iter__` and `__next__` methods
- `__iter__` returns the iterator object itself
- `__next__` returns the next item in the sequence and raises StopIteration when there are no more items
```python
class NyoomIterator:
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 1
            return result
        else:
            raise StopIteration
```

#### What is monkey patching?
- Monkey patching is changing the behavior of a class or module at runtime without altering the source code
- useful for testing, hotfixes, etc.. 
```python
class Monkey:
    def __init__(self, name):
        self.name = name

def monkey_greet(self):
    print(f"I am {self.name}")

Monkey.greet = monkey_greet

monkey = Monkey("Donkey Kong")
monkey.greet()
```

#### What is dependency injection and how would you implement it?
- Dependency injection is a design pattern where the object is passed the dependencies it needs instead of creating and managing them by itself
- Simplest way to implement it is to pass the dependencies as parameters to the constructor
```python
class Dependency:
    def __init__(self, name):
        self.name = name

class Dependent:
    def __init__(self, dependency):
        self.dependency = dependency

dependency = Dependency("dep")
dependent = Dependent(dependency)
```

#### What is the difference between instance, static, and class method?
- **instance method** -> takes self as the first argument, can access instance variables
- **static method** -> doesn't have access to instance variables, useful for utility functions related to the class
- **class method** -> takes cls (class itself) as the first argument, can access class-level data

#### What are dunder/magic methods? Provide and briefly describe few of them.
- Dunder/magic methods are special methods defining behavior and operations for objects in Python, they are automatically called by Python in response to certain language constructs or operations
- `__init__(self, ...)` -> constructor of the class
- `__str__(self)` -> string representation of the object (called by `str()`)
- `__len__(self)` -> length of the object (called by `len()`)
- `__add__(self, other)` -> addition of two objects (used by `+` operation)
- `__call__(self, ...)` -> makes the object callable and executes the code inside the method

#### What are, and how would you implement private, protected, and public class attributes in Python? What about class inheritance when using them?
- there is a naming convention for private, protected, and public attributes but no access control
- **private** -> `__attribute` -> can only be accessed inside the class
- **protected** -> `_attribute` -> can be accessed inside the class and its subclasses
- **public** -> `attribute` -> can be accessed anywhere
- for private attributes, the name is mangled to `_ClassName__attribute` to prevent accidental access
- derived classes follow the same naming convention and can access protected and public attributes of the base class (private attributes are still technically available in the mangled forms)

#### What are context managers and when would you use it?
- Context managers is a python construct that allows you to easily manage resources by using the `with` statement, without having to worry about cleaning up the resources
- typical use cases are file operations, database connections, thread locks, etc..
- the context manager object has to implement the `__enter__` and `__exit__` methods
- `__enter__` -> when entering the `with` block, sets up necessary resources
- `__exit__` -> when exiting the `with` block, cleans up the resources and handles exceptions
```python
class ContextManager:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Entering {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting {self.name}")

with ContextManager("nyoom") as cm:
    print(f"Inside {cm.name}")
```

#### When would you implement a custom exception?
- When the built-in exceptions are not enough to convey specific errors, it also makes the code more expressive, enhances error handling capabilities, improves reliability and maintainability
- Also useful for libraries, frameworks or APIs to provide more useful exceptions specific to the module.

#### What are decorators? Please provide at least one example of their usage. Is it possible to stack multiple different decorators?
- Decorators are functions that take another function as an argument and extend its functionality without modifying it by wrapping it inside another function
- useful for logging, timing, etc..
- multiple decorators can be stacked by stacking them on top of each other
```python
def log(func):
    def wrapper(*args, **kwargs):
        print("Starting")
        func(*args, **kwargs)
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start}")
    return wrapper

@log
@timer
def hello(name):
    print(f"Hello, {name}")

hello("Donkey Kong")
```

## Code snippets
#### 1st snippet
```python
print([1,2,3][10:]) 
print(r" ict a\nd media ")
```
- `[]` -> slicing, returns a list of the sliced elements in this case empty because there are no elements after index 2
- `⎵ict a\nd media⎵` -> `r""` is a raw string, doesn't escape special characters

#### 2nd snippet (too lazy to actually rewrite it)
  - `[42]` -> 2nd argument of extendlist has default value of `[]` so it's the same as `extendlist(42, [])`
  - `[42]` -^
  - `["item"]`

#### Implement a function, that will find all odd integer numbers from interval <1; 100 000>, and stores them into a list.
```python
def find_odd_numbers_100k():
    return [i for i in range(1, 100000 + 1) if i % 2 == 1]
```
- using fancy list comprehension

####  Implement a function, that generates infinite sequence of odd numbers.
```python
def odd_numbers():
    i = 1
    while True:
        print(i) # or yield i to make it a generator
        i += 2
```

#### Write a regular expression, that matches protocol, IPv4 address, and port from the string below. There can be any protocol, IPv4 address, and any port on the input. Protocol and port are optional parts and can be missing. For the string below, it must match groups “protocol=udp”, “ipv4=127.0.0.1”, “port=53” :

`“udp://127.0.0.1:53”`

```regex
(?:(?P<protocol>\w+)://)?(?P<ipv4>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::(?P<port>\d+))?
```
- `(?:(?P<protocol>\w+)://)?` -> non-capturing group, matches the protocol part, `?` makes it optional
- `(?P<ipv4>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})` -> matches the ipv4 address
- `(?::(?P<port>\d+))?` -> non-capturing group, matches the port part

<sub><sup><sub><sup>i despise regex</sup></sub></sup></sub>

# 2. Testing and Code Quality

#### What is the difference between unit and integration testing?
- unit testing -> testing individual units of code, usually functions or methods
- integration testing -> testing multiple units of code together, usually multiple functions or entire modules

#### What is mocking and what are its benefits during testing?
- mocking -> replacing a real object with a fake object that simulates the real object
- when unit testing, mocking is useful for testing the unit in isolation, without having to worry about the other parts of the code it depends on

#### What is white box and black box testing?
- white box testing -> testing the internal structure of the code, usually done by the developers
    - testing with access to the source code
    - all paths are tested
    - test cases based on the code
- black box testing -> testing the functionality of the code
    - testing without access to the source code
    - tests external behaviour
    - test cases based on the requirements

#### What is static analysis of code (hint: pep8)?
- analyzing the code without executing it
- checking for syntax errors, code style, code complexity, etc..
- pep8 -> python style guide

#### What stands for CI and CD?
- CI -> continuous integration
    - merging code changes into a shared repository frequently
    - running automated tests triggered by commits
    - building and validating the code
- CD -> continuous delivery
    - automated deploying the code to production environment
    - running automated tests
    - deploying to production

# 3. Databases

#### What is the difference between SQL and NoSQL database systems? Name a few candidates from each group.
- **SQL** -> relational database, data is stored in tables, data is structured, uses SQL for querying
    - MySQL, PostgreSQL, SQLite
- **NoSQL** -> non-relational database, data is stored in: key-value pairs, documents, graphs, etc.., data is unstructured, uses non-SQL query languages
    - MongoDB, Redis, Neo4j

#### What is a database index? What types of database indexes are familiar to you? (Ideally in PostgreSQL)
- database index -> data structure that improves the speed of data retrieval operations on a database table
- I only really know about B-tree and hash indexes
    - **B-tree** -> default index type in PostgreSQL, stores data in a sorted tree structure, supports range queries
    - **Hash** -> stores data in a hash table, supports only simple equality queries
    - **GIN** -> stores data in a sorted tree structure, supports full text search (component values such as arrays, text, etc..)
    - **GiST** -> stores data in a balanced tree structure, supports geometric data types

#### What would you do, if you needed to optimize an SQL query?
- fetch only the columns that are needed
- use appropriate indexes on the columns used in the query
- use `EXPLAIN ANALYZE` to see how the query is executed and see if there are any visible bottlenecks
- materialized views in PostgreSQL -> precomputed results of a query, useful for queries that are executed often (might cause problems with data consistency if the underlying data changes often)

#### What is ELT and ETL (hint: extract, load, transform)? What are differences between them?
- **ETL** -> extract, transform, load
    - data is extracted from the source, transformed to fit the target schema and loaded into the target database
    - data is transformed before loading into the target database

- **ELT** -> extract, load, transform
    - data is extracted from the source and loaded into the target database
    - data is transformed after loading within the target environment

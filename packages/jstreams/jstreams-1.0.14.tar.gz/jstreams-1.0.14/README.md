# jstreams

jstreams is a Python library aiming to replicate the Java Streams and Optional functionality. The library is implemented with type safety in mind.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install jstream.

```bash
pip install jstreams
```

## Usage

### Streams

```python
from jstreams import Stream

# Applies a mapping function on each element then produces a new string
print(Stream(["Test", "Best", "Lest"]).map(str.upper).collect())
# will output ["TEST", "BEST", "LEST"]

# Filter the stream elements
print(Stream(["Test", "Best", "Lest"])
            .filter(lambda s: s.startswith("T"))
            .collect())
# Will output ['Test']

# isNotEmpty checks if the stream is empty
print(Stream(["Test", "Best", "Lest"])
            .filter(lambda s: s.startswith("T"))
            .isNotEmpty())
# Will output True

# Checks if all elements match a given condition
print(Stream(["Test", "Best", "Lest"]).allMatch(lambda s: s.endswith("est")))
# Will output True

print(Stream(["Test", "Best", "Lest"]).allMatch(lambda s: s.startswith("T")))
# Will output False

# Checks if any element matches a given condition
print(Stream(["Test", "Best", "Lest"]).anyMatch(lambda s: s.startswith("T")))
# Will output True

# Checks if no elements match the given condition
print(Stream(["Test", "Best", "Lest"]).noneMatch(lambda s: s.startswith("T")))
# Will output False

# Gets the first value of the stream as an Opt (optional object)
print(Stream(["Test", "Best", "Lest"])
            .findFirst(lambda s: s.startswith("L"))
            .getActual())
# Will output "Lest"

# Returns the first element in the stream
print(Stream(["Test", "Best", "Lest"]).first())
# Will output "Test"

# cast casts the elements to a different type. Useful if you have a stream
# of base objects and want to get only those of a super class
print(Stream(["Test1", "Test2", 1, 2])
            .filter(lambda el: el == "Test1")
            # Casts the filtered elements to the given type
            .cast(str)
            .first())
# Will output "Test1"

# If the stream elements are Iterables, flatMap will produce a list of all contained items
print(Stream([["a", "b"], ["c", "d"]]).flatMap(list).toList())
# Will output ["a", "b", "c", "d"]

# reduce will produce a single value, my applying the comparator function given as parameter
# in order to decide which value is higher. The comparator function is applied on subsequent elements
# and only the 'highest' one will be kept
print(Stream([1, 2, 3, 4, 20, 5, 6]).reduce(max).getActual())
# Will output 20

# notNull returns a new stream containing only non null elements
print(Stream(["A", None, "B", None, None, "C", None, None]).nonNull().toList())
# Will output ["A", "B", "C"]

```

### Opt
```python
from jstreams import Opt

# Checks if the value given is present
Opt(None).isPresent() # Will return False
Opt("test").isPresent() # Will return True


# There are two ways of getting the value from the Opt object. The get returns a non optional
# value and  will raise a value error if the object is None. On the other hand, getActual returns
# an optional object and does not raise a value error
Opt("test").get() # Does not fail, and returns the string "test"
Opt(None).get() # Raises ValueError since None cannot be casted to any type
Opt(None).getActual() # Returns None, does not raise value error

# The ifPresent method will execute a lambda function if the object is present
Opt("test").ifPresent(lambda s: print(s)) # Will print "test"
Opt(None).ifPresent(lambda s: print(s)) # Does nothing, since the object is None

# The getOrElse method will return the value of the Opt if not None, otherwise the given parameter
Opt("test").getOrElse("test1") # Will return "test", since the value is not None
Opt(None).getOrElse("test1") # Will return "test1", since the value is  None

# The getOrElseGet method will return the value of the Opt if not None, otherwise it will execute 
# the given function and return its value
Opt("test").getOrElseGet(lambda: "test1") # Will return "test", since the value is not None
Opt(None).getOrElseGet(lambda: "test1") # Will return "test1", since the value is  None

# stream will convert the object into a stream.
Opt("test").stream() # Is equivalent with Stream(["test"])
Opt(["test"]).stream() # Is equivalent with Stream([["test"]]). Notice the list stacking

# flatStream will convert the object into a stream, with the advantage that it can
# detect whether the object is a list and avoids stacking lists of lists.
Opt("test").flatStream() # Is equivalent with Stream(["test"])
Opt(["test", "test1", "test2"]).flatStream() # Is equivalent with Stream(["test", "test1", "test2"])

```

### Try
```python
# The Try class handles a chain of function calls with error handling

def throwErr() -> None:
    raise ValueError("Test")

def returnStr() -> str:
    return "test"

# It is important to call the get method, as this method actually triggers the entire chain
Try(throwErr).onFailure(lambda e: print(e)).get() # The onFailure is called

Try(returnStr).andThen(lambda s: print(s)).get() # Will print out "test"

# The of method can actually be used as a method to inject a value into a Try without
# actually calling a method or lambda
Try.of("test").andThen(lambda s: print(s)).get() # Will print out "test"
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
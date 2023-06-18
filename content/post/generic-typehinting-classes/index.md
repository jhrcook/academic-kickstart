---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Leveraging generic type hints of classes in Python"
subtitle: "Exploring the power of generic type hinting in Python classes to make your code more flexible to use and more robust to errors."
summary: "A simple introduction to generic type hints in Python and how to use them in classes."
authors: []
tags: ["Python", "type hinting", "code", "programming"]
categories: ["Programming"]
date: 2023-06-18T17:25:33-04:00
lastmod: 2023-06-18T17:25:33-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "DALLE-2's result for the prompt: 'Claude Monet's Water Lillies with a person sitting on the grass typing on a laptop.'"
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---



## Introduction

Python, a versatile and dynamically-typed language, gained significant enhancements with the introduction of type hinting in Python 3.5.
Often though, there are cases where the specific type of an input and output of a function are not known, just that the types are the same.
This is where generic type hints come in.
There are cases where this principle applies to classes, but it is not immediately clear how to generically type hint a class.
In this blog post, we will delve into the world of generic type hinting in Python classes and explore how it can improve our Python code.

## Understanding generic types

Generic type hinting is a powerful tool that enables flexible APIs while maintaining strong standard of code readability, maintainability, and type safety.
To illustrate the concept, say we want to make a function that doubles every value in a list.
We want to type hint the input and output of the function as lists without limiting the types of the values in the list.
Type hinting this sort of function is illustrated below.

```python
from typing import TypeVar

T = TypeVar("T")

def double_a_list(x: list[T]) -> list[T]:
    return x + x
```

First, the variable `T`[^1] is created using the `TypeVar` class from the `typing` module.
`T` is the generic type, standing in for the type of the values in the list.
You can see how `T` is used as the type of value for the `list[]` type hint in the function definition.
The benefit of using the generic type over just using `Any` is now when `double_a_list()` is used, the type checker will know that the type of the output will match the type of the input
Below is a demonstration where I have included the type hints of the ouputs for clarity, the type checker does not need them for type inference.

[^1]: The name of the generic class is arbitrary, just the name of the variable should match the string passed as the first argument. In strictly typed languages, it is customary to use the generics `T`, `U`, `V`, etc.

```python
a: list[str] = double_a_list(["a", "b", "c"])
b: list[int] = double_a_list([1, 2, 3])
```

This is the process for generic type hinting of functions, but there is an additional step for using generic type hints in classes.

## Defining generic classes

Generic type hinting enables the developer of a class to create an interface where the user of the class can define the expected types of class attributes, method arguments, and return values.
This powerful feature enables the creation of reusable classes that can operate on different types without sacrificing type safety.

To create a generic class, we use `Generic` from the `typing` module in the definition of the class along with the `TypeVar` from before.
Here's a simple example to illustrate the concept:

```python
from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):

    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
```

In the above code snippet, we create a generic class called `Stack` that represents a stack data structure.
The type variable `T` is used to indicate the type of the items stored in the stack.
By using `list[T]`, we ensure that `items` is a list of elements of type `T`.
The `push` method accepts an argument of type `T` and the `pop` method returns a value of type `T`.
This way, we enforce type safety and provide clear type hints for anyone using this class.

## Using the generic class

Now that we have defined our generic class, let's see how it can be used with different types:

```python
stack = Stack[int]()  # Instantiate a Stack object that will contain integers
stack.push(5)
stack.push(10)
value: int = stack.pop()  # This type hint is just to emphasize the return type.
```

In the code above, we instantiate the `Stack` class with the type `int`, indicating that the stack will store integers.
We push integers onto the stack and retrieve them using the `pop` method.

## Classes with multiple generic types

It is possible to define a class with multiple generic types by just listing them in the class definition.
Below is a simple example:

```python
from typing import Generic, TypeVar

T = TypeVar(T)
U = TypeVar(U)

class MyClass(Generic[T, U]):

    def __init__(self, foo: T, bar: U) -> None:
        self.foo = foo
        self.bar = bar

    def get_foo(self) -> T:
        return self.foo

    def get_bar(self) -> U:
        self.bar
```

In the case of multiple generics, it may be helpful to give the generic types more descriptive names.

## Conclusion

Generic type hinting in Python classes brings significant benefits to a codebase.
By leveraging type variables, we can create reusable classes that operate on different types while maintaining type safety and code readability.
Embracing this powerful feature enhances the development experience and makes the code more robust and maintainable.

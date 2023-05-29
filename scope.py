#! /bin/bash
# Python code to variable scopes
a = 100


def scope_variable():
    b = 200
    print("a = ", a, "b = ", b)


if __name__ == '__main__':
    c = 100
    print("a: ", a)
    print("c: ", c)
    scope_variable()
    a = a + 10
    print("a: ", a)
    scope_variable()
def fib_recursive(n: int) -> int:
    if n < 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_non_recursive(n: int) -> int:
    CALL, HANDLE = 0, 1
    call_stack = [(CALL, n)]
    return_stack = []
    while call_stack:
        action, data = call_stack.pop()
        if action == CALL:
            n = data
            if n < 2:
                return_stack.append(1)
            else:
                call_stack.append((HANDLE, None))
                call_stack.append((CALL, n - 2))
                call_stack.append((CALL, n - 1))
        else:  # HANDLE
            x = return_stack.pop()  # fib(n - 1)
            y = return_stack.pop()  # fib(n - 2)
            return_stack.append(x + y)
    return return_stack[-1]


if __name__ == "__main__":
    print(fib_recursive(30))
    print(fib_non_recursive(30))

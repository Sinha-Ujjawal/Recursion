def move_disc(frm: str, to: str) -> str:
    return f"Move disc from {frm} to {to}"


def tower_of_hanoi_recursive(n: int, frm: str, via: str, to: str):
    if n > 0:
        tower_of_hanoi_recursive(n - 1, frm, to, via)
        print(move_disc(frm, to))
        tower_of_hanoi_recursive(n - 1, via, frm, to)


def tower_of_hanoi_non_recursive(n: int, frm: str, via: str, to: str):
    CALL, HANDLE = 0, 1
    call_stack = [(CALL, (n, frm, via, to))]
    while call_stack:
        action, data = call_stack.pop()
        if action == CALL:
            n, frm, via, to = data
            if n > 0:
                call_stack.append((CALL, (n - 1, via, frm, to)))
                call_stack.append((HANDLE, (frm, to)))
                call_stack.append((CALL, (n - 1, frm, to, via)))
        else:  # HANDLE
            frm, to = data
            print(move_disc(frm, to))


if __name__ == "__main__":
    tower_of_hanoi_recursive(4, "A", "B", "C")
    print()
    tower_of_hanoi_non_recursive(4, "A", "B", "C")

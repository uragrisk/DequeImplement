from deque import Deque


def main():
    deque = Deque()
    deque.push_left(22)
    deque.push_left(28)
    deque.push_left(1)
    deque.push_right(11)
    deque.push_right(9)
    deque.push_right(40)
    deque.print_deque()
    deque.find_by_value(1)
    deque.find_by_value(3)
    deque.pop_left()
    deque.pop_right()
    deque.print_deque()


if __name__ == "__main__":
    main()

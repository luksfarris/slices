import sys


def sample_sum(x: int, y: int) -> int:
    return x + y


def run() -> None:
    argv = sys.argv
    x = int(argv[1])
    y = int(argv[2])
    z = sample_sum(x, y)
    print(f"{x}+{y}={z}")


if __name__ == "__main__":
    run()

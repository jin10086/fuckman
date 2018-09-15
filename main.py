import multiprocessing

from apps import Momo


def run(func, phone):
    f = func()
    f.run(phone)


if __name__ == "__main__":
    apps = [Momo]
    phone = ""
    with multiprocessing.Pool() as pool:
        pool.starmap(run, [(i, phone) for i in apps])

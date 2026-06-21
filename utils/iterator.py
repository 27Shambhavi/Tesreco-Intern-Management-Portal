class InternIDIterator:

    def __init__(self):

        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.count <= 999:

            intern_id = f"TES{self.count:03d}"

            self.count += 1

            return intern_id

        raise StopIteration


if __name__ == "__main__":

    ids = InternIDIterator()

    for _ in range(10):
        print(next(ids))
import csv


class Base():
    def __init__(self, file, bufsize=5, encoding='utf-8'):
        self.content = self._scan(file, encoding)
        self.buf = []
        self.bufsize = bufsize

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.content) == 0:
            raise StopIteration()
        self.buf.append(self.content.pop(0))
        if len(self.buf) > self.bufsize:
            self.buf.pop(0)
        return self.buf[-1]

    def unshift(self):
        self.content.insert(0, self.buf.pop())
        return self.content[0]

    # Override this '_scan' method, in sub-class.
    def _scan(self, file, encoding='utf-8'):
        pass


class LineScanner(Base):
    def _scan(self, file, encoding='utf-8'):
        with open(file, 'r', encoding=encoding) as f:
            content = f.readlines()
        return content


class CsvScanner(Base):
    def _scan(self, file, encoding='utf-8'):
        with open(file, 'r', encoding=encoding) as csv_file:
            reader = csv.reader(csv_file)
            content = list(reader)
        return content

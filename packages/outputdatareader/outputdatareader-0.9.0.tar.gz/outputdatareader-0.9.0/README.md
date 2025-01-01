# outputdatareader

プログラムの実行結果として出力されたテキストファイルから、必要なデータを読み取るリーダです。

実行結果をテキストファイルに出力するプログラムは多くありますが、その出力は一貫したフォーマットになっているとは限りません。
複数のセクションからなり、セクションごとにフォーマットが異なっている場合、全体を1つの解析器で賄うことは難しくなります。
また、欲しいのは一部のセクションだけ、というケースもあります。

outputodatareader では、必ずしも出力全てを読み取る必要はなく、欲しい部分だけを読み取ることができます。

## Install

pip でインストールできます：

    $ pip install outputdatareader

または、パッケージマネージャーを使ってプロジェクトに追加します：

    $ poetry add outputdatareader

## Usage

### How it works

outputdatareader は2つのステージから成ります。

1. スキャナはテキストファイルを適切なセグメント（例えば1つの行）に分解します。
2. リーダはスキャナからセグメントを1つずつ取り出し、読み取ることを繰り返します。

リーダはスキャナから取り出したセグメントを1つずつ処理しますが、本当に必要なものだけを選んで読み取ることができます。不要なセグメントは捨ててしまえばいいのです。

リーダはまた、処理の一部を別のリーダに任せることができます。処理が戻ってきたら、そこから処理を続けます。

### Reader

`outputdatareader.readers.Base` クラスを継承したサブクラスを定義し、インスタンスを生成して利用します。
このクラスは読み取りループの枠組みを提供するので、サブクラスではスキャナから取り出したセグメントを解析して読み取ることに集中できます。
サブクラスには、次のメソッドを実装します。

- `setup`
- `loop`
- `teardown`

`loop` だけが必須です。このメソッドが読み取りの本質部分です。
`setup` と `teardown` はそれぞれ読み取りの前処理、後処理をします。

読み取りループ中にはいくつかのプライベートメソッドが利用できます。

- `_next_loop` は「つぎの回」へジャンプします。
- `_exit_loop` は読み取りループを終了します。処理が親クラスへ戻る前に `teardown` が実行されます。
- `_exit_read` は `teardown` もとばして読み取りを終了します。
- `_unshift` はセグメントを1つ、スキャナに戻します。

`_unshift` が必要になるのは、スキャナから受け取ったセグメントが、別のリーダが読み取るべき「次のセクション」の始まりであるような場合です。
セグメントを1つスキャナに戻してから読み取りを終了すれば、「次のセクション」を読み取る別のリーダがそこから読み取りを開始できます。

### Scanner

スキャナは、テキストファイルを適切なセグメントに分解し、リーダに提供します。
スキャナは iterable なオブジェクトです。

独自のスキャナを作るには `outputdatareader.scanners.Base` クラスを継承し、 `_scan` メソッドを実装します。この `_scan` が適切なセグメントに分解する役割を担っています。

`outputodatareader.scanners` モジュールには、1行ずつに分解する `LineScanner` と、CSVファイルを1レコードずつに分解する `CsvScanner` が用意されています。

## Example

```python
from outputdatareader.scanners import LineScanner
from outputdatareader.readers import Base


class MainReader(Base):
    def loop(self, line):
        if line.statswith('Section 2'):
            self._unshift()
            reader = Section2Reader(self.scanner, {})
            self.holder['section_2'] = reader.read()
        elif line.statswith('Section 5'):
            self._unshift()
            reader = Section5Reader(self.scanner, {})
            self.holder['section_5'] = reader.read()
        else:
            # ignore other sections
            pass


class Section2Reader(Base):
    def loop(self, line):
        if line.startswith('Section 3'):
            self._exit_read()
        else:
            # implement here


class Section5Reader(Base):
    def loop(self, line):
        # implement here


def main():
    scanner = LineScanner('some_output.txt', encoding='utf-8')
    result_holder = {}
    reader = MainReader(scanner, result_holder)
    result = reader.read()
    print(result)


main()
```

## License

MIT License.

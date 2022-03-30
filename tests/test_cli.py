import sys
import io

from hello.cli import main


def test_main():
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    main()

    output = new_stdout.getvalue()

    assert "Hello Pyvo!" in output

    sys.output = old_stdout

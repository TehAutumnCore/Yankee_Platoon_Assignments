import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5
    # assert calculator.calculate(6, 2, "divide") == 3.0
# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys,monkeypatch):
    monkeypatch.setattr("sys.argv",["calculator.py", "10","2","multiply"])
    calculator.main()
    captured = capsys.readouterr()
    # print(captured)
    assert captured.out == "Result: 20.0\n"

def test_argument_passing(monkeypatch):
    # monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

# Add more tests to cover edge cases and negative scenarios


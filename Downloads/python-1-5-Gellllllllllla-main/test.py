def captured_in_out(monkeypatch, capsys, file_name, inputs):
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    exec(open(file_name).read())
    captured = capsys.readouterr().out
    return captured


def test_task1(monkeypatch, capsys):
    inputs = iter([
        (iter(["3"]), ""),
        (iter(["2"]), "Число не делится на 3\n"),
        (iter(["5"]), "Число не делится на 3\n"),
        (iter(["473109821"]), "Число не делится на 3\n"),
        (iter(["21836811"]), "")
    ])

    for i, out in inputs:
        assert captured_in_out(monkeypatch, capsys, "task1.py", i) == out


def test_task2(monkeypatch, capsys):
    inputs = iter(
        [
            (iter(["2"]), "четное\n"),
            (iter(["3"]), "нечетное\n"),
            (iter(["4"]), "четное\n"),
            (iter(["5"]), "нечетное\n"),
            (iter(["2657768391978"]), "четное\n"),
            (iter(["2657768391979"]), "нечетное\n")
        ]
    )
    for i, out in inputs:
        assert captured_in_out(monkeypatch, capsys, "task2.py", i) == out


def test_task3(monkeypatch, capsys):
    inputs = iter(
        [
            (iter(["16"]), "Слишком юный\n"),
            (iter(["25"]), "Достаточно взрослый\n"),
            (iter(["18"]), "Слишком юный\n"),
            (iter(["17"]), "Слишком юный\n")
        ]
    )
    for i, out in inputs:
        assert captured_in_out(monkeypatch, capsys, "task3.py", i) == out


def test_task4(monkeypatch, capsys):
    inputs = iter(
        [
            (iter(["Bond"]), "Wellcome, mr. Bond!\n"),
            (iter(["James"]), "")
        ]
    )

    for i, out in inputs:
        assert captured_in_out(monkeypatch, capsys, "task4.py", i) == out


def test_task5(monkeypatch, capsys):
    inputs = iter(
        [
            (iter(["2020"]), "високосный\n"),
            (iter(["2021"]), "невисокосный\n"),
            (iter(["2000"]), "високосный\n"),
            (iter(["1900"]), "невисокосный\n")
        ]
    )

    for i, out in inputs:
        assert captured_in_out(monkeypatch, capsys, "task5.py", i) == out
        

def test_task6(monkeypatch, capsys):
    inputs = iter(
        [
            (iter(["5", "7"]), "7\n"),
            (iter(["7", "7"]), "равны\n"),
            (iter(["5", "5"]), "равны\n"),
            (iter(["7", "5"]), "7\n")
        ]
    )

    for i, out in inputs:
        assert captured_in_out(monkeypatch, capsys, "task6.py", i) == out


def test_task7(monkeypatch, capsys):
    inputs = iter(
        [
            (iter(["5"]), "положительное\n"),
            (iter(["-5"]), "отрицательное\n"),
            (iter(["0"]), "ноль\n"),
            (iter(["-0"]), "ноль\n"),
            (iter(["-10"]), "отрицательное\n"),
            (iter(["10"]), "положительное\n")
        ]
    )

    for i, out in inputs:
        assert captured_in_out(monkeypatch, capsys, "task7.py", i) == out


def test_task8(monkeypatch, capsys):
    inputs = iter(
        [
            (iter(["a"]), "True\n"),
            (iter(["e"]), "True\n"),
            (iter(["i"]), "True\n"),
            (iter(["o"]), "True\n"),
            (iter(["u"]), "True\n"),
            (iter(["y"]), "True\n"),
            (iter(["b"]), "False\n"),
            (iter(["c"]), "False\n"),
            (iter(["d"]), "False\n"),
            (iter(["f"]), "False\n"),
            (iter(["g"]), "False\n"),
            (iter(["h"]), "False\n"),
            (iter(["j"]), "False\n"),
            (iter(["k"]), "False\n"),
            (iter(["l"]), "False\n"),
        ]
    )

    for i, out in inputs:
        assert captured_in_out(monkeypatch, capsys, "task8.py", i) == out


def test_task9(monkeypatch, capsys):
    inputs = iter(
        [
            (iter(["16"]), "Слишком юный\n"),
            (iter(["25"]), "Достаточно взрослый\n"),
            (iter(["18"]), "Достаточно взрослый\n"),
            (iter(["17"]), "Слишком юный\n")
        ]
    )
    for i, out in inputs:
        assert captured_in_out(monkeypatch, capsys, "task9.py", i) == out
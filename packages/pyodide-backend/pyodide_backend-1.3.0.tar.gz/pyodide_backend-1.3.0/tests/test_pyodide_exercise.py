import json

from pyodide_backend import PyodideExercise


def test_run_code():
    pec = "x = 10"
    solution = ""
    sct = ""
    exercise = PyodideExercise(pec=pec, solution=solution, sct=sct)
    exercise.run_init()

    result = exercise.run_code("print(x)\nx+1")

    assert json.loads(result) == [
        {"type": "output", "payload": "10"},
        {"type": "result", "payload": "11"},
    ]


def test_run_code_error():
    pec = "x = 10"
    solution = ""
    sct = ""
    exercise = PyodideExercise(pec=pec, solution=solution, sct=sct)
    exercise.run_init()

    result = exercise.run_code("this is invalid syntax")

    assert json.loads(result) == [
        {
            "type": "error",
            "payload": '  File "<script.py>", line 1\n    this is invalid syntax\n                    ^^^^^^\nSyntaxError: invalid syntax\n',
        }
    ]


def test_run_submit():
    pec = ""
    solution = """
# Create a variable savings
savings = 100

# Print out savings
print(savings)
"""
    sct = """
Ex().check_object("savings").has_equal_value(incorrect_msg="Assign `100` to the variable `savings`.")
Ex().has_printout(0, not_printed_msg = "Print out `savings`, the variable you created, with `print(savings)`.")
success_msg("Great! Let's try to do some calculations with this variable now!")
    """
    exercise = PyodideExercise(pec=pec, solution=solution, sct=sct)
    exercise.run_init()

    code = """
savings = 100
print(savings)
    """
    result = exercise.run_submit(code)

    assert json.loads(result) == [
        {
            "payload": {"output": "100", "script_name": "script.py"},
            "type": "script-output",
        },
        {
            "payload": {
                "correct": True,
                "message": "Great! Let's try to do some calculations with this variable now!",
            },
            "type": "sct",
        },
    ]


def test_run_submit_sct_failure():
    pec = ""
    solution = """
# Create a variable savings
savings = 100

# Print out savings
print(savings)
    """
    sct = """
Ex().check_object("savings").has_equal_value(incorrect_msg="Assign `100` to the variable `savings`.")
Ex().has_printout(0, not_printed_msg = "Print out `savings`, the variable you created, with `print(savings)`.")
success_msg("Great! Let's try to do some calculations with this variable now!")
        """
    exercise = PyodideExercise(pec=pec, solution=solution, sct=sct)
    exercise.run_init()

    code = """
savings = 123
print(savings)
        """
    result = exercise.run_submit(code)

    assert json.loads(result) == [
        {
            "payload": {"output": "123", "script_name": "script.py"},
            "type": "script-output",
        },
        {
            "payload": {
                "correct": False,
                "message": "Assign <code>100</code> to the variable <code>savings</code>.",
                "line_start": 2,
                "column_start": 1,
                "line_end": 2,
                "column_end": 13,
            },
            "type": "sct",
        },
    ]

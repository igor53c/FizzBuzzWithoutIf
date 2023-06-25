def fizzbuzz(number: int):
    return ("fizz" * (number % 3 == 0) + "buzz" * (number % 5 == 0)) or number


# Scenario 1: Don't use if's in your code
def test_no_if_statements():
    # Test case
    source_code = fizzbuzz.__code__.co_code
    bytecode_instructions = list(source_code)

    for i in range(len(bytecode_instructions) - 2):
        if bytecode_instructions[i] == 100 and bytecode_instructions[i+1] == 0 and bytecode_instructions[i+2] == 100:
            raise AssertionError("Scenario 1: Don't use if's in your code - Failed")


# Scenario 2: Fizzbuzz function returns a number
def test_fizzbuzz_returns_number():
    # Test cases
    assert fizzbuzz(7) == 7
    assert fizzbuzz(13) == 13
    assert fizzbuzz(22) == 22


# Scenario 3: Fizzbuzz function returns "fizz"
def test_fizzbuzz_returns_fizz():
    # Test cases
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(9) == "fizz"
    assert fizzbuzz(12) == "fizz"


# Scenario 4: Fizzbuzz function returns "buzz"
def test_fizzbuzz_returns_buzz():
    # Test cases
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(10) == "buzz"
    assert fizzbuzz(20) == "buzz"


# Scenario 5: Fizzbuzz function returns "fizzbuzz"
def test_fizzbuzz_returns_fizzbuzz():
    # Test cases
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(30) == "fizzbuzz"
    assert fizzbuzz(45) == "fizzbuzz"


# Run the tests and print the results
def run_tests():
    try:
        test_no_if_statements()
        print("Scenario 1: Don't use if's in your code - Passed")
    except AssertionError:
        print("Scenario 1: Don't use if's in your code - Failed")

    try:
        test_fizzbuzz_returns_number()
        print("Scenario 2: Fizzbuzz function returns a number - Passed")
    except AssertionError:
        print("Scenario 2: Fizzbuzz function returns a number - Failed")

    try:
        test_fizzbuzz_returns_fizz()
        print("Scenario 3: Fizzbuzz function returns 'fizz' - Passed")
    except AssertionError:
        print("Scenario 3: Fizzbuzz function returns 'fizz' - Failed")

    try:
        test_fizzbuzz_returns_buzz()
        print("Scenario 4: Fizzbuzz function returns 'buzz' - Passed")
    except AssertionError:
        print("Scenario 4: Fizzbuzz function returns 'buzz' - Failed")

    try:
        test_fizzbuzz_returns_fizzbuzz()
        print("Scenario 5: Fizzbuzz function returns 'fizzbuzz' - Passed")
    except AssertionError:
        print("Scenario 5: Fizzbuzz function returns 'fizzbuzz' - Failed")


# Run the tests and print the results
run_tests()

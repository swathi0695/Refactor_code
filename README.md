## What do you do first?

1. I would try to run the provided tests using pytest to see what errors or issues are currently present. This allows me to see the actual errors before diving into the code and gives me an understanding on the level where the codebase needs fixing.
2. After running all the tests, I would make sure to inspect the test results for failures, exceptions, and unexpected behaviour.
3. I would also examine the code structure and imports to ensure everything is in the correct place (e.g., mock import).
4. I would separate the API from the tests and refactor the code. This allows the code to be clean, organised and structured.

## Write down everything that is wrong / broken with the code, and explain why it's wrong.

Solution present in ```annotated_code.py```. Below is the analysis of the issues I've found:

- Issue with API code:
    1. Type hint on make_api_call is incorrect. The parameter url is marked as an int, but it should be a str since urlparse expects a string and URLs are typically strings.
    2. The function has an empty docstring. Ideally, this should describe the function's behavior and parameters.
    3. If the "if" statement fails (i.e., url has a query string), the response variable is never initialized. Attempting to return response.json() will raise an error.
    4. response.json() is likely to return a dictionary or list, and adding 3 to it will raise a TypeError. It’s unclear what the intention was here.
- Issue with Test code:
    1. The first test (test_make_api_call_1) simply asserts True, which doesn't actually test anything.
    2. The second test has a misplaced assertion: assert_not_called() is used incorrectly. It's a method that
      asserts the mock object has not been called, but it’s not in a valid assertion statement.
    3. No assertions are checking the correctness of make_api_call’s output.
    4. Test structure: Mocking is set up globally but not used in a way that would test the actual request calls.

## Rewrite the code in a way that makes sense to you.

Solution present in the ```clean_code```. It has been split and structured in to have ```api``` and ```tests``` folder


# spy_test

This repo cotains a trivial example of how to mock out a function with a 
[spy](https://martinfowler.com/bliki/TestDouble.html).

**Scenario**: We have a function that deletes a file, and that function is called within another
function we want to test.  We want to test the outer function without actually deleting the file -
but we also want to test that the code *would* have deleted the file.


###`foo.py` 

Two functions that act as the library in this example:

* `bar()` deletes the file `empty.txt`
* `foo()` calls `bar()` and then returns 42

### `main.py`

This file is the driver that utilizes the library  It imports `foo`, calls it, and prints out the result.  
When run, this will delete `empty.txt`  If you run it, be sure to recreate te `empty.txt` file so you can 
see that the mock works. 

### `test_foo.py`

We use the `patch` decorator from `unittest.mock` to create a test double for bar.  The parameter to
the test, `mock`, gives us a name for that double, which is an instance of `Mock`.  After we call `foo()`,
we ask the `mock` whether it was called.


## Things To Try:

To see that all this works:

* Run `pytest` and see that the test passes.
* Comment out the call to `bar` in `foo`.  Rerun `pytest` and see that the test fails.
* Note that in both the above, the file `empty.txt` is still present - it isn't deleted because the test
double mocks out the code that would delete the file.
* Run `main.py` and notice that the file is deleted. 


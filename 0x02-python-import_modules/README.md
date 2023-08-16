# Python - Importing and Modules

This project covered the concepts of importing and utilizing functions, as well as creating modules in Python. It also involved practicing the use of the built-in function `dir()` and incorporating command-line arguments in Python programs.

## Tasks :page_with_curl:

* **0. Utilizing a Basic Function from a Simple File**
  * [0-add.py](./0-add.py): This Python program imports the function `def add(a, b):` from the file [add_0.py](./add_0.py) and displays the outcome of the addition `1 + 2 = 3`.
  * Output: `<a value> + <b value> = <add(a, b) value>` followed by a new line.

* **1. Introducing My First Toolbox!**
  * [1-calculation.py](./1-calculation.py): In this Python program, functions are imported from the file [calculator_1.py](./1-calculator.py), and the results of addition, subtraction, multiplication, and division of `10` and `5` are displayed.
  * Output: `<a value> <operator> <b value> = <operation(a, b) value>` followed by a new line.

* **2. Making a Script Dynamic!**
  * [2-args.py](./2-args.py): This Python program displays the count and list of its arguments.
  * Output: `[Number of arguments] argument` (if there is only one argument) or `arguments` (if there are multiple arguments), followed by:
    * `:` (or `.` if no arguments were passed), followed by
    * A new line, followed by
    * One argument per line - the argument's position (starting at `1`), followed by `:` and the argument value on another line.

* **3. Summing Infinitely**
  * [3-infinite_add.py](./3-infinite_add.py): This Python program prints the sum of all provided arguments.
  * Output: Sum of the arguments followed by a new line.

* **4. Identifying Names**
  * [4-hidden_discovery.py](./4-hidden_discovery.py): This Python program prints all the names defined within the compiled module `hidden_4.pyc`.
  * Output: Names listed alphabetically, one per line.
  * Names starting with `__` are excluded.

* **5. Importing Everything**
  * [5-variable_load.py](./5-variable_load.py): In this Python program, the variable `a` is imported from the file [variable_load_5.py](./variable_load_5.py), and its value is displayed.

* **6. Creating a Personal Calculator**
  * [100-my_calculator.py](./100-my_calculator.py): This Python program imports all functions from the file [calculator_1.py](./calculator_1.py) and manages basic arithmetic operations.
  * Usage: `./100-my_calculator.py <a> <operator> <b>` followed by a new line.
  * Output: `<a> <operator> <b> = <result>` followed by a new line.
  * The `operator` parameter can be:
    * `+` for addition
    * `-` for subtraction
    * `*` for multiplication
    * `/` for division
  * If the operator is not one of the above, the function prints `Unknown operator. Available operators: +, -, *, and /` followed by a new line and exits with a status value of `1`.
  * If the number of arguments is not three, the program prints `Usage: ./100-my_calculator.py <a> <operator> <b>` followed by a new line and exits with a status value of `1`.

* **7. Simple Printing**
  * [101-easy_print.py](./101-easy_print.py): This Python program prints `#pythoniscool` followed by a new line in the standard output.
  * Achieved without using `print`, `eval`, `open`, or `sys`.

* **8. ByteCode Translated to Python #3**
  * [102-magic_calculation.py](./102-magic_calculation.py): This Python function precisely matches a bytecode provided by Holberton School.

* **9. Rapid Alphabet Display**
  * [103-fast_alphabet.py](./103-fast_alphabet.py): This Python program prints the uppercase alphabet followed by a new line.
  * Accomplished without utilizing loops, conditionals, `str.join()`, string literals, or system calls.

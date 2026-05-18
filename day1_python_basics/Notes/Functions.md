n Python, a function is a reusable block of organized, executable code that performs a single, related action. Instead of writing the same logic over and over again throughout your script, you can wrap that logic inside a function and call it whenever you need it.
Functions help break down large programs into smaller, modular, and manageable chunks.

Syntax of a Function:

To define a function in Python, you use the def keyword, followed by the function name, parentheses (), and a colon :

def function_name(parameters):
    """Optional docstring describing what the function does"""
    # Code block (indented)
    return value  # Optional

Parameters vs. Arguments

Parameters: Placeholders defined in the function signature to receive data.
Arguments: The actual data values passed to the function when it is called.
While parameters remain constant in the definition, arguments can change with every call.

Return Values:

The return statement exits a function and sends a specific value back to the caller.
An "early return" can be used to exit a function before reaching the end (e.g., if input validation fails).
If no value is specified, the function returns None by default.

Default Arguments:
You can provide default values for parameters. If an argument is not provided during the call, the function uses the default.

Scope: Global vs. Local

Global Variables: Defined outside functions and accessible anywhere.
Local Variables: Defined inside a function and only accessible within that specific code block.
Local variables take precedence over global variables with the same name during function execution

Lambda Functions

Lambda functions are small, anonymous functions restricted to a single expression.
They are often used with higher-order functions like map() and filter()

Syntax: lambda arguments : expression

Variable-Length Arguments (*args and **kwargs)

Professional code often uses these when the number of inputs is unknown:
*args: Receives extra positional arguments as a tuple.
**kwargs: Receives extra keyword arguments as a dictionary.

ype Annotations
Professional developers use type hints to document expected input and output types, aiding build-time checks.

def process_data(id: int) -> str: # [27]
    return f"Processing ID: {id}"



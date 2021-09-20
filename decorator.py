"""Basic components"""


# Step 1: Assigning functions to variables
def my_func(name):
    print("Hello", name)


print_name = my_func

print_name("Vik")


# Step 2: Defining functions inside functions
def get_square(number):

    def square_number(num):
        return num * num

    result = square_number(number)

    return result


print(get_square(5))


# Step 3: Passing functions as arguments to other functions
def square(number):
    return number * number


def call_function(function):
    number_to_square = 5
    return function(number_to_square)


print(call_function(square))


# Step 4: Functions returning other functions
def print_something():
    def print_five():
        return print("Five")

    return print_five


print_it = print_something()

print_it()


"""Creating a decorator"""


# Now we can create a decorator
def decorator_one(function):
    def _wrapper():
        func = function()
        convert_to_uppercase = func.upper()
        return convert_to_uppercase

    return _wrapper


# Write a function that you will want to decorate
def say_five():
    return "Five"


# One way to use the decorator
decorate = decorator_one(say_five)
print(decorate())


# Pythonic way to decorate the function
@decorator_one
def say_five():
    return "Five"


print(say_five())


# Accepting arguments in decorator functions
def decorator_two(function):
    def _wrapper_two(*args):
        print("The received arguments are: ", args)

        function(*args)

    return _wrapper_two


@decorator_two
def just_words(word1, word2):
    return None


just_words("Hello", "World")


# Passing arguments to the decorator itself
def decorator_three(decorator_arg1, decorator_arg2):
    def decorator(function):
        def _wrapper(function_arg1, function_arg2):

            print("The wrapper can access all arguments: \n"
                  "\t- from the decorator maker: {0} {1}\n"
                  "\t- from the function call: {2} {3} \n"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2)
                  )

        return _wrapper
    return decorator


@decorator_three("One", "Two")
def decorated_function(arg1, arg2):
    return None

decorated_function("Three", "Four")



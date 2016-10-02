# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def total_cost(cost, state, tax=.05):
    """ Returns cost of meal with state tax added """

    if state.upper() == "CA":  # just in case user enters "ca or Ca"
        tax = .07
    return cost + cost * tax

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".


def is_berry(fruit):
    """ Returns True if arg is strawberry, cherry or blackberry """

    return fruit in ["strawberry", "cherry", "blackberry"]


#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit):
    """ Returns 0 if fruit is a berry; otherwise returns 5 """

    result = 5
    if is_berry(fruit):
        result = 0
    return result


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.


def is_hometown(town):
    """ Returns True if input town is 'Acton' (my hometown) """

    if town == "Acton":
        return True
    else:
        return False


#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


def full_name(first_name, last_name):
    """ Concatenates first and last names """

    #return first + " " + last
    return "{} {}".format(first_name, last_name)


#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def hometown_greeting(town, first_name, last_name):
    """ Greets by full name, depending on where from """

    name = full_name(first_name, last_name)

    if is_hometown(town):
        print "Hi, %s, we're from the same place!" % name
    else:
        print "Hi %s, where are you from?" % name


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.


def add(x, y):
    """ Adds x and y """

    return x + y


def increment(y, x=1):
    """ Increments y by default value of 1 """

    return add(x, y)


# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.


addfive = increment(5, 5)
addfive = increment(20, 5)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def custom_append(num, num_list):
    """ Appends number to list of numbers """

    #num_list.append(num)   Is this allowed? This seems too easy.

    #num_list[-1:] = [num_list[-1], num]
    num_list += [num]

    return num_list

#####################################################################

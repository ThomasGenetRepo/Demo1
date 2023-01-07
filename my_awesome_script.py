def my_awesome_function(x, y):
    z = x+y
    return z

def my_even_more_awesome_function(x ,y):
    z = x**y
    return z

def main():
    x, y = 2, 2
    z1 = my_awesome_function(x, y)
    z2 = my_even_more_awesome_function(x, y)

if __name__ == '__main__':
    main()
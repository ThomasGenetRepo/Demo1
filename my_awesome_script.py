# This funcion is truely awesome!!! 
my_awesome_function = lambda x, y: x + y

# But this function is the awesomest funciton ever!!! 
my_even_more_awesome_function = lambda x, y: x ** y


def main():
    x, y = 2, 2
    z1 = my_awesome_function(x, y)
    z2 = my_even_more_awesome_function(x, y)

    print(f"Passing {x} & {y} to my awesome function gives: {z1}")
    print(f"Passing {x} & {y} to my eevn more awesome function gives: {z2}")

# lol if main then call main
if __name__ == '__main__':
    main()
def get_half_even_number(number):
    if number % 2 == 0:
        return number / 2
    else:
        message = (
        f"This Function only supports halving even numbers. Received: {number}"
        )
        raise Exception(message)

def increase_percent(initial_value, after_value):
    try:
        return (after_value / initial_value) * 100
    except ZeroDivisionError:
        return 0
    except Exception as error:
        print("Uh oh, unexpected error occurred!")
        raise error

# get_half_even_number(11)

print(increase_percent(0, 10))
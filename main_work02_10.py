while True:

    try:
        user_input = int(input('>>>'))
        print(user_input)
        break
    except ValueError as e:
        print(f"Not a number, {e}. Try again")

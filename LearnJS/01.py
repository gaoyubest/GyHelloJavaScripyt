def closer():
    index = 0

    def return_function():
        nonlocal index
        print(index)
        index += 1
    # index = 0
    return return_function


if __name__ == '__main__':
    print("\n闭包演示")
    f = closer()
    f()
    f()
    f()

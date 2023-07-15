def check_type(obj):
    match obj:
        case int:
            print("Object is an integer")
        case str:
            print("Object is a string")
        case list:
            print("Object is a list")
        case _:
            print("Object is of an unknown type")

# Test the function
check_type(10)  # Object is an integer
check_type("Hello")  # Object is a string
check_type([1, 2, 3])  # Object is a list
check_type(3.14)  # Object is of an unknown type

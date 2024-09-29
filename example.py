def example_function():
    # A sample function with some performance issues and potential code smells.
    result = []
    for i in range(1000):
        result.append(i * 2)  # Inefficient use of list append in a loop
    
    return result


# colocando um comentário
def unused_function():
    # Unused code example (code smell)
    return "This function is never called"
print(example_function())

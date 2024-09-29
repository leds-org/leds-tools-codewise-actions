def example_function():
    # A sample function with some performance issues and potential code smells.
    result = []
    for i in range(1000):
        result.append(i * 2)  # Inefficient use of list append in a loop
    
    return result
# colocando um comentário sei lã o que tem aqui  dkjhkdhkahskhkds
def unused_function():
    # Unused code example (code smell)
    return "This function is never called"
## mais um comentário
print(example_function())

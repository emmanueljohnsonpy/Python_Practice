

# decorator to convert string returns to lowercase

def to_lowercase(func):
    def wrapper(*args, **kwargs):
        res = func(*args)
        return res.lower() if isinstance(res, str) else res
    return wrapper

@to_lowercase
def greet(word):
    return f"Hai, {word}"
    
print(greet("Ronaldo"))
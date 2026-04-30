# Documenting Functions
# Functions can get complicated so you want to explain it

# You can either add an explainer text this is called a docstring
# You can also hint at what types of data you expect for the parameters and the return value

def test(a:int = 10,b:int = 0):
    """A simple function that print 2 parameter"""
    print(a)
    print(b)
    return a + b
test(1,2)
print(test.__doc__)
help(test)


# Short Circuiting

## Using "and" and "or" on expressions can sometimes short circuit the code

# and = True if both condition1, condition2 = True
# and = False if condition1 = False or condition2 = False
## if condition1 = False, the interpreter doesn't even care about condition2, the expression will evaluate to False anyway (short circuit)


# or = True if condition1 = True or condition2 = True
# or = False if condition1 = False or condition2 = False
## if condition1 = True, the interpreter doesn't even care about condition2, the expression will evaluate to True anyway (short circuit)
## if condition1 = False, the interpreter doesn't even care about condition2, the expression will evaluate to False anyway (short circuit)
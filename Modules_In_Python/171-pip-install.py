# Python packages can be installed directly in PyCharm and they'll be installed in the virtual environment,
# an example is in the test.py file from the modules project

# But most of the time we'll install these directly from a terminal into our local environment

import pyjokes

print(pyjokes.get_joke('en', 'neutral'))
# What does 'Emacs' stand for? 'Exclusively used by middle aged computer scientists.'

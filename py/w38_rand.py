#!/usr/bin/python
print('Content-type: text/html\n')

import random

# Print some text and a random number
print("<html>")
print("<head><title>Random Number</title></head>")
print("<body>")
print("<h1>Hello, World!</h1>")
print("<p>Random number: {}</p>".format(random.randint(1, 100)))
print("</body>")
print("</html>")


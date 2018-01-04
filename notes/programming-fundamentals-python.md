# Programming fundamentals w/ Python

- "Take a break" program
    - Waits 2 hours
    - Plays favorite song after 2 hours by:
        - Opening browser
        - Playing youtube vid
    - Repeats 3 times

`import webbrowser`

Open a web browser in python using `webbrowser.open("_website_")`

Python standard library includes modules (like webbrowser, time, etc.) with functions that you can use just by reading documentation

### Classes

ex) with `turtle` - there is a `Turtle` class inside of the `turtle` python module
function `__init__` inside class Turtle is the constructor

- Class: blueprint
- Instance/Object: an object created from the class 

`from` - for importing a specific variable, class or a function from a module

`self` is always first argument to constructor, it represents the instance being created

### File I/O

`open(_file_)` is in python std lib but not a member of a package
    - called "built in functions"
    - returns an object of the file type

```python
import urllib.request

python_site = urllib.request.urlopen('http://python.org')
```



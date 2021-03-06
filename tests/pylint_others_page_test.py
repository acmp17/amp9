def test_oops_terms_page_content(client):
    """This confirms content on the OOP Terms page"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>OOP Terms</title>
    </head>
    <body>""" in response.data
    assert b"<h1>Object Oriented Programming Terms</h1>" in response.data
    assert b'<div class="text">' in response.data
    assert b"<h2>Instantiation</h2>" in response.data
    assert b"<p>the creation of an object. Sometimes referred to as the running process of an instance in a given class.</p>" in response.data
    assert b"<h2>Object</h2>" in response.data
    assert b"""<p>regions of memory that contain a value and referenced by identifiers. Can be a combination of variables,
            functions, and data structures.</p>""" in response.data
    assert b"<h2>Class</h2>" in response.data
    assert b"""<p>Used to describe one or more objects that are related and share common characteristics. Serves as a template
            for creating, instantiating, or specifying objects within a program. </p>""" in response.data
    assert b"<h2>Namespace</h2>" in response.data
    assert b"<p>a container or environment created to hold a logical grouping of unique identifiers.</p>" in response.data
    assert b"<h2>Constructor</h2>" in response.data
    assert b"""<p>a function that is automatically called whenever an instance of the class is created. Also contains the
            collection of instructions that are executed at the time of object creation. Used to assign initial values
            to the data members of the same class. Always has the same name as the class, no return type.
        </p>""" in response.data
    assert b"<h2>Fixture</h2>" in response.data
    assert b"""<p>will run before each test function to which it is applied as preparation needed to perform one or more tests,
            any associated cleanup actions. They provide scalable and comprehensible content for tests. Available for
            tests to request if they are in the scope that fixture is defined in.</p>""" in response.data
    assert b"<h2>Type Hint</h2>" in response.data
    assert b"""<p>formal solution to statically indicate the type value within your Python code.
            type cast. Metadata that can be used for either static analysis or at runtime.
        </p>""" in response.data
    assert b"<h2>Unit Test</h2>" in response.data
    assert b"""<p>supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into
            collections, and independence of the tests from the reporting framework. Provides a rich set of tools for
            constructing and running tests.
        </p>""" in response.data
    assert b"<h2>Static</h2>" in response.data
    assert b"""<p>can be called directly from the class by reference to the class. Cannot access or modify the class attributes
            in the Python programming language, but is only bound to the class. Python doesnt require any static
            keywords.
        </p>""" in response.data
    assert b"<h2>Instance Method</h2>" in response.data
    assert b"""<p>used to access or modify the object state including attributes. Using instance variables inside a method.
            Must have a self parameter to refer to the current object.</p>""" in response.data
    assert b"<h2>Instance Property</h2>" in response.data
    assert b"""<p>to create special class attributes, instance attributes that are derived from a Python property class. Using
            getters and setters in object-oriented programming</p>""" in response.data
    assert b"<h2>Static Method</h2>" in response.data
    assert b"""<p>can be called without creating an object or instance. Call a method in a class without creating an
            object.</p>""" in response.data
    assert b"<h2>Static Property</h2>" in response.data
    assert b"<p>similar to static method if you want to be computed at class definition time.</p>" in response.data
    assert b"<h2>SOLID</h2>" in response.data
    assert b"""<ul>
            <li>The Single-Responsibility Principle (SRP): being able to split the operations of your code into more
                subparts then making a single function (class), generally called main that calls the other functions
                step-to-step. This can localize errors more conveniently, any part of the code is reusable, and easier
                to create testing for each function in the code.
            </li>
            <li>The Open-Closed Principle (OCP): You should not require to change other parts of the code when adding
                new functions that are similar to the one in the present. Creating new method functions and adding an
                extension as its invocation to the main. Only modifying the main where the former classes are being
                picked up.
            </li>
            <li>The Liskov Substitution Principle (LSP): if you are using a function there should not be a noticeable
                difference between the functions in the base class so the user should expect the same behavior from the
                two. In order to code in a consistent way.
            </li>
            <li>The Interface Segregation Principle (ISP): create more client-specific interfaces rather than one
                general-purpose interface. Keep the content of a subclass clean from elements of no use to that subclass
                in order to have classes clean and minimize mistakes
            </li>
            <li>The Dependency inversion Principle (DIP):adding a third abstraction that takes info as input and passes
                it to the others.
            </li>
        </ul>""" in response.data
    assert b"<h2>Design Patterns</h2>" in response.data
    assert b"""<p>premade blueprints that designers can customize to solve a recurring design problem in the code. One can follow the pattern details and implement a solution that is suitable for their own program. It is a tool that contains tried and tested solutions to common problems in software design. It can also have a team communicate more efficiently.</p>
        <ul>
            <li>Creational patterns: provide object creation mechanisms that increase flexibility and reuse of existing code.</li>
            <li>Structural patterns: explain how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient</li>
            <li>Behavioral patterns: take care of effective communication and the assignment of responsibilities between objects.</li>
        </ul>""" in response.data
    assert b'<a href="https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/"> How to explain object-oriented programming concepts to a 6-year-old</a> <br>' in response.data
    assert b'<a href="https://realpython.com/python-namespaces-scope/"> Namespaces and Scope in Python</a> <br>' in response.data
    assert b"</div>" in response.data
    assert b"</body>" in response.data
    assert b"</html>" in response.data
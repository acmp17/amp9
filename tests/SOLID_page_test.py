def test_SOLID_page_content(client):
    """This confirms content on the SOLID page"""
    response = client.get("/page8")
    assert response.status_code == 200
    assert b"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>SOLID</title>
    </head>
    <body>""" in response.data
    assert b"<h1>SOLID article</h1>" in response.data
    assert b'<div class="text">' in response.data
    assert b"""<h2>Single-Responsibility Principle (SRP)</h2>
        <p>being able to split the operations of the code into subparts and making a single function class, main.
            The main class will call all the other functions one-by-one during a step by step process.</p>
        <h2>The Open-Closed Principle (OCP)</h2>
        <p>Creating new method functions should add an extension to the main class. One can add on to the subclasses'
            functions,
            then making simple modifications to the main.</p>
        <h2>The Liskov Substitution Principle (LSP)</h2>
        <p>There should not be a noticeable difference between the functions of the base class so the user can expect
            the same behavior. </p>
        <h2>The Interface Segregation Principle (ISP)</h2>
        <p>Keep the content of a subclass clean from elements of no use to that subclass in order to have classes clean
            and minimize mistakes</p>
        <h2>The Dependency Inversion Principle (DIP)</h2>
        <p>adding a third abstraction that takes info as input and passes it to the others. Example: operations
            folder</p>
        <h2>Design Patterns</h2>
        <p>Structural design patterns are about organizing different classes and objects to form larger structures and
            provide new functionality while keeping these structures flexible and efficient.</p>
        <p>Creational patterns provides essential information regarding the Class instantiation or the object
            instantiation.</p>
        <p>Behavioral patterns are all about identifying the common communication patterns between objects and realize
            these patterns. These patterns are concerned with algorithms and the assignment of responsibilities between
            objects.</p>""" in response.data
    assert b"""<a href="https://towardsdatascience.com/solid-coding-in-python-1281392a6a94"> SOLID Coding in Python</a> <br>
        <a href="https://www.geeksforgeeks.org/solid-principle-in-programming-understand-with-real-life-examples/"> SOLID Principle in Programming: Understand With Real Life Examples</a>""" in response.data
    assert b"</div>" in response.data
    assert b"</body>" in response.data
    assert b"</html>" in response.data
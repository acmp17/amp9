def test_OOPs_page_content(client):
    """This confirms content on the OOPs page"""
    response = client.get("/page7")
    assert response.status_code == 200
    assert b"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>OOPs</title>
    </head>
    <body>""" in response.data
    assert b"<h1>Object Oriented Programming</h1>" in response.data
    assert b'<div class="text">' in response.data
    assert b"""<h2>Encapsulation</h2>
        <p>restrict access to methods and variables that are inside the class. Modifications from outside of the class
            cannot be made so to change the value we would have to use a setter function to take the value as a
            parameter. The self.result value is restricted only to modifications within the class as it is
            encapsulated.</p>
        <h2>Inheritance</h2>
        <p>Creating a class for using details in another existing class without modifying it. The new formed class would
            be
            derived as a child class and the existing class as the parent class (base class). Method of the parent class
            is
            called inside the child class. The def add classes are derived child classes of the parent class
            "calculator"</p>
        <h2>Polymorphism</h2>
        <p>Creating a common interface that takes any object and calls the objects method. Each type can provide its
            own
            independent implementation of this interface.</p>
        <h2>Abstraction</h2>
        <p>Hide the internal functionality of the function from the users. The users can interact with the basic
            implementation, but the inner workings are hidden in order to reduce complexity. The base class of
            calculator
            did not need critical modifications, but the operation derived classes are what have the complex
            functionality </p>""" in response.data
    assert b'<a href="https://www.programiz.com/python-programming/object-oriented-programming"> Python Object Oriented Programming</a>' in response.data
    assert b"</div>" in response.data
    assert b"</body>" in response.data
    assert b"</html>" in response.data
def test_AAA_page_content(client):
    """This confirms content on the AAA page"""
    response = client.get("/page6")
    assert response.status_code == 200
    assert b"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>AAA Testing</title>
    </head>
    <body>""" in response.data
    assert b"<h1>AAA</h1>" in response.data
    assert b'<div class="text">' in response.data
    assert b"""<h2>Arrange</h2>
        <p>the block of code that sets up the conditions of the test action. Handle all these operations at the at the
            start
            of the test</p>
        <h2>Act</h2>
        <p>Action is taken on the Systems Under Test. Either consists of calling a function or interacting with a web
            page
            focusing on the target behavior.</p>
        <h2>Assert</h2>
        <p>verify the good or bad results of the response. Determines if the test passes or fails. Assertions can check
            numeric or string values or multiple facets of a system.</p>
        <p>The importance of testing is that it provides critical feedback loops for development. It keeps the program
            safe
            by identifying when things break in the program. In order to prevent bugs in the code. </p>""" in response.data
    assert b'<a href="https://jamescooke.info/arrange-act-assert-pattern-for-python-developers.html"> Arrange Act Assert pattern for Python developers</a>' in response.data
    assert b"</div>" in response.data
    assert b"</body>" in response.data
    assert b"</html>" in response.data
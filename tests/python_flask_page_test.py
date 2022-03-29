def test_request_python_flask_content(client):
    """This tests the python flask info page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Python/Flask</title>
    </head>
    <body>""" in response.data
    assert b'<h2>Pytest</h2>' in response.data
    assert b"<h2>Outline</h2>" in response.data

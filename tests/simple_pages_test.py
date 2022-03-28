"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/page1">Git</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/page4">Cont. Integration & Deploy</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"" in response.data

def test_request_page1(client):
    """This makes the page1"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_page2(client):
    """This makes the page2"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_page3(client):
    """This makes the page3"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Python/Flask" in response.data

def test_request_page4(client):
    """This makes the page4"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Continuous Integration and Deployment" in response.data

def test_request_page_not_found(client):
    """This makes the page not found page"""
    response = client.get("/page10")
    assert response.status_code == 404

def test_request_carousel(client):
    """This tests the carousel links"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a href="/page1"' in response.data
    assert b'<a href="/page2"' in response.data
    assert b'<a href="/page3"' in response.data
    assert b'<a href="/page4"' in response.data
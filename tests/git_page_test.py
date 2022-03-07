"""This test is for the git page"""

def test_request_git(client):
    """This confirms content on the git page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"<header>All About Git</header>" in response.data
    assert b"<h2>Git</h2>" in response.data
    assert b"<h2>Branches</h2>" in response.data
    assert b"<h2>Merge</h2>" in response.data
    assert b"<h2>Commit</h2>" in response.data
    assert b"<h2>Tags</h2>" in response.data
    assert b"<h2>Repositories</h2>" in response.data
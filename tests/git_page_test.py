"""This test is for the git page"""

def test_request_git(client):
    """This confirms content on the git page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"<h1>Git</h1>" in response.data
    assert b"<h1>Branches</h1>" in response.data
    assert b"<h1>Merge</h1>" in response.data
    assert b"<h1>Commit</h1>" in response.data
    assert b"<h1>Tags</h1>" in response.data
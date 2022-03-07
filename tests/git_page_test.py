"""This test is for the git page"""

def test_request_git(client):
    """This confirms content on the git page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"<h1>Git</h1>" in response.data
    assert b"<p>Git is the most popular version control system in the world which makes it easier to track changes in a file." in response.data
    assert b"It is a great tool to coordinate with other developers and save checkpoints on what is changed over time." in response.data
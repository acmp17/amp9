"""This test is for the docker page"""

def test_request_docker(client):
    """This confirms content on the docker page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"<h2>Docker</h2>" in response.data
    assert b"<h2>Containers</h2>" in response.data
    assert b"<h2>Images</h2>" in response.data
    assert b'<a href="https://hub.docker.com/repository/docker/acmp17/project1-amp">Visit DockerHub Project Repository</a>' in response.data

def test_docker_commands_list(client):
    """This confirms content in the docker commands list"""
    response =  client.get("/page2")
    assert response.status_code == 200
    assert b"<h2>Docker Commands to know</h2>" in response.data

def test_docker_starter(client):
    """This tests the docker starter description"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"<h2>How to start A Project with Docker</h2>" in response.data
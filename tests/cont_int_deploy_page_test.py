def test_content_on_cont_int_deploy(client):
    """This confirms content on the git page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"<h2>Continuous Integration</h2>" in response
    assert b"<h2>Continuous Deployment</h2>" in response

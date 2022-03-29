def test_content_on_cont_int_deploy(client):
    """This confirms content on the cont int page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Continuous Integration & Deployment</title>
    </head>
    <body>""" in response.data
    assert b"<h1>All about Continuous Integration and Deployment</h1>" in response.data
    assert b'<div class="text">' in response.data
    assert b"<h2>Continuous Integration</h2>" in response.data
    assert b"""<p>Continuous Integration is the practice of testing each change done to your project and at an early efficient time.
                Members of a team can utilize the process of collaborating on code which causes for multiple integrations in a single day.
                This reduces problems from showing up when working.</p>""" in response.data
    assert b"<h2>Continuous Deployment</h2>" in response.data
    assert b"""<p>Continuous deployment is towards the end of the Continuous Integration process. It
            automates the delivery of applications to selected infrastructure environments.</p>""" in response.data
    assert b"""<p>GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline.
                You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.</p>""" in response.data
    assert b"""<p>Since in both the dev.yml and prod.yml files I have pytest code running, it does a job whenever the changes in the project file triggers it. The pip install command always looks for the latest version of the package and installs it.
                You can review code using a development server before merging pull requests by searching localhost on the web browser. You can deploy master to a production server by pushing to the prod branch from the yml file</p>""" in response.data
    assert b"</div>" in response.data
    assert b"</body>" in response.data
    assert b"</html>" in response.data
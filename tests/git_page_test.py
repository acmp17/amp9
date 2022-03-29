"""This test is for the git page"""


def test_git_page_content(client):
    """This confirms content on the git page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"""    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Git</title>
    </head>
    <body>
    <h1>All About Git</h1>
    <div class="text">""" in response.data
    assert b'<h2>Git</h2>' in response.data
    assert b"""<p>Git is the most popular version control system in the world which makes it easier to track changes in a file.
            It is a great tool to coordinate with other developers and save checkpoints on what is changed over time.""" in response.data
    assert b"""You can download Git by its commandline interface. Github is the website that is used for hosting the
            projects that use git.</p>""" in response.data
    assert b'<h2>Branches</h2>' in response.data
    assert b"""<p>Branches that are being used in git are similar to how File > Save as.. In a text editor.
            The branch name is for reference of the current state of your project.
            One branch can be for working on a single feature and another branch can be for applying another feature</p>""" in response.data

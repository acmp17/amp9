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
    assert b'<h2>Merge</h2>' in response.data
    assert b"""<p> The concept of merge lets you take the independent lines created by git branches and integrate them into a
            single branch (most likely the default branch). If someone makes changes to the master branch on git, you
            can
            do the merge command to update your local master branch. Merge conflicts occur when multiple people are
            making
            changes to the file on the same lines at the same time.
            Pull command is to fetch the information changed on the master branch and merge automatically to the local
            branch on the device.</p>""" in response.data
    assert b'<h2>Commit</h2>' in response.data
    assert b"""<p>Commits are basically a capture of the projects currently saved changes. These captures can be known as the
            safe versions of the project.
            The add command helps prepare the marked changes on the file before actually committing. Commit makes the
            changes on the local repository and
            then the push command sends the changes out to the remote location (Github). </p>""" in response.data
    assert b'<h2>Tags</h2>' in response.data
    assert b"""<p>Tags are reference points in Gits history. Unlike branches, it does not change and they dont have a further
            history of commits after being created.
            Annotated tags store extra metadata information like a name and an extra message. Lightweight tags are
            bookmarks to a commit.
            It is either utilized for a name or specific pointers to a commit.</p>""" in response.data
    assert b'<h2>Repositories</h2>' in response.data
    assert b"""<p>Repositories in git contain a collection of files of different version types in a project. These files are
            imported from repositories that are in the local server
            and the user can update and modify the contents in the file. After those changes are made, they can update
            the repository on the remote location. </p>
    </div>
    </body>
    </html>""" in response.data

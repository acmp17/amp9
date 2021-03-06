def test_python_flask_content(client):
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
    assert b"<h1>All about Python/Flask</h1>" in response.data
    assert b'<div class="text">' in response.data
    assert b"<h2>Pytest</h2>" in response.data
    assert b"""<p>Pytest is a testing framework that allows users to write test codes using the Python programming language.
            It helps write simple and scalable tests kept in a file for a project. Flask is a web framework that provides useful
            tools and features that make creating web applications with Python much easier.</p>""" in response.data
    assert b"<h2>Outline</h2>" in response.data
    assert b"<p>Project root folder (docker_flask) <- Root of the Project</p>" in response.data
    assert b"""<ul>
                <li>Venv folder <- a tool used to create isolated Python environments.
                    Contains all the necessary executables to use the packages that a Python project would need.
                    Allows you to manage separate package installations for different projects.</li>
                <li>Tests folder <- contains python files that are testing features on the project affecting the workflow.""" in response.data
    assert b"""<ul>
                        <li>Calculator_test.py <- tests the calculator</li>
                        <li>Conftest.py <- makes the test configuration setup</li>
                        <li>Context_process_test.py <- testing approach depends on the context of the software developed.
                            Different types of software need to perform different types of testing</li>
                        <li>Docker_page_test.py <- tests the docker info page</li>
                        <li>Git_page_test.py <- tests the git info page</li>
                        <li>Simple_pages_test.py <- tests the elements of the home page</li>
                    </ul>""" in response.data
    assert b"""</li>
                <li>.dockerignore <- file that allows you to exclude files from context.
                    Helps build faster and lighter excluding big files that are not being used in the build.</li>
                <li>.gitignore <- same concept as .dockerignore where its a file that allows you to exclude big files
                    that are not being used in the build from the git repository. </li>
                <li>.pylintrc <- static code checker that analyses the code without it actually running. checks for errors,
                    tries to enforce a coding standard, and tries to enforce a coding style.</li>
                <li>docker-compose.yml <- Orchestration file that contains the configuration to develop locally,
                    it overrides the Dockerfile to run the flask development server instead of running the gunicorn server that is used for hosting on Heroku</li>
                <li>Dockerfile <-File used to create an image to run in a container that runs the program</li>
                <li>Heroku.yml <- allows you to build docker images on Heroku and define it.</li>
                <li>Pytest.ini <- file that eases the difficulties in typing the same series of command line options every time you use pytest</li>
                <li>Readme.md <- a text file that is attached to a software program that contains critical or important information about that program.</li>
                <li>Requirements.txt <- used to specify python packages that are required to run for the project</li>
                <li>.github folder <- has information that is necessary for the project including and information on commits, remote repository address, a log on commit history. </li>
                <li>.coveragerc <- configuration files that control coverage.py. Checked into source control rather than home directory</li>
                <li>Workflows folder <- folder that combines several workflow tools into one application that automates processes involving machine and human tasks in a sequence""" in response.data
    assert b"""<ul>
                        <li>Dev.yml <- used for writing configuration files for the development portion of the project. Includes pytesting, heroku and docker connections</li>
                        <li>Prod.yml <- used for production appropriate configuration files. Includes pytesting, heroku, and docker connections </li>
                    </ul>""" in response.data
    assert b"""</li>
                <li>App folder <- contains files that are important for the applications functionality
                    <ul>
                        <li>Templates folder/Base.html <- a specific html file that contains what should be consistent on all of the pages of the website </li>
                        <li>Static folder <- contains the css, images, and javascript files that are needed for the lay out of the project.""" in response.data
    assert b"""<ul>
                                <li>Style.css <- a style sheet file that contains information on formatting characteristics and how to display the HTML elements</li>
                                <li>sample.jpeg </li>
                                <li>Scripts.js <- embedded program </li>
                            </ul>""" in response.data
    assert b"""</li>
                        <li>simple_pages/templates <- contains the html for all the different pages in the project (extended from base.html)
                            <ul>
                                <li>index.html <- html for the homepage</li>
                                <li>page1.html <- html for the git page</li>
                                <li>page2.html <- html for the docker page</li>
                                <li>page3.html <- html for the Python/Flask page</li>
                                <li>page4.html <- html for the continuous integration and deployment</li>
                            </ul>
                        </li>""" in response.data
    assert b"""<li>Run.py <- allows Gunicorn (python HTTP server) to serve the app in production</li>
                        <li>Context_processors <- runs before the template is rendered and have the ability to inject new values into the template context
                            <ul>
                                <li>__init__.py <- python function that takes the request object as an argument and returns a dictionary that gets added to the request context</li>
                            </ul>
                        </li>
                        <li>__pycache__ <- directory that contains bytecode cache files that are automatically generated by python</li>
                        <li>__init__.py<- creates and configures an instance of the Flask application</li>""" in response.data
    assert b"</ul>" in response.data
    assert b"</li>" in response.data
    assert b"</ul>" in response.data
    assert b"</div>" in response.data
    assert b"</body>" in response.data
    assert b"</html>" in response.data


"""This test is for the docker page"""


def test_docker_page_content(client):
    """This confirms content on the docker page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Docker</title>
    </head>
    <body>""" in response.data
    assert b"<h1>All About Docker</h1>" in response.data
    assert b'<div class="text">' in response.data
    assert b"<h2>Docker</h2>" in response.data
    assert b"""<p>Docker is an open source containerization platform that lets developers package applications into containers.
            It helps build, run, and manage containers on servers and the cloud. It allows developers to take advantage
            of Dockers methodologies to reduce the delay between writing code and running it in production. </p>""" in response.data
    assert b'<h2>Containers</h2>' in response.data
    assert b"""<p>A docker container is a virtualized environment that isolates an application and its dependencies into a
            self-contained unit that can run anywhere.
            It removes the need of utilizing physical hardware and wasting extra computing resources.
            This concept of containerization is more efficient when it comes to energy consumption and cost
            effectiveness.</p>""" in response.data
    assert b'<h2>Images</h2>' in response.data
    assert b"""<p>Docker images are immutable files that contain source code, libraries, dependencies, tools and other files in
            order for the application to run.
            They represent an application in its virtual environment during specific points in time.
            Images are like templates as base to build a container, which basically runs the image.</p>""" in response.data
    assert b'<a href="https://hub.docker.com/repository/docker/acmp17/project1-amp">Visit DockerHub Project Repository</a>' in response.data
    assert b'</div>' in response.data
    assert b'</body>' in response.data
    assert b'</html>' in response.data

def test_docker_commands_list(client):
    """This confirms content in the docker commands list"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"<h2>Docker Commands to know</h2>" in response.data
    assert b"""<ul>
            <li>Docker login <- login to the docker hub repository</li>
            <li>Docker images <- lists all locally stored docker images</li>
            <li>Docker build <- builds Docker images from a Dockerfile and a given path or url.</li>
            <li>Docker run <- creates a container from a given image and starts the container using a given command</li>
            <li>Docker ps <- used to list the running containers</li>
            <li>Docker stop <- stops running containers</li>
            <li>Docker kill <- stops execution immediately</li>
            <li>Docker rm <- used to delete a stopped container</li>
            <li>Docker commit <- creates a new image of edited container in the local</li>
            <li>Docker push <- used to push an image to the docker hub repository</li>
            <li>Docker pull <- pull images from docker hub repository</li>
        </ul>""" in response.data
    assert b'<h2>How to start A Project with Docker</h2>' in response.data

def test_docker_start_list(client):
    """This tests the docker starter description"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"<h2>How to start A Project with Docker</h2>" in response.data
    assert b"""<p>Firstly, Dockerfile is a text document that one needs to make in order to contain all the commands a user can
            call on the command line to assemble an image.
            Then using docker build command users can automatically execute several command-line instructions
            successfully.
            To see the docker images that you just created the command is docker images (or docker image ls).
            Docker run lets you run the application on a computer that has docker and then you can push and pull the
            image onto the docker hub from the local repository and vice versa.</p>""" in response.data

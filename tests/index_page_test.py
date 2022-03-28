def test_index_page_content(client):
    """This tests the content on the index.html page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"""{% extends "base.html" %}
{% block content %}
    <!-- Carousel -->
    <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
              integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
              crossorigin="anonymous">

        {% block head %}
            <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}"/>
            <title>{% block title %}{% endblock %}This is {{ name }} Website</title>
        {% endblock %}

    </head>
    <body>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <a href="/page1"> <img src="https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png"
                                       class="d-block" alt="..."> </a>
            </div>

            <div class="carousel-item">
                <a href="/page2"><img src="https://thingsolver.com/wp-content/uploads/docker-cover.png" class="d-block"
                                      alt="..."> </a>
            </div>

            <div class="carousel-item">
                <a href="/page3"><img src="https://miro.medium.com/max/640/1*XzIRJGujfqAiOV2EIQgR_Q.png" class="d-block"
                                      alt="..."></a>
            </div>

            <div class="carousel-item">
                <a href="/page4"><img
                        src="https://www.xenonstack.com/hubfs/xenonstack-continuous-integration-and-continuous-delivery.png"
                        class="d-block" alt="..."></a>
            </div>

        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls"
                data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls"
                data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
            crossorigin="anonymous"></script>

    <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
    <p>Alianna Panganiban is a New Jersey Institute Of Technology Student. Currently majoring in Computer Science,
        she is taking IS218 a Building Applications course. This website will be a guide to building web applications
        and
        provide tools in order to execute the code in a test bug free environment.</p>
    </body>
{% endblock %}

""" in response.data

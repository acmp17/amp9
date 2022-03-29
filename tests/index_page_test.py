def test_index_page_content(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<!-- Carousel -->' in response.data
    assert b'<!doctype html>' in response.data
    assert b'<html lang="en">' in response.data
    assert b'<head>' in response.data
    assert b'<!-- Required meta tags -->' in response.data
    assert b'<meta charset="utf-8">' in response.data
    assert b'<meta name="viewport" content="width=device-width, initial-scale=1">' in response.data
    assert b'<!-- Bootstrap CSS -->' in response.data
    assert b'<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"' in response.data
    assert b'integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"' in response.data
    assert b'crossorigin="anonymous">' in response.data
    assert b"""<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}"/>""" in response.data
    assert b"""</head>
    <body>
    <h1>IS218-006 Building Web Applications</h1>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <a href="/page1"> <img src="https://cdn.freebiesupply.com/logos/thumbs/2x/git-logo.png"
                                       class="gitimage" alt="..."> </a>
            </div>

            <div class="carousel-item">
                <a href="/page2"><img src="https://www.pinclipart.com/picdir/middle/116-1161113_docker-logo-png-clipart.png" class="d-block"
                                      alt="..."> </a>
            </div>

            <div class="carousel-item">
                <a href="/page3"><img src="https://pandaprogrammer.com/wp-content/uploads/2020/11/python.jpg" class="d-block"
                                      alt="..."></a>
            </div>

            <div class="carousel-item">
                <a href="/page4"><img
                        src="https://image.slidesharecdn.com/ciandcdinenterprisescenario-160203045816/95/continuous-integration-and-continuous-deployment-in-enterprise-scenario-8-638.jpg?cb=1454475629"
                        class="d-block" alt="..."></a>
            </div>

            <div class="carousel-item">
                <a href="/page5"><img
                        src="https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_9424a42a223635fd4bbac68e393c1181/pylint.png"
                        class="d-block" alt="..."></a>
            </div>

            <div class="carousel-item">
                <a href="/page6"><img
                        src="http://2.bp.blogspot.com/_9kQQgQD35rY/ScqXDQeIoeI/AAAAAAAAAlc/uWnnQL0l-JQ/s400/arrangeActAssert.jpg"
                        class="d-block" alt="..."></a>
            </div>

            <div class="carousel-item">
                <a href="/page7"><img
                        src="https://simplesnippets.tech/wp-content/uploads/2018/03/java-introduction-to-Object-Oriented-Programming.jpg"
                        class="d-block" alt="..."></a>
            </div>

            <div class="carousel-item">
                <a href="/page8"><img
                        src="https://miro.medium.com/max/719/1*s0b7xHpy4AOhDA1ylPMGpw.png"
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
        and provide tools in order to execute the code in a test bug free environment. New addition for Project 2:
        Object Oriented Programming Principles and Examples </p>
    </body>""" in response.data
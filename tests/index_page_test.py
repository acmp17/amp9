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
    assert b"""</head>
    <body>
    <h1>IS218-006 Building Web Applications</h1>""" in response.data
    assert b"""<div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <a href="/page1"> <img src="https://cdn.freebiesupply.com/logos/thumbs/2x/git-logo.png"
                                       class="gitimage" alt="..."> </a>
            </div>""" in response.data

    assert b"""<div class="carousel-item">
                <a href="/page2"><img src="https://www.pinclipart.com/picdir/middle/116-1161113_docker-logo-png-clipart.png" class="d-block"
                                      alt="..."> </a>
            </div>""" in response.data

    assert b"""<div class="carousel-item">
                <a href="/page3"><img src="https://pandaprogrammer.com/wp-content/uploads/2020/11/python.jpg" class="d-block"
                                      alt="..."></a>
            </div>""" in response.data
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


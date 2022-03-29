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
    assert b'<!-- Bootstrap CSS -->' in response.data
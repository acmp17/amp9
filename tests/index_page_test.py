def test_index_page_content(client):
    """This makes the index page"""
    response = client.get("/index")
    assert response.status_code == 200
    assert b'{% extends "base.html" %}' in response.data
    assert b'{% block content %}' in response.data
    assert b'<!-- Carousel -->' in response.data
    assert b'<!doctype html>' in response.data
    assert b'<html lang="en">' in response.data
    assert b'<head>' in response.data
    assert b'<!-- Required meta tags -->' in response.data
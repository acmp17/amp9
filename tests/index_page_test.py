def test_index_page_content(client):
    """This tests the content on the index.html page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'{% extends "base.html" %}' \
           b'{% block content %}' \
           b'<!-- Carousel -->' \
           b'<!doctype html>' \
           b'<html lang="en">' \
           b'<head>' in response.data

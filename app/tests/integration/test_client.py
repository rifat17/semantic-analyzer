def test_analyze(client):
    response = client.post(
        "/predict",
        json={"text": "I love this product! It's the best thing since sliced bread!"},
    )
    assert response.status_code == 200
    assert response.json["sentiment"] == "positive"

def test_create_user_is_saved_to_database(app, db_connection):
    client = app.test_client()

    resp = client.post("/users", data={"username": "testuser", "password": "1234"})

    assert resp.status_code == 200

    result = db_connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    assert len(result) == 1
    assert result[0]["username"] == "testuser"

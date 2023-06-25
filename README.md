# HOWTO

## To run the project, you will need to have Docker installed.

Once you have Docker installed, you can run the following command to build and start the project:

        make run
            or
        docker-compose up --build -d

This will start the server. The server will be available at http://localhost:5000

To get the sentiment of a text, you can use the following curl command:

```bash
curl -X POST \
http://localhost:5000/analyze \
-H "Content-Type: application/json" \
-d '{
    "text": "I love Icecream"
}'
```

The response will be a JSON object containing sentiment of the requested sentence.

---

## To run the tests (**pytest**), you can run the following command:

    make test
        or
    docker-compose run --rm analyzer python -m pytest app/tests/

---

## To format the code with _black_, you can run the following command:

    make black

---

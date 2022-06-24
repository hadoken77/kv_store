To build docker image, run: docker build --tag kv_store .
Then run image: docker run --publish 8000:8000 kv_store
To access application, use browser go to http://http://localhost:8080
To access swagger (for testing): http://http://localhost:8080/docs:8000/docs
This will allow you to test various operations available

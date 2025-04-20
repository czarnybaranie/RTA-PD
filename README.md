# Zadanie 1 - Analiza danych w czasie rzeczywistym

**To run the app:**

First spin up the docker container, eg.:

```
docker build -t pdapi .
docker run -p 8000:8000 pdapi
```

Next, to complete the homework assignment:

```
curl "http://127.0.0.1:8000/api/v1.0/predict?num1=3&num2=4"
```

The app should return: *{"features":{"num1":3.0,"num2":4.0},"prediction":1}*
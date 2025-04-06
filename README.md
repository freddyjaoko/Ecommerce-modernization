# Django-Ecommerce



docker run --name some-postgres --network some-network -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -d postgres


docker build -t ecommerce .

docker run --network=some-network --name my-container -p 8000:8000 -d my-image-name

docker run --name ecommerce -p 8000:8000 -d ecommerce
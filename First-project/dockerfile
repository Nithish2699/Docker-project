FROM python:3.11-slim


WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
EXPOSE 5000

#Command Line Instructions:

#docker build -t sample-project:1.0 .
#docker run -d --name sample-project -p 5000:5000 sample-project:1.0
#docker ps
#docker stop sample-project
#docker rm sample-project
#docker rmi sample-project:1.0
#docker images
#docker system prune -a
#docker exec -it sample-project bash
#docker logs sample-project
#docker inspect sample-project
#docker stats sample-project
#docker-compose up -d --build
#docker-compose down
#docker-compose ps
#docker-compose logs
#docker-compose exec web bash
#docker-compose stop
#docker-compose start
#docker-compose restart web
#docker-compose rm
#docker-compose pull
#docker-compose push    
#docker-compose config
#docker-compose version
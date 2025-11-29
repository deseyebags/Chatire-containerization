This project is a Dockerized version of the Chatire App project by [@danidee10](https://github.com/danidee10).

It's a small project that I did to recap some basics about Docker and Containerization concepts.
In the `master branch`, you will find the updated version of the Chat App project that uses the django channels (redis layer) to achieve real-time messaging.

In the branch `channels-vs-websockets`, you will find the original version of the Chat App project that uses the websockets (uWSGI) to achieve real-time messaging.

Both branches can be run using Docker Compose.

```bash
docker compose up
```


# Acknowledgements

[@danidee10](https://github.com/danidee10) for the [Chat App](https://github.com/danidee10/chat_app) which I used as the basis and foundation for this project.

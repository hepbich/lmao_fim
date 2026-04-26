Запуск в Докере

Создать и запустить контейнер:

```$ export BOT_TOKEN=<BOT_TOKEN>```

```$ export AI_KEY=<AI_KEY>```
```$ export VCHAT_ID=<VCHAT_ID>```
```$ export DCHAT_ID=<DCHAT_ID>```
```$ export SCHAT_ID=<SCHAT_ID>```
```$ docker-compose up -d```

Остановить запущенный контейнер:

```$ docker-compose stop```

Запустить остановленный контейнер:

```$ docker-compose start```

Остановить и удалить контейнер и сеть:

```$ docker-compose down```

Удалить докер-образ:

```$ docker rmi lariska_bot```

Очистить логи:

```$ sudo rm -rf logs/*```

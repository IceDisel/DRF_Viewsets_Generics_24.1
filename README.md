### Как запустить проект с помощью Docker-compose:

В терминале набираем команду

        docker-compose build

docker-compose build — позволяет обновить образы или создать их заново, если они были изменены;

Далее набираем команду

        docker-compose up

docker-compose up — запускает приложение со всеми контейнеры, информация о которых есть в docker-compose.yml. Если файл
не указан, по умолчанию используется файл в текущем каталоге

Остальные команды для DOCKER которыми вы можете воспользоваться в своем проекте.

        docker-compose restart

Docker-compose restart — перезапускает контейнеры;

        docker-compose logs

Docker-compose logs — выводит журналы состояния;

        docker-compose ps

Docker-compose ps — отображает текущее состояние контейнеров.

        docker-compose down

Docker-compose down — останавливает и удаляет все контейнеры, а также тома, связанные с ними.

        docker-compose start

Docker-compose start — запускает остановленные контейнеры.

        docker-compose stop

Docker-compose stop — останавливает работу запущенных контейнеров без их удаления.

        docker-compose restart

Docker-compose restart — перезапускает контейнеры.

        docker-compose pull

Docker-compose pull — загружает последние версии образов для сервисов, описанных в файле docker-compose.yaml
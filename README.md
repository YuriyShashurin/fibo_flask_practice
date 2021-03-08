# fibo_flask_practice
## Веб-сервис, который возвращает числа Фибоначчи с использованием кэширование результатов в Redis.

#### Как запустить контейнеры в Docker

* склонировать этот репозиторий ```git clone https://github.com/YuriyShashurin/flask_fibo_practice.git```
* перейти в папку с ним ```cd flask_fibo_practice```
* Установить docker и docker-compose согласно вашей ОС согласно инструкциям.(Docker - https://docs.docker.com/get-docker/ Docker-Compose - https://docs.docker.com/compose/install/)
* Собрать образы командой в консоли```docker-compose build```
* Запустить образы командой в консоли```docker-compose up```


##### Страницы: 
* Приветственная страница http://127.0.0.1:8081/
* Страница, на которое возвращается k-ое число Фибоначчи http://127.0.0.1:8081/k - где k необходимо заменить на любое целое число.

При повторном запросе по тому же числу, результы вернуться из кэша. 

# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем путь Poetry в переменную окружения PATH
ENV PATH="/root/.local/bin:$PATH"

# Включаем виртуальное окружение Poetry
RUN poetry config virtualenvs.create true

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости с помощью Poetry
RUN poetry install

# Устанавливаем команду по умолчанию для контейнера
ENTRYPOINT ["poetry", "run"]

CMD ["bash"]
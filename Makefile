install: # установить зависимости проекта
	poetry install

brain-games: # запустить файл brain-games
	poetry run brain-games

build: # позволяет создать "собранную" версию проекта
	poetry build

publish: # для отладки публикации
	poetry publish --dry-run

package-install: # для установки пакета из операционной системы
	python3 -m pip install --user dist/*.whl
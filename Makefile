install: # установить зависимости проекта
	poetry install

brain-games: # запустить файл brain-games
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
brain-gcd:
	poetry run brain-gcd

build: # позволяет создать "собранную" версию проекта
	poetry build

publish: # для отладки публикации
	poetry publish --dry-run

package-install: # для установки пакета из операционной системы
	python3 -m pip install --user dist/*.whl
package-reinstall:
	pip install --user --force-reinstall dist/*.whl
make lint:
	poetry run flake8 brain_games

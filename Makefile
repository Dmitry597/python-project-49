install: # установить зависимости проекта
	poetry install

brain-games: # запустить файл brain-games
	poetry run brain-games

brain-even: # запустить игру «Проверка на чётность»
	poetry run brain-even

brain-calc: # запустить игру «Калькулятор»
	poetry run brain-calc

brain-gcd: # запустить игру «Наибольший общий делитель (НОД)»
	poetry run brain-gcd

brain-progression: # запустить игру «Арифметическая прогрессия»
	poetry run brain-progression

build: # позволяет создать "собранную" версию проекта
	poetry build

publish: # для отладки публикации
	poetry publish --dry-run

package-install: # для установки пакета из операционной системы
	python3 -m pip install --user dist/*.whl

package-reinstall: # для переустановки пакета из операционной системы
	pip install --user --force-reinstall dist/*.whl

lint:   # для проверки линтера flake8
	poetry run flake8 brain_games

asciinema:
	asciinema rec

installation:
	poetry install
	poetry build
	poetry publish --dry-run
	pip install --user --force-reinstall dist/*.whl

migrations:
	python informe_cvr/manage.py makemigrations 
	python informe_cvr/manage.py migrate 

serve:
	python informe_cvr/manage.py runserver

admin:
	python informe_cvr/manage.py createsuperuser

test:
	rm -rf htmlcov .coverage
	coverage run --source informe_cvr informe_cvr/manage.py test -v 2 informe

coverage: test
	coverage report -m
	coverage html

index:
	python informe_cvr/manage.py rebuild_index --noinput

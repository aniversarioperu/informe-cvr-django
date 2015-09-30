migrations:
	python informe_cvr/manage.py makemigrations 
	python informe_cvr/manage.py migrate 

serve:
	python informe_cvr/manage.py runserver

admin:
	python informe_cvr/manage.py createsuperuser

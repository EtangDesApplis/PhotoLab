# TO INSTALL DEPENDENCIES
```
conda install -c anaconda django 
```

# TO BUILD

```
python manage.py migrate
python manage.py makemigrations PhotoLab
```

# TO RUN

```
python manage.py runserver 0:8080
```
Appilcation is accessible via web browser:
```
http://localhost:8080/
```
# TO USE IN DOCKER MODE
```
docker run -p 8080:8080 antoinenguyen31/photolab
```
# TO USE AS A FREE WEB SERVICE:
```
http://vps-1fd410ea.vps.ovh.net
```

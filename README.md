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
# TO ACCESS TO APPLICATION
 
Via web browser:
```
http://localhost:8080/
```
# TO USE IN DOCKER MODE
```
docker run -p 8080:8080 -v /tmp:/tmp antoinenguyen31/photolab:20200719
```

# Mediheart Backend 
This repository is the home for the backend of Mediheart App.

## Quick Start  
---
Clone this repo.
```
$ git clone {repo-link}  
```
Change your current directory.
``` 
$ cd mediheart-server
```

Run with docker.
```
$ docker-compose up 
```

## API Provided  
---
  

### Authentication API

|    URL       | Method |
|------------- |:------:|
| /login/      | POST   |   
| /logout/     | GET   |   
| /signup/     | POST   | 
| /deleteu/    | POST   |   
| /changepass/ | POST   | 
  
### Patients Management API

|    URL   | Method | Description | 
|-------------------------------|:------:| :-------: |  
| /personalInfo/<int:id>        | GET    | Get patient by ID
| /personalInfo/                | POST   | Add patient(s)  
| /personalInfo/                | PUT    | Modify patient information 
| /personalInfo/                | DELETE | Delete patients  
| /patients/                    | GET    | Get all patients in database
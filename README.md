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

Build and run with Docker (Docker installation required).

```
docker build -t mediheart-server .  
docker run -p 8000:8000 mediheart-server

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
| /api/personalInfo/<int:id>        | GET    | Get patient by ID
| /api//personalInfo/               | POST   | Add patient(s)  
| /api/personalInfo/                | PUT    | Modify patient information 
| /api/personalInfo/                | DELETE | Delete patients  
| /api/patients/                    | GET    | Get all patients in database
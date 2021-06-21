# Mediheart Backend 
This repository is the home for the backend of Mediheart App.

## Quick Start  
---

```
$ docker-compose up 
```

## API Provided  
---
  

### Authentication API

|    URL       | Method |
|------------- |:------:|
| /login/      | POST   |   
| /logout/     | POST   |   
| /signup/     | POST   | 
| /deleteu/    | POST   |   
| /changepass/ | POST   | 
  
### Patients Management API

|    URL   | Method |
|----------|:------:|
| /personalInfo/<int:id>        | POST   |
| /personalInfo/modify/<int:id> | POST   |   
| /patients/ | POST   | 
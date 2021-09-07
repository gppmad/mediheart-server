from api.models.patients import Patients

def count_patients(user_id):
    return Patients.objects.filter(fk_user_id=user_id).count() > 0
        

print(count_patients(69))
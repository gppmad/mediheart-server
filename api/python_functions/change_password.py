
from django.db.models.expressions import F
from api.models.patients import Patients as Patients


def change_pass():
    patients_table = list(Patients.objects.all().values("firstname","lastname","birthDate","gender", patientId=F("id"), userId=F("fk_user")  ) )
    print("patients retrivied")


change_pass()
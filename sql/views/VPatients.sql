SELECT id,
       firstname,
       lastname,
       birthDate,
       gender,
       [api.bloodType].id,
       [api.bloodtype].bloodType
FROM [api.patients]
INNER JOIN [api.bloodtype] ON [api.patients].bloodType_id=[api.bloodtype].id
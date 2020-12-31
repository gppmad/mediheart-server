SELECT id,
       firstname,
       lastname,
       birthDate,
       gender,
       [api_bloodtype].id,
       [api_bloodtype].bloodType
FROM [api_patients]
INNER JOIN [api_bloodtype] ON [api_patients].bloodType_id=[api_bloodtype].id
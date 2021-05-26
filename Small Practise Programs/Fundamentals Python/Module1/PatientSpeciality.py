# lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    p = 0
    o = 0
    e = 0
    speciality = ""
    for i in range(0, len(patient_medical_speciality_list)):
        if i % 2 != 0:
            if patient_medical_speciality_list[i] == "P":
                p += 1
            elif patient_medical_speciality_list[i] == "O":
                o += 1
            elif patient_medical_speciality_list[i] == "E":
                e += 1
    if p > o:
        if p > e:
            speciality = medical_speciality["P"]
        else:
            speciality = medical_speciality["E"]
    elif o > e:
        speciality = medical_speciality["O"]
    else:
        speciality = medical_speciality["E"]

    return speciality


# provide different values in the list and test your program
patient_medical_speciality_list = [301, 'P', 302, 'P', 305, 'P', 401, 'E', 656, 'E']
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(patient_medical_speciality_list, medical_speciality)
print(speciality)
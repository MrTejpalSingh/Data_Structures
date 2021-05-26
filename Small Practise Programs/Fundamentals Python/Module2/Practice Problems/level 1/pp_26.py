# lex_auth_0127136253311385601197

def check_occurence(string):
    mat_ls = ["MAT","MAt","Mat","mat","maT","mAT","MaT","mAt"]
    jet_ls = ["JET", "JEt", "Jet", "jet", "jeT", "jET", "JeT", "jEt"]
    mat_c = 0
    jet_c = 0
    lst = string.split(" ")
    for i in lst:
        if i in mat_ls:
            mat_c += 1
    for i in lst:
        if i in jet_ls:
            jet_c += 1

    if jet_c == mat_c:
        return True
    else:
        return False

string = "Mat is old buy a new mat and come to jet"
print(check_occurence(string))
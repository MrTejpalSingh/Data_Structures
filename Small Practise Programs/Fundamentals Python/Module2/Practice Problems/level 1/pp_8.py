# lex_auth_0127135929511936001157

def calculate_net_amount(trans_list):
    wid = 0
    dip = 0
    for i in range(len(trans_list)):
        str_trans = trans_list[i].split(":")
        if str_trans[0] == "D":
            dip = dip + int(str_trans[1])
        else:
            wid = wid + int(str_trans[1])
    net_amount = dip - wid
    return net_amount


trans_list = ["D:350", "W:100", "W:500", "D:1000"]
print(calculate_net_amount(trans_list))
# lex_auth_0127135869481369601150

def list123(nums):
    flg = 0
    for i in range(len(nums)-1):
        if nums[i] == 1:
            for j in range(i + 1, len(nums)):
                if nums[j] == 2:
                    for k in range(j + 1, len(nums)):
                        if nums[k] == 3:
                            flg = 1
    if flg == 0:
        return False
    else:
        return True


nums = [100,2000,1,2,3,300]
print(list123(nums))
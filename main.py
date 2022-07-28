ans = 0

for j in range(10 ** 2):
    string = str(j)

    desired_array = [int(i) for i in string]
    print('ds', desired_array)

    new_array = desired_array

    desired_array.sort()

    if new_array == desired_array:
        ans += 1
        print(desired_array)

print('answer', ans)


def total_inc_dec(x):
    #     ans = 0
    #     for j in range(10 ** x):
    #         s = list(str(j))
    #         if ( all(s[i] <= s[i + 1] for i in range(len(s) - 1)) or
    #              all(s[i] >= s[i + 1] for i in range(len(s) - 1)) ):
    #             ans += 1

    ans = 0

    for j in range(10 ** x):
        string = list(str(j))
        desired_string = [int(j) for j in list(string)]
        if desired_string == j:
            ans += 1

    return ans

# CODEWARS    ---Total increasing or decreasing numbers up to a power of 10---

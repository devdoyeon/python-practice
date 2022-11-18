def DashInsert(string):
    result = []
    li = list(map(int, string))
    for idx, num in enumerate(li):
        result.append(str(num))
        if idx < len(li) - 1:
            is_odd = num % 2 == 1
            is_next_odd = li[idx + 1] % 2 == 1
            if is_odd and is_next_odd:
                result.append("-")
            elif not is_odd and not is_next_odd:
                result.append("*")
    print("".join(result))

DashInsert("4546793")
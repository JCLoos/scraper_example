global results
global i
results = "22213211321"
i = 0


def checksite(search_criteria):
    global results
    global i
    result = results[i]
    i += 1
    # 1 = data good for downloading
    # 2 = too much data: make search criteria better
    # 3 = no data
    print(f"checksite result = {result}")
    return int(result)


def increment_last_pos(index):
    last_pos = index[-1]
    index = index[:-1]
    index.append(last_pos + 1)
    return index


def add_new_pos(iundex):
    last_pos = index[-1]
    index.append(last_pos)
    return index


def reduce_pos(index):
    index = index[:-1]
    last_pos = index[-1]
    index = index[:-1]
    index.append(last_pos + 1)
    return index


def get_search(index):
    # chars = "0123456789abcdefghijklmnopqrstuvxyz-!"
    chars = "abcdefghijklmnopqrstuvxyz-!"
    search = ""
    for pos in index:
        search += chars[pos]
    return search


index = [0]
for _ in range(10):
    print("-"*10)
    print(f"index = {index}")
    search = get_search(index)
    result = checksite(search)
    if result == 1:
        print(f"search criteria {search} is good: download the list")
        index = increment_last_pos(index)
        print(f"new index after inc last pos = {index}")
    elif result == 2:
        print(f"search criteria {search} is not good enough.")
        index = add_new_pos(index)
    elif result == 3:
        print(f"search criteria {search} has no data.")
        index = reduce_pos(index)

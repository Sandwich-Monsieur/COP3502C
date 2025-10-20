def reformat(data):
    result = {}
    for item in data:
        item_type = item["type"]
        name = item["name"]
        price = item["price"]
        
        if item_type not in result:
            result[item_type] = {}
        
        result[item_type][name] = price
    
    return result
    
def nth(data, n):
    if data is None:
        return None
    if n == 0:
        return data[0]
    return nth(data[1], n-1)

def where(data):
    if data == "Waldo":
        return 1
    elif type(data) == list:
        return sum(where(item) for item in data)
    elif type(data) == dict:
        return sum(where(key) + where(value) for key, value in data.items())
    else:
        return 0
def solution(cacheSize, cities):
    ans = 0
    buffer = []
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
            city = city.lower()
            if city in buffer:
                buffer.remove(city)
                buffer.append(city)
                ans += 1
            else:
                ans += 5
                if len(buffer) < cacheSize:
                    buffer.append(city)
                else:
                    buffer.pop(0)
                    buffer.append(city)
    return ans
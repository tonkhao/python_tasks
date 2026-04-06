logs = [
    "192.168.1.1 2023-10-01 10:00:00 200",
    "192.168.1.2 2023-10-01 10:05:00 404",
    "192.168.3.1 2023-10-01 10:10:00 500",
    "10.0.0.1 2023-10-01 10:15:00 200",
    "192.168.1.2 2023-10-01 10:20:00 200"
]

# получение айпишников
# первый классический вариант
def getIps(logs):
    ips = []
    for log in logs:
        ip = log.split()[0]
        ips.append(ip)
    return ips

# print(getIps(logs))

# получение айпишников
# современный более краткий вариант
def getIpsModern(logs):
    return [log.split()[0] for log in logs]

ips = getIpsModern(logs)
print(ips)

# получение уникальных айпишников
def getUniqueIps(ips):
    return set(ips)

uniqueIps = getUniqueIps(ips)
print(uniqueIps)

# словарь подсчета статусов
def getStatusCount(logs):
    result = dict()
    uniqueStatusesArr = [log.split()[3] for log in logs]
    for status in uniqueStatusesArr:
        result[status] = 0
    for log in logs:
        status = log.split()[3]
        result[status] += 1
    return  result

statusesDict = getStatusCount(logs)
print(statusesDict)

# самое раннее посещение
def getEarliestTime(logs):
    return min([log.split()[2] for log in logs])

# самое позднее посещение
def getLatestTime(logs):
    return max([log.split()[2] for log in logs])

earliestTime = getEarliestTime(logs)
latestTime = getLatestTime(logs)

print(earliestTime, latestTime)

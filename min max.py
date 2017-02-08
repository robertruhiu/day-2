def words(n):

    resultingDict = {}

    separated = n.split()

    if len(separated) == 1:
        resultingDict[separated[0]] = 1
        return resultingDict
    else:
        for item in separated:
            if item.isdigit():
                item = int(item)
            resultingDict[item] = separated.count(str(item))
        return resultingDict

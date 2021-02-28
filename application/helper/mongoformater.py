from application.config.autoload import *

def mongo_loads(document, field=[]):
    result = []
    for data in document:
        data_result = {}
        for item in data:
            if item == '_id':
                data_result[item] = str(data[item])
                continue
            data_result[item] = data[item]
        result.append(data_result)

    if field:
        print("masuk")
        result_field = []
        for i in field:
            for j in result:
                j_r = {}
                for k in j:
                    if i in k:
                        j_r[k] = j[k]
                result_field.append(j_r)
        return result_field
    return result


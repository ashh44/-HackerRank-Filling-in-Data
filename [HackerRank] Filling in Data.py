def to_float(value):
    try:
        return float(value)
    except ValueError:
        return None


def calcMissing(readings):
    data = [{'index': i, 'value': to_float(r.split('\t')[1])} for i, r in enumerate(readings)]

    for row in data:
        if row['value'] is None:
            left_not_none = next((r for r in data[:row['index']][::-1] if r['value'] is not None), None)
            right_not_none = next((r for r in data[row['index'] + 1:] if r['value'] is not None), None)
            if left_not_none is None:
                print(right_not_none['value'])
            elif right_not_none is None:
                print(left_not_none['value'])
            else:
                diff_index = right_not_none['index'] - left_not_none['index']
                diff_value = right_not_none['value'] - left_not_none['value']
                print(left_not_none['value'] + diff_value / diff_index)
import csv


def create_special_object(
        file_name,
        duration_gte=None,
        duration_gt=None,
        duration_lte=None,
        duration_lt=None
):

    with open(file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            id_str = row['id']
            dur = float(row['trip_duration'])
            need_to_return = False
            if duration_gte and dur >= duration_gte: need_to_return = True
            if duration_gt and dur > duration_gt: need_to_return = True
            if duration_lte and dur <= duration_lte: need_to_return = True
            if duration_lt and dur < duration_lt: need_to_return = True

            if need_to_return: yield tuple([id_str, dur])


data = create_special_object('submission.csv', duration_gte=1000)

for i in data:
    print(i)

import csv
import os
import time

blog_posts_file = "sample_data.csv"
blog_posts = ["id", "title", "message"]


def read_from_file(file=blog_posts, id=None):
    list_of_data = []
    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            data = dict(row)
            if id is not None and row["id"] == id:
                return data
            list_of_data.append(data)
        return list_of_data


def write_to_file(message, file=blog_posts_file, is_new=True):
    old_message = read_from_file(file)
    if file == blog_posts_file:
        header = blog_posts

    with open(file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()

        for row in old_message:
            if not is_new:
                if message["id"] == row["id"]:
                    row = message
            writer.writerow(row)
        if is_new:
            writer.writerow(message)


def generate_id(file=blog_posts_file):
    list_of_posts = read_from_file(file)
    if len(list_of_posts) == 0:
        new_id = '1'
        return new_id
    max_id = 0
    for row in list_of_posts:
        if int(row[id]) > max_id:
            max_id = int(row[id])
    new_id = str(max_id+1)
    return new_id


def collect_data(recive_data, header=blog_posts):
    if header == blog_posts:
        file = blog_posts_file
    message = {key:'' for key in header}
    for key in recive_data:
        message[key] = recive_data[key]
        message['id'] = generate_id(file)
    return message

def overwrite_old_post(new_data, file=blog_posts_file):


    if file == blog_posts_file:
        header = blog_posts

    with open(file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()

        for row in new_data:
            writer.writerow(row)


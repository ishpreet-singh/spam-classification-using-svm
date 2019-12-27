import os
import csv
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
dataset_path = os.path.join(dir_path, "dataset/enron1/")

def read_dataset():
    ham_emails_path = os.path.join(dataset_path, "ham/")
    spam_emails_path = os.path.join(dataset_path, "spam/")
    ham_emails = []
    spam_emails = []

    for email in os.listdir(ham_emails_path):
        email_content = ""
        email_name = os.path.join(ham_emails_path, email) 
        with open(email_name, 'r') as f:
            email_content = f.read()
        dic = { 'name' : email, 'content' : email_content, 'type': "ham" }
        ham_emails.append(dic)

    for email in os.listdir(spam_emails_path):
        email_content = ""
        email_name = os.path.join(spam_emails_path, email) 
        with open(email_name, 'r', errors='ignore') as f:
            email_content = f.read()
        dic = { 'name' : email, 'content' : email_content, 'type': "spam" }
        spam_emails.append(dic)

    emails = ham_emails + spam_emails

    random.shuffle(emails)

    keys = emails[0].keys()
    with open('dataset.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(emails)

def main():
    print("Reading main")
    read_dataset()

if __name__ == "__main__":
    main()
import json
import pickle

with open("contributors_sample.json", "r") as f:
    contributors_list = json.load(f)

jobs_dict = {}
for worker in contributors_list:
    for job in worker["jobs"]:
        if job not in jobs_dict:
            jobs_dict[job] = []
        jobs_dict[job].append(worker["username"])

with open("job_people.pickle", "wb") as f:
    pickle.dump(jobs_dict, f)

with open("job_people.json", "w") as f:
    json.dump(jobs_dict, f, indent=4)

#сравнение размеров
import os

pickle_size = os.path.getsize("job_people.pickle")
json_size = os.path.getsize("job_people.json")

print(f"Размер файла pickle - {pickle_size} байт")
print(f"Размер файла JSON - {json_size} байт")

# with open("job_people.json", "r") as f:
#     data = json.load(f)
# print(data)
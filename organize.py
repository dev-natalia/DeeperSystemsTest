import json

def organize(messed_list):
    priorited_list = []
    for project in messed_list:
        if not priorited_list:
            priorited_list.append(project)
        else:
            control = False
            for i in range(len(priorited_list)):
                if project["priority"] <= priorited_list[i]["priority"]:
                    priorited_list.insert(i, project)
                    control = True
                    break
            if control is False:
                priorited_list.append(project)

    manager_dict = {}
    watchers_dict = {}
    for project in priorited_list:
        for manager in project["managers"]:
            if manager not in manager_dict:
                manager_dict[manager] = []
                manager_dict[manager].append(project["name"])
            else:
                manager_dict[manager].append(project["name"])
        for watchers in project["watchers"]:
            if watchers not in watchers_dict:
                watchers_dict[watchers] = []
                watchers_dict[watchers].append(project["name"])
            else:
                watchers_dict[watchers].append(project["name"])

    with open('managers.json', 'w') as file_managers:
        json.dump(manager_dict, file_managers)

    with open('watchers.json', 'w') as file_watchers:
        json.dump(watchers_dict, file_watchers)

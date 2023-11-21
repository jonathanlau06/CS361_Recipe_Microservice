import json


json_file = open("recipes_raw_nosource_epi.json", "r")
recipes = json.load(json_file)


while True:
    ready_file = open("ready.txt", "r+")
    ready_text = ready_file.read()
    if ready_text == "ready":
        ready_file.seek(0)
        ready_file.truncate()
        ready_file.write("standby")
        ready_file.close()
        service_file = open("recipe_service.txt", "r+")
        service_text = service_file.readlines()
        # Search using name
        if service_text[0] == "1\n":
            service_file.seek(0)
            service_file.truncate()
            found = False
            num_found = 0
            for i in recipes:
                title = recipes[i]["title"]
                if num_found == 10:
                    break
                if service_text[1].lower() in title.lower():
                    found = True
                    num_found += 1
                    service_file.write(str(num_found) + "\n")
                    service_file.write(recipes[i]["title"] + "\n")
                    service_file.write(str(recipes[i]["ingredients"]) + "\n")
                    service_file.write(recipes[i]["instructions"] + "\n")
            if found is False:
                service_file.write("Recipe Not Found")
            service_file.close()
        # Search using ingredient(s)
        elif service_text[0] == "2\n":
            service_file.seek(0)
            service_file.truncate()
            service_text.pop(0)
            service_text = [i.strip().lower() for i in service_text]
            found = False
            num_found = 0
            for i in recipes:
                ingredients = recipes[i]["ingredients"]
                remainder = len(service_text)
                used_ingredient = []
                used_recipe = []
                if num_found == 10:
                    break
                for j in service_text:
                    if num_found == 10:
                        break
                    for k in recipes[i]["ingredients"]:
                        if j in k.lower():
                            if j not in used_ingredient:
                                used_ingredient.append(j)
                                remainder -= 1
                            if remainder == 0 and recipes[i]["title"] not in used_recipe:
                                found = True
                                num_found += 1
                                service_file.write(str(num_found) + "\n")
                                service_file.write(recipes[i]["title"] + "\n")
                                used_recipe.append(recipes[i]["title"])
                                service_file.write(str(recipes[i]["ingredients"]) + "\n")
                                service_file.write(recipes[i]["instructions"] + "\n")
                            if num_found == 10:
                                break
            if found is False:
                service_file.write("Recipe Not Found")
            service_file.close()


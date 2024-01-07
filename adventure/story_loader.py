import json


def load(filepath):
    with open(filepath, 'r') as file:
        story = json.load(file)
    with open(filepath, 'w') as file:
        json.dump(story, file, indent=4)
    return story

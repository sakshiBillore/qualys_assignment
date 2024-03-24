import os
import time
import yaml

PARENT_DIR = "tasks"


# This function will create yaml files based on the data
def generate_yaml_file(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)


# This function will prepare data for yaml file generation
def generate_yaml_files(dir_name, duration=60, interval=5):
    iterations = duration // interval
    task_path = os.path.join(PARENT_DIR, dir_name)
    for i in range(iterations):
        data = {
            'iteration': i + 1,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
        }
        os.makedirs(task_path, exist_ok=True)
        file_name = os.path.join(task_path, f"output_{i + 1}.yaml")
        generate_yaml_file(file_name, data)
        print(f"Generated {file_name}")
        time.sleep(interval)


# This function returns the data of generated yaml files
def get_yaml_data(dir_name):
    dir_name = os.path.join(PARENT_DIR, dir_name)
    yaml_data = []
    for file_name in os.listdir(dir_name):
        if file_name.endswith('.yaml'):
            file_path = os.path.join(dir_name, file_name)
            with open(file_path, 'r') as file:
                data = yaml.load(file, Loader=yaml.FullLoader)
                yaml_data.append({
                    'iteration': data['iteration'],
                    'timestamp': data['timestamp'],
                    'filename': file_path
                })
    yaml_data.sort(key=lambda x: int(x['iteration']))
    return yaml_data


if __name__ == "__main__":
    generate_yaml_files()

from flask import Flask, abort, render_template
import uuid
import threading
import generate_yaml

app = Flask(__name__)

# Dictionary to store tasks and their statuses
# TODO: instead of keeping tasks in memory, we can create a task DB
tasks = {}


# run_task will generate yaml file in separate thread and will set the task
# status to complete once the yaml files generation is successfull
def run_task(task_id):
    generate_yaml.generate_yaml_files(task_id)
    tasks[task_id] = 'completed'


# handle_root will propmts the button to initiate a task
@app.route('/', methods=['GET'])
def handle_root():
    return render_template('index.html')


# POST API to create task
@app.route('/tasks', methods=['POST'])
def handle_task():
    # Generate a unique task ID
    task_id = str(uuid.uuid4())

    # Start a new thread to run the task
    task_thread = threading.Thread(target=run_task, args=(task_id,))
    task_thread.start()

    # Store the task ID and its status
    tasks[task_id] = 'running'
    return render_template('task.html', status='running', task_id=task_id)


# GET task API
@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    # Check if the task ID exists
    if task_id not in tasks:
        abort(404)
    status = tasks[task_id]
    if status == 'running':
        return render_template('task.html', status=status, task_id=task_id)
    elif status == 'completed':
        tabular_data = generate_yaml.get_yaml_data(task_id)
        return render_template('task.html', status=status, task_id=task_id,
                               tabular_data=tabular_data)


if __name__ == '__main__':
    app.run(debug=True)

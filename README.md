
# Flask project template

`QUALYS Assignment` contains a working example of a Flask project with features:

- Ability to create yaml files for the span of one minute with five second intervals
- Poll Tasks
- Generates report having ymal file name, timestamp, iterations in tabular format

## How to start

```sh
$ mkdir qualys_assignment
$ cd qualys_assignment
$ git clone https://github.com/sakshiBillore/qualys_assignment.git .
$ python3 -m venv env
$ pip install -r requirements.txt
$ python app.py
```

Open http://127.0.0.1:5000/.

## Steps taken to create the project
- Created a VM(Ubuntu) via virtual box
- Installed VS Code on host machine and connected to VM via SSH
- Created a flask application with three endpoints 
  - / (Takes to index.html which will have a form to generate task)
  - /tasks (Creates a task and run the yaml generation script in seperate thread and returns a html page to poll tasks)
  - /tasks/<task_id> (Gets the status of the task and generate report when task is  completed)

## Screenshots of the pages is present in `qualys_assignments/screenshots`
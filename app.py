from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_limit = 10  # Set your desired task limit here

@app.route('/')
def index():
    enumerated_tasks = [(index, task) for index, task in enumerate(tasks)]
    task_count = len(tasks)
    return render_template('index.html', enumerated_tasks=enumerated_tasks, task_limit=task_limit, task_count=task_count)


@app.route('/add_task', methods=['POST'])
def add_task():
    if len(tasks) < task_limit:
        task = request.form.get('task')
        if task:
            tasks.append(task)
    return redirect(url_for('index'))

@app.route('/remove_task/<int:task_index>')
def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

@app.route('/edit_task/<int:task_index>')
def edit_task(task_index):
    if 0 <= task_index < len(tasks):
        task_to_edit = tasks[task_index]
        return render_template('edit_task.html', task_to_edit=task_to_edit, task_index=task_index)

@app.route('/update_task/<int:task_index>', methods=['POST'])
def update_task(task_index):
    if 0 <= task_index < len(tasks):
        new_task = request.form.get('new_task')
        tasks[task_index] = new_task
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

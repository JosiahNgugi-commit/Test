from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

tasks = []

@app.route('/')
def task_list():
    return render_template('task_list.html', tasks=tasks)

@app.route('/task/new', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        title = request.form['title']
        due_date = request.form['due_date']
        priority = request.form['priority']
        task = {'title': title, 'due_date': due_date, 'priority': priority}
        tasks.append(task)
        return redirect(url_for('task_list'))
    return render_template('task_form.html', action='Add')

@app.route('/task/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    task = tasks[index]
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['due_date'] = request.form['due_date']
        task['priority'] = request.form['priority']
        return redirect(url_for('task_list'))
    return render_template('task_form.html', action='Edit', task=task)

@app.route('/task/delete/<int:index>')
def delete_task(index):
    del tasks[index]
    return redirect(url_for('task_list'))

if __name__ == '__main__':
    app.run(debug=True)


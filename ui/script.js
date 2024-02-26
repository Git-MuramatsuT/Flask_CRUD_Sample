document.addEventListener("DOMContentLoaded", fetchTodos());

async function fetchTodos() {
    const todos = await fetch("http://localhost:5000/todos");
    if(!todos.ok) {
        throw new Error("Could not fetch todos");
    }
    const todosJson = await todos.json();
    console.log(todosJson)
    renderTodos(todosJson)
}

function renderTodos(todosJson) { 
    const todoDiv = document.getElementById("todo-list");
    if (!todoDiv) {
        throw new Error("Could not find todoList element");
    }
    todoDiv.innerHTML = "";
    const todoTable = document.createElement("table");
    todoTable.innerHTML = `
    <th>ID</th>
    <th>task</th>
    <th>deadline</th>
    `
    todosJson.todos.forEach(todo => {
        todoTable.innerHTML += `
        <tr>
            <td>${todo.id}</td>
            <td>${todo.task}</td>
            <td>${todo.deadline}</td>
            <td>
                <button onclick="renderTodo(${todo.id})">Edit</button>
            </td>
        </tr>
        `;
    });
    todoDiv.appendChild(todoTable);
}

async function handleRegisterTodo(event) {
    event.preventDefault();
    const form = event.target.form;
    const formData = new FormData(form);
    const todo = {
        task: formData.get("task"),
        deadline: formData.get("deadline")
    }

    const response = await fetch("http://localhost:5000/todos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(todo)
    });
    if (!response.ok) {
        const error = await response.json();
        console.error(error);
        return;
    }
    // fetchTodos();
}

async function fetchTodo(id) {
    const response = await fetch(`http://localhost:5000/todos/${id}`);
    if (!response.ok) {
        throw new Error("Could not fetch order");
    }
    return await response.json();
}

async function renderTodo(id) {
    const todo = await fetchTodo(id);
    const todoDiv = document.getElementById("order-modal-component");
    todoDiv.innerHTML = `
    <form>
        <div> ID: ${todo.id}</div>
        <label for="task">task:</label>
        <input type="text" name="task" value=${todo.task}></input>
        <label for="deadline">deadline:</label>
        <input type="date" name="deadline" value=${todo.deadline}></input>
        <button type="submit" onclick="handleUpdateTodo(event, ${todo.id})">Update</button>
    </form>
    `;
    document.getElementById("myModal").style.display = "block";
}


async function handleUpdateTodo(event, id) {
    event.preventDefault();
    const form = event.target.form;
    const formData = new FormData(form);
    const todo = {
        task: formData.get("task"),
        deadline: formData.get("deadline")
    };

    const response = await fetch(`http://localhost:5000/todos/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(todo)
    });

    if (!response.ok) {
        const result = await response.json();
        throw new Error(result.message);
    } else {
        document.getElementById("myModal").style.display = "none";
    }
}
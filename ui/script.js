document.addEventListener("DOMContentLoaded", fetchTodos());

async function fetchTodos() {
    const todos = await fetch("http://localhost:5000/todos");
    if(!todos.ok) {
        throw new Error("Could not fetch todos");
    }
    const todosJson = await todos.json();
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
    `
    todosJson.todos.forEach(todo => {
        todoTable.innerHTML += `
        <tr>
            <td>${todo.id}</td>
            <td>${todo.task}</td>
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
        task: formData.get("task")
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
    fetchTodos();
}
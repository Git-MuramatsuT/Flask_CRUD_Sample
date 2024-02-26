async function fetchTodos() {
    const todos = await fetch("http://localhost:5000/todos");
    if(!todos.ok) {
        throw new Error("Could not fetch todos");
    }
    const todosJson = await todos.json();
    renderTodos(todosJson)
}

function renderTodos(todosJson) { 
    console.log(todosJson)
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
        </tr>
        `;
    });
    todoDiv.appendChild(todoTable);
}
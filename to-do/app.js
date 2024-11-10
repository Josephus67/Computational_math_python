const listInput = document.getElementById('todo-input');
const addButton = document.getElementById('add-todo');
const todoList = document.getElementById('todo-list');

addButton.addEventListener('click',function(e) {
  const todoText = listInput.value.trim();
  
  if (todoText.length < 1) {
    alert('Please enter a valid todo item.');
    return;
  }
  
  const listItem = document.createElement('li');
  listItem.textContent = todoText;


  todoList.appendChild(listItem);

  const doneButton = document.createElement('button');

  listInput.value = '';
});

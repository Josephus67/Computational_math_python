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
  doneButton.textContent = 'Done';
  doneButton.classList.add('done-button');

  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'Delete';
  deleteButton.classList.add('delete-button');

  listItem.appendChild(doneButton);
  listItem.appendChild(deleteButton);

  listInput.value = '';
});

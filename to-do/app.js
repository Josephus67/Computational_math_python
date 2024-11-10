const listInput = document.getElementById('todo-input');
const addButton = document.getElementById('add-todo');
const todoList = document.getElementById('todoList');

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
  saveData();
});


todoList.addEventListener('click', function(event) {
  const target = event.target;
  const listItem = target.parentNode

  if (target.classList.contains('done-button')) {
    listItem.classList.toggle('completed');
  } 
  else if (target.classList.contains('delete-button')) {
    listItem.remove();
  }
  saveData();
});

function saveData(){
  localStorage.setItem('data', todoList.innerHTML); 
}
function showTask(){
  app.innerHTML= localStorage.getItem('data');
}
showTask();
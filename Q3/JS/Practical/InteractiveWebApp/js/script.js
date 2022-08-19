// Add a new item to the list

// Get form element and store in variable
const formElement = document.querySelector("form");

// Get existing list element
let existingList = document.querySelector("#to-do-list");

// Listen for the "submit" event on the button
formElement.addEventListener("submit", (event) => {
	// Stop page from reloading
	event.preventDefault();

	// Get value from form input field, pass to function
	let newItemText = formElement.querySelector("#input-txt").value;
	let newListElement = createNewElement(newItemText);

	// Append new element to existing list
	existingList.appendChild(newListElement);
});

//  Create a new element to append to the list, complete with
//  edit and delete buttons. Returns an `HTMLLIElement` object.
function createNewElement(newItemText) {
	// Create list element to add to; set class
	let newListElement = document.createElement("li");
	newListElement.classList.add("todo");

	// Create item div; set class
	let newItemDiv = document.createElement("div");
	newItemDiv.classList.add("todo-item");

	// Set text of new list div from input
	newItemDiv.innerText = newItemText;

	// Create edit button, set text and class
	let editButton = document.createElement("button");
	editButton.innerText = "Edit";
	editButton.classList.add("edit-btn");

	// Create delete button, set text and class
	let deleteButton = document.createElement("button");
	deleteButton.innerText = "Delete";
	deleteButton.classList.add("del-btn");

	// Append item div and edit & delete buttons to overall list element
	newListElement.appendChild(newItemDiv);
	newListElement.appendChild(editButton);
	newListElement.appendChild(deleteButton);

	return newListElement;
}

// Listen for a click on any of the "delete" buttons
const deleteButtons = document.querySelectorAll("del-btn");
deleteButtons.addEventListener("click", (event) => {
	console.log(event.target);
});

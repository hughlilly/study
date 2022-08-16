// Get form element and store in variable
const formElement = document.querySelector("form");

formElement.addEventListener("submit", (event) => {
	// Stop page from reloading
	event.preventDefault();

	// Get value from form input field
	let newItemText = formElement.querySelector("#input-txt").value;

	// Create element to add to list
	let newListElement = document.createElement("li");

	// Set text of new element from form
	newListElement.innerText = newItemText;

	// Get existing list element
	let existingList = document.getElementById("to-do-list");

	// Append new element to existing list
	existingList.appendChild(newListElement);
});

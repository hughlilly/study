function handle(event) {
	event.preventDefault();
	alert("Enter!");
}

function addItemToList(inputText) {
	// Create element, and add "todo" class to it
	let newItemElement = document.createElement("li");
	newItemElement.classList.add("todo");

	// Set content to input text from form
	newItemElement.innerText = inputText;

	// Get existing list element, and append new element to it
	let existingList = document.getElementById("to-do-list");
	existingList.append(newItemElement);
}

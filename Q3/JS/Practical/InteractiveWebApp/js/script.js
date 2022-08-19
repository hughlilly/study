// A: Add a new item to the list

// Get form element
const formElement = document.querySelector("form");

// Listen for the "submit" event on the button
formElement.addEventListener("submit", (event) => {
	// Stop page from reloading
	event.preventDefault();

	// Get value from form input field
	let newItemText = formElement.querySelector("#input-txt").value;

	// If not blank, continue with adding process
	if (newItemText != "") {
		// Pass input text to function and store result in variable
		let newListElement = createNewElement(newItemText);

		// Append new element to existing list
		existingList.appendChild(newListElement);

		// Reset value
		formElement.querySelector("#input-txt").value = "";
	}
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

// B: Delete and update list items

// Get existing list element
const existingList = document.querySelector("#to-do-list");

// Listen for clicks on the list
existingList.addEventListener("click", (event) => {
	// If Edit button clicked, run edit function
	if (event.target.classList.contains("edit-btn")) {
		console.log("Editing…");
	}
	// Else, if Delete button clicked, print info to console and remove item
	else if (event.target.classList.contains("del-btn")) {
		const innerText =
			event.target.parentNode.querySelector(".todo-item").innerText;
		// const innerText = event.currentTarget.firstElementChild.firstElementChild.innerText;
		console.log(`Deleting item "${innerText}"…`);
		event.target.parentNode.remove();
	}
});

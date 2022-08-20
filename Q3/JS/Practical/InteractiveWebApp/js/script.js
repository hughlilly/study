// A: Add a new item to the list

// Get form element
const formElement = document.querySelector("form");

// Get existing list element
const existingList = document.querySelector("#to-do-list");

if (existingList.childNodes.length === 0) {
	const placeholderText = document.createElement("div");
	placeholderText.classList.add("no-items-placeholder");
	placeholderText.innerText = "No items";
	existingList.appendChild(placeholderText);
}

placeholderElement = existingList.querySelector(".no-items-placeholder");

// Listen for the "submit" event on the button
formElement.addEventListener("submit", (event) => {
	// Stop page from reloading
	event.preventDefault();

	// If placeholder span is there, hide it
	if (placeholderElement) placeholderElement.hidden = true;

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
	editButton.innerText = "✏️";
	editButton.classList.add("edit-btn");

	// Create delete button, set text and class
	let deleteButton = document.createElement("button");
	deleteButton.innerText = "🗑";
	deleteButton.classList.add("del-btn");

	// Append item div and edit & delete buttons to overall list element
	newListElement.appendChild(newItemDiv);
	newListElement.appendChild(editButton);
	newListElement.appendChild(deleteButton);

	return newListElement;
}

// B: Delete and update list items

// Listen for clicks on the list
existingList.addEventListener("click", (event) => {
	// If Edit button clicked, run edit function
	if (event.target.classList.contains("edit-btn")) {
		editItem(event);
	}
	// Else, if Delete button clicked, print info to console and remove item
	else if (event.target.classList.contains("del-btn")) {
		const innerText =
			event.target.parentNode.querySelector(".todo-item").innerText;
		let time = new Date();
		time = time.toLocaleTimeString();
		console.info(`"${innerText}" was deleted at ${time}`);
		event.target.parentNode.remove();

		// If `childElementCount` is 1, presume this is the placeholder div, and unhide it
		if (existingList.childElementCount === 1)
			placeholderElement.removeAttribute("hidden");
	}
});

function editItem(event) {
	const listItem = event.target.parentNode;

	// Get edit and delete buttons
	const delButton = listItem.querySelector(".del-btn");
	const editButton = listItem.querySelector(".edit-btn");

	// Create Save button
	const saveButton = document.createElement("button");
	saveButton.innerText = "✔️";
	saveButton.classList.add("save-btn");

	// Create Cancel button
	const cancelButton = document.createElement("button");
	cancelButton.innerText = "❌";
	cancelButton.classList.add("cancel-btn");

	// Insert new buttons before edit button
	editButton.insertAdjacentElement("beforebegin", saveButton);
	editButton.insertAdjacentElement("beforebegin", cancelButton);
	// editButton.insertBefore(saveButton, cancelButton);

	// Hide delete and edit buttons
	delButton.hidden = true;
	editButton.hidden = true;

	// Get item and text
	const itemDiv = listItem.querySelector(".todo-item");
	const innerText = itemDiv.innerText;

	// Create input element for editing
	const editInput = document.createElement("input");
	editInput.classList.add("edit-input");
	editInput.value = innerText;

	// Replace existing div with new input field
	itemDiv.replaceWith(editInput);
	editInput.focus();
	editInput.select();

	// If enter is pressed inside editInput, save item
	editInput.addEventListener("keypress", function (event) {
		if (event.key === "Enter") {
			saveItem();
		}
	});

	// If Cancel is pressed
	cancelButton.addEventListener("click", function () {
		// Reset delete and edit button state
		delButton.removeAttribute("hidden");
		editButton.removeAttribute("hidden");

		// Restore div
		editInput.replaceWith(itemDiv);

		// Remove Save button and self
		saveButton.remove();
		this.remove();
	});

	// If Save is pressed
	saveButton.addEventListener("click", function () {
		saveItem();
	});

	function saveItem() {
		let newText = editInput.value;
		let oldText = itemDiv.innerText;
		let time = new Date();
		time = time.toLocaleTimeString();
		console.log(`"${oldText}" set to "${newText}" at ${time}`);
		// set itemDiv value to inputElementEdit value
		itemDiv.innerText = editInput.value;

		// Reset delete and edit button state
		delButton.removeAttribute("hidden");
		editButton.removeAttribute("hidden");

		// Restore div
		editInput.replaceWith(itemDiv);

		// Remove Cancel button and self
		cancelButton.remove();
		saveButton.remove();
	}
}

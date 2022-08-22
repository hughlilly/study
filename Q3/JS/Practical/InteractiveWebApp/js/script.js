// A: Add a new item to the list

// Get form element
const formElement = document.querySelector("form");

// Get existing list element
const existingList = document.querySelector("#to-do-list");

// If list is blank, inject placeholder div
if (existingList.childNodes.length === 0) {
	const placeholderText = document.createElement("div");
	placeholderText.classList.add("no-items-placeholder");
	placeholderText.innerText = "No items";
	existingList.appendChild(placeholderText);
}

// Store placeholder element in a variable so it can be hidden and unhidden
placeholderElement = existingList.querySelector(".no-items-placeholder");

// Store message area element so it can be updated
const messageArea = document.querySelector("#message-area");

// Listen for the "submit" event on the form
formElement.addEventListener("submit", (event) => {
	// Stop page from reloading
	event.preventDefault()

	// Store input element in variable so it can be queried
	const inputField = formElement.querySelector("#input-txt");

	// Get value from form input field, trim it
	let newItemText = inputField.value.trim();

	// If not blank, continue
	if (newItemText !== "") {
		// Hide placeholder
		placeholderElement.hidden = true;

		// Pass input text to function and store result in variable
		let newListElement = createNewElement(newItemText);

		// Append new element to existing list
		existingList.appendChild(newListElement);
	} else if (newItemText === "") {
		// If blank, set to warning, fadeout, and update text
		messageArea.classList.add("warning", "fadeout");
		messageArea.innerText = "List items cannot be blank!";

		// After 3 seconds, clear inner text and remove fadeout class
		setTimeout(function () {
			messageArea.innerText = "";
			messageArea.classList.remove("fadeout");
		}, 2000);
	}
	// Reset value
	formElement.querySelector("#input-txt").value = "";
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
	const originalValue = itemDiv.innerText;

	// Create input element for editing
	const editInput = document.createElement("input");
	editInput.classList.add("edit-input");
	editInput.value = originalValue;

	// Replace existing div with new input field
	itemDiv.replaceWith(editInput);
	editInput.focus();
	editInput.select();

	// If enter is pressed inside editInput, save item; if "Esc", cancel
	editInput.addEventListener("keypress", function (event) {
		if (event.key === "Enter") {
			saveItem();
		} else if (event.key === "Escape") {
			// If value in editable field has been changed, log to console
			if (!editInput.value == originalValue)
				console.info(
					`Editing cancelled. New text would have been "${editInput.value}"`
				);
			cancelEditing();
		}
	});

	// If Save is pressed, run Save function
	saveButton.addEventListener("click", function () {
		saveItem();
	});

	// If Cancel is pressed, run Cancel function
	cancelButton.addEventListener("click", function () {
		// Reset delete and edit button state
		cancelEditing();
	});

	function saveItem() {
		let newText = editInput.value;
		let oldText = itemDiv.innerText;

		// Log to console as a way to track history before implementing Local Storage
		let time = new Date();
		time = time.toLocaleTimeString();
		console.log(`"${oldText}" set to "${newText}" at ${time}`);
		// set itemDiv value to inputElementEdit value
		itemDiv.innerText = editInput.value;

		// Run CancelEditing function because actions are the same from here on out
		cancelEditing();
	}

	function cancelEditing() {
		// Reset state of delete and edit buttons
		delButton.removeAttribute("hidden");
		editButton.removeAttribute("hidden");

		// Restore original div
		editInput.replaceWith(itemDiv);

		// Remove Save and Cancel buttons
		saveButton.remove();
		cancelButton.remove();
	}
}

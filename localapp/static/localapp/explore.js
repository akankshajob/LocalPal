function filterFacilities() {
    const searchInput = document.getElementById('search-bar').value.toLowerCase();
    const categoryFilter = document.getElementById('category-filter').value;
    const ratingFilter = document.getElementById('rating-filter').value;
    const facilities = document.querySelectorAll('.facility-card');

    facilities.forEach(facility => {
        const title = facility.querySelector('h3').textContent.toLowerCase();
        const category = facility.getAttribute('data-category');
        const rating = facility.getAttribute('data-rating');

        const matchesSearch = title.includes(searchInput);
        const matchesCategory = categoryFilter === 'all' || category === categoryFilter;
        const matchesRating = ratingFilter === 'all' || parseInt(rating) >= parseInt(ratingFilter);

        if (matchesSearch && matchesCategory && matchesRating) {
            facility.style.display = 'block';
        } else {
            facility.style.display = 'none';
        }
    });
}


// Add feedback to the facility
function addFeedback(button) {
    const feedbackSection = button.parentElement; // Get the parent feedback section
    const feedbackInput = feedbackSection.querySelector(".feedback-input");
    const feedbackList = feedbackSection.querySelector(".feedback-list");

    const feedbackText = feedbackInput.value.trim();
    if (feedbackText === "") {
        alert("Feedback cannot be empty!");
        return;
    }

    // Create a new feedback list item
    const feedbackItem = document.createElement("li");
    feedbackItem.textContent = feedbackText;

    // Append feedback to the list
    feedbackList.appendChild(feedbackItem);

    // Clear the input field
    feedbackInput.value = "";
}

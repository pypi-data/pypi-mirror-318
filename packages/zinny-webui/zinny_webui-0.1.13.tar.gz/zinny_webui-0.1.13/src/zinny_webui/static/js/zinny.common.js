
// Common and cross-component functions

const state = {
    title_id: null,
    survey_id: null,
    screen_type: null,
    ratings: {}, // Keyed by criterion name, e.g., { "acting_skill": "8" }
};

async function fetchAndApplyRatings() {
    const titleId = state.title_id || null;
    const surveyId = state.survey_id || null;

    if (!titleId || !surveyId) {
        // console.warn("Title or survey not selected. Skipping fetch and apply ratings.");
        state.ratings = {}; // Default to empty ratings
        return;
    }

    try {
        const ratingsResponse = await fetch(`/api/v1/ratings?title_id=${titleId}&survey_id=${surveyId}`);
        if (ratingsResponse.ok) {
            const existingRatings = await ratingsResponse.json();
            if (existingRatings == {}) {
                state.ratings = {}; // Default to empty ratings
                console.warn("No ratings found for this survey-title combination.");
            } else {
                if (existingRatings.screen_type_id) {
                    ScreenSelect.selectScreenTypeFromId(existingRatings.screen_type_id);
                }
                state.ratings = existingRatings.ratings || {};
            }
        } else {
            throw new Error(`Failed to fetch ratings: ${ratingsResponse.status}`);
        }
    } catch (error) {
        console.error("Error fetching ratings:", error);
        state.ratings = {}; // Default to empty ratings on error
    }
    // console.log("Ratings:", state.ratings);
}


document.addEventListener("resetCriteria", () => {
    console.log("WARNING: Criteria values reset not implemented yet");
});



document.addEventListener("DOMContentLoaded", () => {
    // Initialize Survey and Title Select
    SurveySelect.fetchAllSurveys();
    TitleSelect.searchTitles;
    TitleSelect.resetTitleSearch();
    SurveySelect.setupCriteriaInteraction();
    SurveySelect.setCriteriaEditable(false);
    ScreenSelect.setupScreenTypeSelector();

    // Initialize Save Button
    const saveButton = document.getElementById("save-ratings-button");
    saveButton.addEventListener("click", SurveySelect.saveSurveyResponses);

    // Initialize Survey Filters
    const filterOptions = document.getElementById("survey-filter-options");
    const filtersContainer = document.getElementById("survey-filters-container");

    // Add event listeners for expand and collapse
    filterOptions.addEventListener("show.bs.collapse", () => {
        // filtersContainer.style.display = "block"; // Show the parent container
        filtersContainer.classList.remove("d-none"); // Remove the d-none class
    });

    filterOptions.addEventListener("hidden.bs.collapse", () => {
        // filtersContainer.style.display = "none"; // Hide the parent container
        filtersContainer.classList.add("d-none"); // Remove the d-none class
    });

    // Initialize Tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach((tooltipTriggerEl) => {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });

});


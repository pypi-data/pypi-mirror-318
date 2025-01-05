let surveyFilters = {
    preset: null,
};

const SurveySelect = (function() {


    function createSurveyCard(survey) {
        const card = document.createElement("div");
        card.className = "card mb-2";
        card.onclick = () => selectSurvey(survey.id);

        const cardBody = document.createElement("div");
        cardBody.className = "card-body";

        const cardTitle = document.createElement("h5");
        cardTitle.className = "card-title";
        cardTitle.textContent = survey.name;

        const cardDescription = document.createElement("p");
        cardDescription.className = "card-text text-muted";
        cardDescription.textContent = survey.description;

        cardBody.appendChild(cardTitle);
        cardBody.appendChild(cardDescription);
        card.appendChild(cardBody);

        return card;
    }

    async function fetchAllSurveys() {
        const surveysList = document.getElementById("surveys-list");

        try {
            const response = await fetch("/api/v1/surveys/");
            if (!response.ok) {
                throw new Error("Failed to fetch surveys");
            }

            const surveys = await response.json();
            surveysList.innerHTML = ""; // Clear previous results

            surveys.forEach((survey) => {
                surveysList.appendChild(createSurveyCard(survey));
            });
        } catch (error) {
            console.error("Error fetching surveys:", error);
            surveysList.innerHTML = `
                <li class="list-group-item text-danger">Failed to load surveys. Please try again.</li>
            `;
        }
    }

    async function surveySearch() {
        const query = document.getElementById("survey-search-input").value.toLowerCase();
        const surveysList = document.getElementById("surveys-list");

        if (!query) {
            await fetchAllSurveys();
            return;
        }

        try {
            let apiUrl = `/api/v1/surveys/search?query=${encodeURIComponent(query)}`;
            if (surveyFilters.preset) {
                apiUrl += `&preset=${encodeURIComponent(surveyFilters.preset)}`;
            }

            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error("Failed to fetch surveys");
            }

            const results = (await response.json()).results || [];
            surveysList.innerHTML = ""; // Clear previous results

            if (results.length === 0) {
                surveysList.innerHTML = `
                    <li class="list-group-item">No surveys found.</li>
                `;
            } else {
                results.forEach((survey) => {
                    surveysList.appendChild(createSurveyCard(survey));
                });
            }
        } catch (error) {
            console.error("Error fetching surveys:", error);
            surveysList.innerHTML = `
                <li class="list-group-item text-danger">Failed to load surveys. Please try again.</li>
            `;
        }
    }


    async function selectSurvey(survey_id) {
        try {
            const surveyResponse = await fetch(`/api/v1/surveys/${survey_id}`);
            if (!surveyResponse.ok) {
                throw new Error("Failed to fetch survey details");
            }
    
            const surveyDetails = await surveyResponse.json();
            const criteria = JSON.parse(surveyDetails.criteria);
            const survey_name = surveyDetails.name;



            // Update state
            state.survey_id = survey_id;
            // update state ratings and screen_type with existing values
            await fetchAndApplyRatings();

            // Update the screen type selector from state
            await ScreenSelect.prefillScreenType();

            // Replace search bar with selected survey display
            const searchBar = document.getElementById("survey-input-group");
            searchBar.innerHTML = `
                <div class="form-control bg-light">${survey_name}</div>
                <button class="btn btn-secondary was-btn-outline" onclick="SurveySelect.resetSurveySearch()">
                    <i class="bi bi-pencil"></i>
                </button>
            `;
            searchBar.classList.add("survey-selected");
            // Clear search results and display criteria
            const surveysList = document.getElementById("surveys-list");
            surveysList.classList.add("d-none");
            surveysList.innerHTML = "";
    
            // Clear and populate UI
            const criteriaList = document.getElementById("criteria-list");
            criteriaList.innerHTML = "";
            criteria.forEach((criterion) => {
                const card = createCriterionCard(criterion);
                criteriaList.appendChild(card);
            });
            criteriaList.classList.remove("d-none");
    

        } catch (error) {
            console.error("Error selecting survey:", error);
        }
    }
    
    function showCriterionInfo(criterion, event = null) {
        const modal = document.getElementById("criterion-info-modal");
        const modalDialog = modal.querySelector(".modal-dialog");
    
        const modalTitle = document.getElementById("criterion-info-modal-label");
        const modalContent = document.getElementById("criterion-info-modal-content");
    
        // Ensure the content is cleared and updated dynamically
        modalTitle.textContent = criterion.name || "No Title Available";
        modalContent.textContent = criterion.description || "No Description Available";
    
        // Dynamically position the modal
        if (event) {
            const { clientX, clientY } = event; // Get the click position
            modalDialog.style.position = "fixed";
            modalDialog.style.left = `${-modalDialog.offsetWidth / 2}px`;
            modalDialog.style.top = `${clientY - modalDialog.offsetHeight / 2}px`;
        } else {
            modalDialog.style.position = "fixed";
            modalDialog.style.left = "50%";
            modalDialog.style.top = "50%";
            modalDialog.style.transform = "translate(-50%, -50%)";
        }
    
        // Reinitialize and show the modal
        const bootstrapModal = new bootstrap.Modal(modal, {
            backdrop: true, // Ensure proper backdrop handling
            focus: true,    // Ensure focus is set to the modal
        });
        bootstrapModal.show();
    }
    
    function resetSurveySearch() {
        const searchBar = document.getElementById("survey-input-group");
        const surveysList = document.getElementById("surveys-list");
        const criteriaList = document.getElementById("criteria-list");

        // Restore original search bar
        searchBar.innerHTML = `
            <span class="input-group-text" id="survey-section">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                    <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"></path>
                </svg>
            </span>
            <input id="survey-search-input" type="text" class="form-control" placeholder="Search surveys" aria-label="Search Surveys" oninput="surveySearch()">
            <button id="survey-filter-button" class="btn btn-secondary was-btn-outline bi bi-funnel" type="button" data-bs-toggle="collapse" data-bs-target="#survey-filter-options" aria-expanded="false" aria-controls="survey-filter-options"></button>
        `;
        surveysList.innerHTML = "";
        surveysList.classList.remove("d-none");

        criteriaList.innerHTML = "";
        criteriaList.classList.add("d-none");

        // Fetch all surveys to reset the results
        fetchAllSurveys();
    }

    // Enable or Disable Criteria Section
    document.querySelectorAll('input[name="screen_type"]').forEach((radio) => {
        radio.addEventListener('change', () => {
            const criteriaList = document.getElementById("criteria-list");
            criteriaList.querySelectorAll("input, button").forEach((element) => {
                element.disabled = !radio.checked;
            });
        });
    });
    // Function to update slider thumb style
    function updateThumbStyle(valueDisplay, rangeInput) {
        if (valueDisplay.value) {
            HeaderBar.enableSaveButton();
            rangeInput.classList.add("filled");
            rangeInput.classList.remove("cleared");
        } else {
            rangeInput.classList.add("cleared");
            rangeInput.classList.remove("filled");
        }
    }


    function setupCriterionInteractions(rangeInput, valueDisplay, clearButton) {
    
        // Sync range and input
        rangeInput.addEventListener("input", () => {
            valueDisplay.value = rangeInput.value;
            updateThumbStyle();
        });
    
        valueDisplay.addEventListener("input", () => {
            const value = parseInt(valueDisplay.value, 10);
            if (!isNaN(value) && value >= 1 && value <= 10) {
                rangeInput.value = value;
            } else {
                rangeInput.value = "";
            }
            updateThumbStyle();
        });
    
        // Clear values on clear button click
        clearButton.addEventListener("click", () => {
            rangeInput.value = "";
            valueDisplay.value = "";
            updateThumbStyle(valueDisplay, rangeInput);
        });
    
        // Initialize thumb style
        updateThumbStyle(valueDisplay, rangeInput);
    }
    
    let criterionIdCounter = 0;

    function createUniqueId(base, id) {
        return `${base}-${id}`;
    }

    function clearSurveyResponses() {
        // Get the survey container or the root where criterion cards are present
        const criteriaList = document.getElementById("criteria-list");
        const valueDisplays = criteriaList.querySelectorAll('.criterion-value-display');
        const rangeInputs = criteriaList.querySelectorAll('.criterion-range');

        HeaderBar.enableSaveButton();

    
        // Clear the value displays and range inputs
        valueDisplays.forEach((valueDisplay) => {
            valueDisplay.value = "";
        });
    
        rangeInputs.forEach((rangeInput) => {
            rangeInput.value = "";
            rangeInput.classList.remove("filled");
            rangeInput.classList.add("cleared");
        });
    
    }

    function hideCriteriaList() {
        const criteriaList = document.getElementById("criteria-list");
        criteriaList.classList.add("d-none");
    }


    function showCriteriaList() {
        const criteriaList = document.getElementById("criteria-list");
        criteriaList.classList.remove("d-none");
    }

    function setCriteriaEditable(isEditable) {
        const criteriaList = document.getElementById("criteria-list");
    
        if (isEditable) {
            criteriaList.classList.remove("disabled");
        } else {
            criteriaList.classList.add("disabled");
        }
    }
    
    function setupCriteriaInteraction() {
        const criteriaList = document.getElementById("criteria-list");
        criteriaList.addEventListener("click", (event) => {
            if (criteriaList.classList.contains("disabled")) {
                event.preventDefault(); // Prevent the default interaction
                showModal("Please select a title to survey.");
            }
        });
    }
    
    function showModal(message) {
        // Create a simple modal dynamically or use an existing Bootstrap modal
        const modalContent = document.getElementById("modal-content");
        const modal = new bootstrap.Modal(document.getElementById("instruction-modal"));
    
        modalContent.textContent = message;
        modal.show();
    }
    

    // function createCriterionCard(criterion, existingRatings) {
    //     const template = document.getElementById("criterion-card-template");
    //     const card = template.content.cloneNode(true);
    
    //     // Generate unique IDs
    //     const rangeId = createUniqueId("criterion-range");
    //     const valueDisplayId = createUniqueId("criterion-value-display");
    //     const clearButtonId = createUniqueId("criterion-value-clear");
    
    //     // Update IDs in the card
    //     const rangeInput = card.querySelector("#criterion-range");
    //     const valueDisplay = card.querySelector("#criterion-value-display");
    //     const clearButton = card.querySelector("#criterion-value-clear");
    
    //     rangeInput.id = rangeId;
    //     valueDisplay.id = valueDisplayId;
    //     clearButton.id = clearButtonId;
    
    //     // Add classes to the inputs
    //     rangeInput.classList.add("criterion-range");
    //     valueDisplay.classList.add("criterion-value-display");
    
    //     // Pre-fill values if available
    //     if (existingRatings && existingRatings.ratings) {

    //         // Parse encoded ratings if necessary
    //         let parsedRatings;
    //         try {
    //             parsedRatings = typeof existingRatings.ratings === "string"
    //                 ? JSON.parse(existingRatings.ratings)
    //                 : existingRatings.ratings;
    //         } catch (error) {
    //             console.error("Failed to parse ratings:", error);
    //         }

    //         const existingValue = parsedRatings ? parsedRatings[rangeId] : null;
    //         if (existingValue) {
    //             rangeInput.value = existingValue;
    //             valueDisplay.value = existingValue;
    //         }
    //     }
    
    //     // Set up interactions
    //     setupCriterionInteractions(rangeInput, valueDisplay, clearButton);
    
    //     // Event listeners for manual updates
    //     rangeInput.addEventListener("input", () => {
    //         valueDisplay.value = rangeInput.value;
    //     });
    
    //     valueDisplay.addEventListener("focus", () => {
    //         valueDisplay.select(); // Automatically selects the text
    //     });
    
    //     valueDisplay.addEventListener("input", () => {
    //         const value = parseInt(valueDisplay.value, 10);
    
    //         // Validate input
    //         if (!isNaN(value)) {
    //             if (value < 1) {
    //                 value = 1;
    //             } else if (value > 10) {
    //                 value = 10;
    //             }
    //             valueDisplay.value = value; // Update display if clamped
    //             rangeInput.value = value; // Update slider if valid
    //         } else {
    //             valueDisplay.value = ""; // Reset invalid input
    //             rangeInput.value = ""; // Reset slider
    //         }
    //     });
    
    //     clearButton.addEventListener("click", () => {
    //         rangeInput.value = ""; // Reset slider
    //         valueDisplay.value = ""; // Clear display
    //     });
    
    //     // Update other card content
    //     const title = card.querySelector(".text-truncate");
    //     title.textContent = criterion.name;
    
    //     const infoButton = card.querySelector(".btn-link");
    //     infoButton.addEventListener("click", () => {
    //         showCriterionInfo(criterion);
    //     });
    
    //     return card;
    // }
    

    // function createCriterionCard(criterion, existingRatings) {
    //     const template = document.getElementById("criterion-card-template");
    //     const card = template.content.cloneNode(true);
    
    //     // Set criterion name as a data attribute
    //     const cardElement = card.querySelector(".card");
    //     cardElement.setAttribute("data-criterion-name", criterion.name);
    //     cardElement.setAttribute("data-criterion-id", criterion.id);
    
    //     // Generate unique IDs
    //     const rangeId = createUniqueId("criterion-range");
    //     const valueDisplayId = createUniqueId("criterion-value-display");
    //     const clearButtonId = createUniqueId("criterion-value-clear");
    
    //     // Update IDs in the card
    //     const rangeInput = card.querySelector("#criterion-range");
    //     const valueDisplay = card.querySelector("#criterion-value-display");
    //     const clearButton = card.querySelector("#criterion-value-clear");
    
    //     rangeInput.id = rangeId;
    //     valueDisplay.id = valueDisplayId;
    //     clearButton.id = clearButtonId;
    
    //     // Pre-fill values if available
    //     if (existingRatings && existingRatings.ratings) {
    //         const existingValue = existingRatings.ratings[criterion.name];
    //         if (existingValue) {
    //             rangeInput.value = existingValue;
    //             valueDisplay.value = existingValue;
    //         }
    //     }
    

    //     return card;
    // }

    function clampValue(value, min=1, max=10) {
        // Validate input
        if (!isNaN(value)) {
            if (value < min) {
                value = min;
            } else if (value > max) {
                value = max;
            }
        }
        return value;
    }

    function addUniqueID(DOMObject, genericId, id) {
        const uniqueID = createUniqueId(genericId, id);
        const element = DOMObject.querySelector(`#${genericId}`);
        // console.log("Element:", element);
        element.id = uniqueID;
        element.classList.add(genericId);
        return element;
    }

    function createCriterionCard(criterion) {
        const template = document.getElementById("criterion-card-template");
        const card = template.content.cloneNode(true);
    
        // Set criterion name as a data attribute
        const cardElement = card.querySelector(".criterion-card");
        cardElement.setAttribute("data-criterion-id", criterion.id);
        cardElement.setAttribute("data-criterion-name", criterion.name);
        
        // Generate unique IDs
        const rangeInput = addUniqueID(card, "criterion-range", criterion.id);
        const valueDisplay = addUniqueID(card, "criterion-value-display", criterion.id);
        const clearButton = addUniqueID(card, "criterion-value-clear", criterion.id);

        // Populate initial values from state
        const existingValue = state.ratings[criterion.id] || "";
        rangeInput.value = existingValue;
        valueDisplay.value = existingValue;

        if (existingValue) {
            rangeInput.classList.add("filled");
        }
    
        // select text to be ready for new input
        valueDisplay.addEventListener("focus", () => {
            valueDisplay.select();
        });
    
        clearButton.addEventListener("click", () => {
            rangeInput.value = ""; // Reset slider
            valueDisplay.value = ""; // Clear display
        });
    
        // Update other card content
        const title = card.querySelector(".text-truncate");
        title.textContent = criterion.name;
    
        const infoButton = card.querySelector(".btn-link");
        infoButton.addEventListener("click", (event) => {
            showCriterionInfo(criterion, event);
        });
        

        // Update state on interaction
        rangeInput.addEventListener("input", () => {
            const value = rangeInput.value;
            state.ratings[criterion.id] = value; // Update state
            valueDisplay.value = value; // Sync display
            updateThumbStyle(valueDisplay, rangeInput);

        });
    
        valueDisplay.addEventListener("input", () => {
            const value = valueDisplay.value;
            state.ratings[criterion.id] = value; // Update state
            rangeInput.value = value; // Sync slider
            updateThumbStyle(valueDisplay, rangeInput);
        });
    
        return card;
    }
    
    
    // async function saveSurveyResponses() {
    //     // Ensure required state values are set
    //     if (!state.title_id || !state.survey_id) {
    //         console.error("Title ID and Survey ID are required to save responses.");
    //         return;
    //     }

    //     // Collect survey responses from criteria inputs    
    //     const criteriaList = document.querySelectorAll(".criterion-card");
    //     const ratings = {};
    
    //     criteriaList.forEach((card) => {
    //         // const criterionName = card.getAttribute("data-criterion-name");
    //         const criterionId = card.getAttribute("data-criterion-id");
    //         const rangeInput = card.querySelector(".criterion-range");
    //         const valueDisplay = card.querySelector(".criterion-value-display");
    //         ratings[criterionId] = valueDisplay.value || null; // Save value or null if unset
    //         console.log("Criterion ID:", criterionId, "Value:", valueDisplay.value);
    //     });
    
    //     // TODO: add UI field input for comments
    //     const commentsInput = document.getElementById("comments")
    //     if (commentsInput) {
    //         comments = commentsInput.value || ""; 
    //     } else {
    //         comments = "";
    //     }
    
    //     console.log("State:", state);

    //     const payload = {
    //         title_id: state.title_id,
    //         survey_id: state.survey_id,
    //         ratings: ratings,
    //         comments,
    //         screen_type: state.screen_type || null,
    //     };
    //     try {
    //         const response = await fetch("/api/v1/ratings/", {
    //             method: "POST",
    //             headers: {
    //                 "Content-Type": "application/json",
    //             },
    //             body: JSON.stringify(payload),
    //         });
    
    //         if (response.ok) {
    //             const result = await response.json();
    //             // console.log("Ratinga saved successfully:", result);
    //             const saveStatus = document.getElementById("save-status");
    //             HeaderBar.disableSaveButton();
    //             // saveStatus.textContent = "All changes saved";
    //             // saveStatus.style.color = "green";
    //         } else {
    //             const error = await response.json();
    //             console.error("Error saving rating:", error);
    //             const saveStatus = document.getElementById("save-status");
    //             // saveStatus.textContent = "Failed to save changes";
    //             // saveStatus.style.color = "red";
    //         }
    //     } catch (error) {
    //         console.error("Error saving rating:", error);
    //         const saveStatus = document.getElementById("save-status");
    //         // saveStatus.textContent = "Failed to save changes";
    //         // saveStatus.style.color = "red";
    //     }
    // }

    async function saveSurveyResponses() {
        const payload = {
            title_id: state.title_id,
            survey_id: state.survey_id,
            screen_type: state.screen_type,
            ratings: state.ratings,
        };
    
        try {
            const response = await fetch("/api/v1/ratings/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload),
            });
    
            if (response.ok) {
                console.log("Survey responses saved successfully.");
            } else {
                console.error("Failed to save survey responses.");
            }
        } catch (error) {
            console.error("Error saving survey responses:", error);
        }
    }
    

    return {
        createSurveyCard,
        fetchAllSurveys,
        surveySearch,
        selectSurvey,
        showCriterionInfo,
        // updateViewedOn,
        resetSurveySearch,
        setupCriterionInteractions,
        createUniqueId,
        createCriterionCard,
        clearSurveyResponses,
        hideCriteriaList,
        showCriteriaList,
        setCriteriaEditable,
        saveSurveyResponses,
        setupCriteriaInteraction,
    };


})();



// // fetch all surveys on initial page load
// document.addEventListener("DOMContentLoaded", SurveySelect.fetchAllSurveys);

// // Initialize criteria interactions
// document.addEventListener("DOMContentLoaded", () => {
//     setupCriteriaInteraction();
//     setCriteriaEditable(false); // Initially non-editable
// });
    
    
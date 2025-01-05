

const TitleSelect = (function() {
    let titles = [];

    // Filters
    let filters = {
        lock: false,
        collection: "",
        startYear: null,
        endYear: null,
    };

    // Trigger Filter Application on "Enter" or "Tab"
    document.getElementById("title-start-year").addEventListener("keydown", handleFilterKey);
    document.getElementById("title-end-year").addEventListener("keydown", handleFilterKey);
    

    function handleFilterKey(event) {
        if (event.key === "Enter" || event.key === "Tab") {
            // event.preventDefault(); // Prevent default behavior for Tab
            updateFilters();
        }
    }

    const filterContainer = document.getElementById("title-filters-container");
    // const filterButton = document.getElementById("title-filter-button");
    
    function hideFilters() {
        const filterContainer = document.getElementById("title-filters-container");

        if (filterContainer.classList.contains("visible")) {
            filterContainer.classList.remove("visible");
            filterContainer.classList.add("hidden");
        }

    };

    function updateFilters() {
        filters.startYear = document.getElementById("title-start-year").value || null;
        filters.endYear = document.getElementById("title-end-year").value || null;

        // Change filter icon to indicate active filters
        const filterButton = document.getElementById("title-filter-button");
        if (filterButton != null) {
            if (filters.startYear || filters.endYear) {
                filterButton.classList.remove("bi-funnel");
                filterButton.classList.add("bi-funnel-fill");
            } else {
                filterButton.classList.remove("bi-funnel-fill");
                filterButton.classList.add("bi-funnel");
            }
        }

        // Trigger a new search with updated filters
        searchTitles();
    }

    function toggleFilters() {
        if (filterContainer.classList.contains("hidden")) {
            // Show the filters
            filterContainer.classList.remove("hidden");
            filterContainer.classList.add("visible");
        } else {
            // Hide the filters
            filterContainer.classList.remove("visible");
            filterContainer.classList.add("hidden");
        }
    }

    function clearFilters() {

        filters.collection = "";
        filters.startYear = null;
        filters.endYear = null;

        startYear = document.getElementById("title-start-year")
        endYear = document.getElementById("title-end-year")

        startYear.value = "";
        endYear.value = "";
        updateFilters();
    };
    

    async function fetchTitleTypes() {
        try {
            const response = await fetch("/api/v1/title-types");
            if (!response.ok) throw new Error("Failed to fetch title types.");
            return await response.json();
        } catch (error) {
            console.error("Error fetching title types:", error);
            return [];
        }
    }

    async function addTitle(form, resultsList) {
        const name = form.querySelector("#add-title-name").value;
        const year = form.querySelector("#add-title-year").value;
        const type = form.querySelector("#add-title-type").value;
    
        try {
            const response = await fetch("/api/v1/titles/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ name, year, type }),
            });
    
            const result = await response.json();
    
            if (response.ok) {
                // Build API URL with query and filters
                let innerApiUrl = `/api/v1/titles/`+ result.title_id;
    
                // Fetch titles from the API
                const inner_response = await fetch(innerApiUrl);
                if (!inner_response.ok) {
                    throw new Error("Failed to fetch title with id: " + result.title_id);
                }
                const apiInnerResponse = await inner_response.json();
    
                // If the API inner_response wraps the list in an object, extract it
                titles = [ apiInnerResponse ];
    
                selectTitle(apiInnerResponse.id);
            } else {
                const errorDiv = form.querySelector("#add-title-error");
                errorDiv.textContent = result.error || "Failed to add title.";
                errorDiv.style.display = "block";
            }
        } catch (error) {
            const errorDiv = form.querySelector("#add-title-error");
            errorDiv.textContent = "An error occurred while adding the title.";
            errorDiv.style.display = "block";
            console.error(error);
        }
    }
    
    async function showAddTitleForm(query, titleSearchResults) {
        const template = document.getElementById("add-title-form-template").content.cloneNode(true);
        const form = template.querySelector("#add-title-form");
    
        // Prefill the title input and focus the year field
        const titleInput = template.querySelector("#add-title-name");
        const yearInput = template.querySelector("#add-title-year");
        const typeSelect = template.querySelector("#add-title-type");
    
        titleInput.value = query; // Prefill with the search query
        yearInput.focus();
    
        // Fetch and populate title types
        const titleTypes = await fetchTitleTypes();
        titleTypes.forEach(({ display_name, type }) => {
            const option = document.createElement("option");
            option.value = type;
            option.textContent = display_name;
            typeSelect.appendChild(option);
        });

        // make sure typeSelect selection is none to start
        typeSelect.selectedIndex = -1;
    
        // Add form submission logic
        form.addEventListener("submit", async (event) => {
            event.preventDefault();
            await addTitle(form, titleSearchResults);
        });
    
        // Append the form to the results
        titleSearchResults.innerHTML = ""; // Clear existing content
        titleSearchResults.appendChild(template);
        titleSearchResults.classList.remove("d-none");
    }

    async function searchTitles() {
        const input_value = document.getElementById("title-search-input").value;
        const query = input_value.toLowerCase();
        const titleSearchResults = document.getElementById("title-search-results");

        // Clear results if the query is empty
        if (!query) {
            titleSearchResults.innerHTML = `<div class="text-center">-- Selecte a title to review --</div>`;
            titleSearchResults.classList.add("text-center");
            updateResultsVisibility();
            return;
        }

        try {
            // Build API URL with query and filters
            let apiUrl = `/api/v1/titles/search?query=${encodeURIComponent(query)}`;
            if (filters.startYear) {
                apiUrl += `&year_start=${encodeURIComponent(filters.startYear)}`;
            }
            if (filters.endYear) {
                apiUrl += `&year_end=${encodeURIComponent(filters.endYear)}`;
            }

            // Fetch titles from the API
            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error("Failed to fetch titles");
            }
            const apiResponse = await response.json();

            // If the API response wraps the list in an object, extract it
            const results = Array.isArray(apiResponse) ? apiResponse : apiResponse.results;
            titles = results;

            titleSearchResults.innerHTML = '<div class="mb-3">Selecte a title to review:</div>'; // Clear previous results
            titleSearchResults.classList.remove("text-center");


            if (results.length === 0) {
                showAddTitleForm(input_value, titleSearchResults);
            } else {
                results.slice(0, 10).forEach((title) => {
                    const listItem = document.createElement("li");
                    listItem.className = "list-group-item";
                    listItem.textContent = `${title.name} (${title.year})`;
                    listItem.onclick = () => selectTitle(title.id);
                    titleSearchResults.appendChild(listItem);
                });

                if (results.length > 10) {
                    const ellipsis = document.createElement("li");
                    ellipsis.className = "list-group-item text-muted";
                    ellipsis.textContent = ". . . .";
                    titleSearchResults.appendChild(ellipsis);
                }
            }
        } catch (error) {
            console.error("Error fetching titles:", error);
            titleSearchResults.innerHTML = `
                <li class="list-group-item text-danger">Failed to load results. Please try again.</li>
                <li>`+ error + `</li>
            `;
        }
        updateResultsVisibility();
    }
    
    function updateResultsVisibility() {
        const titleSearchResults = document.getElementById("title-search-results");
        if (titleSearchResults.children.length > 0) {
            titleSearchResults.classList.remove("d-none");
        } else {
            titleSearchResults.classList.add("d-none");
        }
    };


    async function selectTitle(title_id) {
        const selectedTitle = titles.find((title) => title.id === title_id);
        const titleSearchResults = document.getElementById("title-search-results");
        // const titleInputGroup = document.querySelector(".input-group");
        const titleInputGroup = document.getElementById("title-input-group");

        // Replace search bar with selected title display
        titleInputGroup.innerHTML = `
            <div class="form-control bg-light">${selectedTitle.name} (${selectedTitle.year})</div>
            <button id="title-edit-button" class="btn btn-secondary was-btn-outline" onclick="TitleSelect.resetTitleSearch()">
                <i id="title-edit-button" class="bi bi-pencil"></i>
            </button>
        `;

        // Expand the selected title to fill the results area
        titleSearchResults.innerHTML = ''; // Clear previous results
        updateResultsVisibility();

        // updateFilters();
        hideFilters();

        state.title_id = selectedTitle.id;
        // update ratings and screen_type with existing values
        ScreenSelect.showScreenOptions();
        await fetchAndApplyRatings();

        // Update the screen type selector from state
        await ScreenSelect.prefillScreenType();
        // SurveySelect.showCriteriaList();
        SurveySelect.setCriteriaEditable(true)
        
        // select the survey if one is in the state
        if (state.survey_id) {
            SurveySelect.selectSurvey(state.survey_id);
        }

    }


    // Reset to the search interface
    function resetTitleSearch() {
        // const titleInputGroup = document.querySelector(".input-group");
        const titleSearchResults = document.getElementById("title-search-results");
        const titleInputGroup = document.getElementById("title-input-group");

        // Restore original search bar
        titleInputGroup.innerHTML = `
            <span class="input-group-text" id="title-section"><i class="bi bi-search"></i></span>
            <input id="title-search-input" type="text" class="form-control" placeholder="Start typing a title to review" aria-label="Search Titles" oninput="TitleSelect.searchTitles()">
            <button id="title-filter-button" class="btn btn-secondary was-btn-outline bi bi-funnel" type="button"  onclick="TitleSelect.toggleFilters()" data-bs-toggle="collapse" data-bs-target="#title-filter-body" aria-expanded="false" aria-controls="title-filter-body"></button>
        `;

        // Clear search results
        titleSearchResults.innerHTML = "-- Search for a title to review --";
        titleSearchResults.classList.remove("d-none");
        titleSearchResults.classList.add("text-center");
        if (!filters.lock) {
            clearFilters();
        }
        HeaderBar.disableSaveButton();

        SurveySelect.clearSurveyResponses();
        ScreenSelect.clearScreenOptions();
        SurveySelect.setCriteriaEditable(false)


        updateFilters();
    }

    function toggleFilterLock () {
        filters.lock = !filters.lock;
        const lockButton = document.getElementById("title-filter-lock-button");
        if (filters.lock) {
            lockButton.innerHTML = `<i class="bi bi-lock-fill"></i>`
        } else {
            lockButton.innerHTML = `<i class="bi bi-unlock"></i>`
        }
    };


    function showAddTitle() {
        // Logic to open "Add Title" modal
    }

    return {
        clearFilters,
        // handleFilterToggle,
        handleFilterKey,
        hideFilters,
        resetTitleSearch,
        searchTitles,
        selectTitle,
        showAddTitle,
        toggleFilters,
        toggleFilterLock,
        updateFilters,
    };
})();

// document.addEventListener("DOMContentLoaded", TitleSelect.searchTitles);

// document.addEventListener("DOMContentLoaded", function() {
//     resetTitleSearch();
// });

let screen_types = {}
async function fetchScreenTypes() {
    return fetch("/api/v1/screen-types")
        .then((response) => response.json())
        .then((data) => {
            screen_types = data;
        })
        .catch((error) => {
            console.error("Error fetching screen types:", error);
        });
}
fetchScreenTypes();

const ScreenSelect = (function() {




    function showScreenOptions() {
        const screenOptionsContainer = document.getElementById("screen-types-container");
        const template = document.getElementById("screen-types-template").content.cloneNode(true);

        screenOptionsContainer.classList.remove("d-none");
        screenOptionsContainer.innerHTML = ``;
        screenOptionsContainer.appendChild(template);

    }

    function hideScreenOptions() {
        const screenOptionsContainer = document.getElementById("screen-types-container");
        const template = document.getElementById("screen-types-template").content.cloneNode(true);

        screenOptionsContainer.classList.add("d-none");
        screenOptionsContainer.innerHTML = ``;
    }

    async function prefillScreenType() {
        const screenType = state.screen_type;
    
        if (screenType) {
            const radioButtons = document.querySelectorAll('input[name="screen_type"]');
            radioButtons.forEach((button) => {
                if (button.value === screenType) {
                    button.checked = true;
                }
            });
        }
    }
    
    function setupScreenTypeSelector() {
        const radioButtons = document.querySelectorAll('input[name="screen_type"]');
    
        radioButtons.forEach((button) => {
            button.addEventListener("change", () => {
                if (button.checked) {
                    state.screen_type = button.value; // Update state
                }
            });
        });
    
        // Sync initial state
        prefillScreenType();
    }
    

    // // Toggles the edit view for "Screen Type"
    // function toggleViewedOnEdit() {
    //     const options = document.getElementById("screen-types");
    //     const editButton = document.getElementById("screen-types-edit-button");

    //     if (options.style.display === "none") {
    //         editButton.innerHTML = `<i class="bi bi-chevron-up"></i>`;
    //         options.style.display = "flex";
    //     } else {
    //         editButton.classList.remove("d-none");
    //         editButton.innerHTML = `<i class="bi bi-pencil"></i>`;
    //         options.style.display = "none";
    //     }
    // }


    // Updates the selected "Screen Type" value
    function selectScreenType(screen_type_type) {
        // lookup scren_type_id from screen_types where screen_types[id].type == screen_type
        for (const [key, value] of Object.entries(screen_types)) {
            if (value.type == screen_type_type) {
                screen_type_id = value.id;
            }
        }
        selectScreenTypeFromId(screen_type_id);
    }

    function selectScreenTypeFromId(screen_type_id) {
        // console.log("Selecting screen type from id:", screen_type_id);
        // const options = document.getElementById("screen-types");
        // const editButton = document.getElementById("screen-types-edit-button");

        // check against current state and update if needed
        if (state.screen_type_id == screen_type_id) {
            return;
        }
        HeaderBar.enableSaveButton();

        // lookup scren_type.type from screen_types
        for (const [key, value] of Object.entries(screen_types)) {
            if (value.id == screen_type_id) {
                screen_type_type = value.type;
            }
        }
        state.screen_type = screen_type_type
        state.screen_type_id = screen_type_id;
        // editButton.classList.remove("d-none");
        // options.style.display = "none";
        // console.log("Selected screen type:", screen_type_type);
        updateViewedOn(screen_type_id)
        // updateViewedOn(screen_type_type)
        
        
    }

    function updateViewedOn(screen_type_id) {
        // console.log("Updating viewed on screen type:", screen_type_id);
        const screenTypeValue = document.getElementById("screen-type-value");
        // console.log("Screen type value:", screenTypeValue);

        // lookup scren_type.type from screen_types
        for (const [key, value] of Object.entries(screen_types)) {
            if (value.id == screen_type_id) {
                display_name = value.display_name;
                screen_type_type = value.type;
                // console.log("Screen type type:", screen_type_type);
                // console.log("Display name:", display_name);
            }
        }

        // display_name = screen_types[screen_type_id].display_string;
        screenTypeValue.innerHTML = `<span>Viewed on ${display_name}</span>`;

        const screenTypesSelector = document.querySelectorAll('input[name="screen-type-selector"]');
        screenTypesSelector.forEach((option) => {
            if (option.value == screen_type_type) {
                option.checked = true;
            }
        });

    }

    function clearScreenOptions() {

        // Reset "viewed on" radio buttons
        const viewedOnOptions = document.querySelectorAll('input[name="screen_type"]');
        viewedOnOptions.forEach((option) => {
            option.checked = false; // Uncheck all options
        });

        hideScreenOptions();
    }
    
    return {
        clearScreenOptions,
        prefillScreenType,
        selectScreenType,
        selectScreenTypeFromId,
        setupScreenTypeSelector,
        showScreenOptions,
        // toggleViewedOnEdit,
        updateViewedOn,
    };

})();

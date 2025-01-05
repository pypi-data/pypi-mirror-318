

let surveyResponses = {}; // Store survey responses for the current title

const HeaderBar = (function() {

    function enableSaveButton() {
        const saveButton = document.getElementById("save-ratings-button");
        // saveButton.disabled = false;
        saveButton.classList.remove("disabled");
    }

    function disableSaveButton() {
        const saveButton = document.getElementById("save-ratings-button");
        // saveButton.disabled = true;
        saveButton.classList.add("disabled");
    }

    return {
        enableSaveButton,
        disableSaveButton,
    };

})();
document.addEventListener("DOMContentLoaded", function () {
    const linterFilter = document.getElementById("linter-filter");
    const tableRows = document.querySelectorAll("tbody tr");

    // Filter function
    linterFilter.addEventListener("change", function () {
        const selectedLinter = linterFilter.value.toLowerCase();
        tableRows.forEach((row) => {
            const linterCell = row.querySelector("td:first-child");
            const linterName = linterCell ? linterCell.textContent.toLowerCase() : "";
            row.style.display = selectedLinter === "" || linterName === selectedLinter ? "" : "none";
        });
    });
});
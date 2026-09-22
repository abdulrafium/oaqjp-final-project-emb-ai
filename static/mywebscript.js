/**
 * Executes the Emotion Detection request to the Flask server
 * and displays the response in the web UI.
 */
let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    let responseDiv = document.getElementById("system_response");

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            responseDiv.innerHTML = this.responseText;
            responseDiv.style.display = "block";
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};

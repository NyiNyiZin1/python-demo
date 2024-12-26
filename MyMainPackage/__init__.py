<!-- Include the CSS class definition -->
<style>
.selected-text {
  text-decoration: underline;
}
</style>

<!-- HTML content -->
<div id="my-text" onclick="underlineText(event)">This is my text.</div>

<script>
function underlineText(event) {
  // Get the selected text
  var selectedText = window.getSelection().toString();
  
  // Check if any text is selected
  if (selectedText.length > 0) {
    // Wrap the selected text in a span with the CSS class
    var modifiedHTML = '<span class="selected-text">' + selectedText + '</span>';
  
    // Replace the original text with the modified HTML
    var textElement = document.getElementById('my-text');
    textElement.innerHTML = textElement.innerHTML.replace(selectedText, modifiedHTML);
  }
}
</script>
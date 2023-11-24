const textarea = document.querySelector("textarea");
const languageDiv = document.querySelector(".language");
const language = languageDiv.getAttribute("data-language");

function getLanguageMode(choice) {
  switch (choice) {
    case "javascript":
      return "javascript";
    case "python":
      return "python";
    case "java":
      return "text/x-java";
    case "c":
      return "text/x-c";
    case "c#":
      return "text/x-csharp";
    case "c++":
      return "text/x-objectivec++";
  }
}

const codeMirrorInstance = CodeMirror.fromTextArea(textarea, {
  mode: getLanguageMode(language),
});

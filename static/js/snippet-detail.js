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

const textArea = document.querySelector("textarea");
const language = textArea.getAttribute("data-language");
const codeMirrorInstance = CodeMirror.fromTextArea(textArea, {
  mode: getLanguageMode(language),
  readOnly: true,
});

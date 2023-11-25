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

const textareas = Array.from(document.querySelectorAll("textarea"));

textareas.forEach((textarea) => {
  const language = textarea.getAttribute("data-language");
  const codeMirrorInstance = CodeMirror.fromTextArea(textarea, {
    mode: getLanguageMode(language),
  });
});

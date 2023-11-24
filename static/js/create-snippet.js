const select = document.querySelector("select");
const textarea = document.querySelector("textarea");
const form = document.querySelector("form");
const button = document.querySelector(".submit-btn");
let codeMirrorInstance;

export function getLanguageMode(choice) {
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

select.addEventListener("change", (e) => {
  if (codeMirrorInstance) {
    codeMirrorInstance.toTextArea();
  }
  codeMirrorInstance = CodeMirror.fromTextArea(textarea, {
    mode: getLanguageMode(e.target.value),
  });
});

button.addEventListener("click", (e) => {
  textarea.value = codeMirrorInstance.getValue();
  form.submit();
});

window.addEventListener("load", function () {
  if (true) {
    textarea.value = "";
    select.value = null;
  }
});

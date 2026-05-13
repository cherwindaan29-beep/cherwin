// HAMBURGER MENU //
function toggleMenu() {
  const nav = document.getElementById("myNavbar");

  if (nav.className === "navbar") {
    nav.className += " responsive";
  } else {
    nav.className = "navbar";
  }
}


// SHOW CODE SNIPPET //
function showCode(skill) {

  let code = "";

  if (skill === "html") {
    code = `<h1>Hello World</h1>`;
  }

  else if (skill === "css") {
    code = `body{
  background: black;
}`;
  }

  else if (skill === "js") {
    code = `console.log("Hello World");`;
  }

  document.getElementById("codeOutput").innerText = code;
}


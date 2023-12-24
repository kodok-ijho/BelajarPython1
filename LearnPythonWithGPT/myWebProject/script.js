function greet(name) {
    return "Hello, " + name + "!";
}
var heading = document.querySelector('h1');
heading.textContent = greet('User');

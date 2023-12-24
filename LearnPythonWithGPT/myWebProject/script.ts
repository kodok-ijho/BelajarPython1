function greet(name: string): string {
    return "Hello, " + name + "!";
}

const heading = document.querySelector('h1')!;
heading.textContent = greet('User');

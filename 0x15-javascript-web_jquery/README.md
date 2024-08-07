# 0x15. JavaScript - Web jQuery

## Description

This project covers the basics of using JavaScript with the jQuery library to manipulate the DOM, handle events, and fetch data using AJAX.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Chrome (version 57.0)
- All files should end with a new line
- Code should be semistandard compliant with the flag `--global $`: `semistandard *.js --global $`
- You must use JQuery version 3.x
- You are not allowed to use `var`
- HTML should not reload for each action: DOM manipulation, update values, fetch data...

## Tasks

0. **No JQuery** - Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`).
1. **With JQuery** - Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) using JQuery.
2. **Click and turn red** - Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`.
3. **Add `.red` class** - Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`.
4. **Toggle classes** - Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`.
5. **List of elements** - Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`.
6. **Change the text** - Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`.
7. **Star wars character** - Write a JavaScript script that fetches the character name from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`.
8. **Star Wars movies** - Write a JavaScript script that fetches and lists the title for all movies by using this URL: `https://swapi-api.alx-tools.com/api/films/?format=json`.
9. **Say Hello!** - Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.
10. **No jQuery - Document Loaded** - Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`). Note: Your script must be imported from the `<head>` tag, not at the end of the HTML.
11. **List, Add, Remove** - Write a JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks:
    - The new element must be: `<li>Item</li>`
    - The new element must be added to `UL.my_list`
    - When the user clicks on `DIV#add_item`: a new element is added to the list
    - When the user clicks on `DIV#remove_item`: the last element is removed from the list
    - When the user clicks on `DIV#clear_list`: all elements of the list are removed
12. **Say Hello to Everybody!** - Write a JavaScript script that fetches and prints how to say "Hello" depending on the language:
    - The language code will be the value entered in the tag `INPUT#language_code` (ex: es, fr, en etc.)
    - The translation must be fetched when the user clicks on `INPUT#btn_translate`
    - The translation of "Hello" must be displayed in the HTML tag `DIV#hello`
13. **And Press ENTER** - Write a JavaScript script that fetches and prints how to say "Hello" depending on the language:
    - The language code will be the value entered in the tag `INPUT#language_code` (ex: es, fr, en etc.)
    - The translation must be fetched when the user clicks on `INPUT#btn_translate` OR presses ENTER when the focus is on `INPUT#language_code`
    - The translation of "Hello" must be displayed in the HTML tag `DIV#hello`

## Usage

To test each script, use the corresponding HTML file provided in the project description.

# HTML
Structure: `<tag attribute="value">content</tag>`
Homepage is always `(root)/index.html`

## Generating boilerplate
- `!` + `tab` in VSCode

## Adding CSS
- `<html style="attribute-value: red"></html>` - Inline CSS - ONLY ONE TAG
- `<style> tag {attribute: value} </style>` - Internal CSS - ONLY ONE HTML DOCUMENT
- Head pointer to external stylesheet - RECOMMENDED

## General Tags
- Global attributes
  - Attribute: draggable = boolean

## Pre-header
- `<!DOCTYPE html>` - Doctype declaration, generally at the very top of the page before html tag
- `<html lang = "en"></html>` - Root element, wraps everything in a page

## Header: Wrapped in `<head></head>`
Shows metadata that is not shown in page
- `<meta charset="UTF-8">` - Character encoding
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` - Responsive design
- `<title>Page Title</title>` - Title of page
- `<link rel="icon" type = "image/png" href="favicon.png">` - Favicon = Icon beside title
- `<link rel="stylesheet" href="style.css">` - Link to external CSS stylesheet

## Body: wrapped in `<body></body>`
- `<h1></h1>` to `<h6></h6>` Header tags - only 6 levels
- `<p>` Paragraph tags 
- Void elements 
  - `<br/>` = line break
  - `<hr/>` = horizontal line
- `<ul> <li>item 1</li> </ul>` Unordered list with list items 
  - `<ol> <li>item 1</li> </ol>` Ordered list
  - `<ul> <li>item 1 <ul> <li>item 1.1</li> </ul> </li> </ul>` Nested list
- `<a href="https://www.google.com">Google</a>` Anchor element = link - can be external or on the same page
  - The text can also be any other tag: header, images, etc
- `<img src="pic.jpg" alt="alt_text" width=200 height=200/>` Image element - dimensions in pixels

## Footer: wrapped in `<footer></footer>`

# CSS

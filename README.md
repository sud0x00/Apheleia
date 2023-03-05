# Apheleia

## Introduction

Apheleia is a simple Perl-based Pastebin clone that allows users to paste code snippets or any type of text and share the resulting URL with others.

## Why the name?
Apheleia is the Greek goddess of simplicity, prudence, and modesty. I chose this name for my pastebin project because I believe in the power of simplicity and minimalism in software design.

## Why use Apheleia at all ? 

Apheleia is a lightweight and responsive solution, with the entire script weighing in at just 2KB

## Requirements

- A web server running Perl
- CGI.pm and Digest::MD5 Perl modules

## Installation

1. Download the `apheleia.cgi` file from the GitHub repository.
2. Place the `apheleia.cgi` file in a directory named `apheleia` on your web server.
3. Create a directory named `pastes` in the same directory as `apheleia.cgi`. This directory will be used to store the pastes.
4. Make sure that the `apheleia.cgi` file has execute permission.

## Usage

1. Navigate to `http://localhost/apheleia/apheleia.cgi` in your web browser.
2. Paste the code you want to share in the text area provided.
3. Click the "Submit" button.
4. Your paste will be saved to the `pastes` directory with a unique filename.
5. A success message will be displayed with a link to your paste.
6. Share the link with others to share your paste.

## Notes

- The `apheleia.cgi` file uses Bootstrap for styling. You can customize the styling by modifying the `-style` parameter in the `start_html()` function.
- The `apheleia.cgi` file uses the `Digest::MD5` module to generate unique filenames for each paste. If you prefer a different naming scheme, you can modify the code accordingly.
- The `apheleia.cgi` file does not include any authentication or expiration features. If you need these features, you will need to modify the code or use a different pastebin solution.


## Demo

https://user-images.githubusercontent.com/91898207/222961987-32ea0b69-ae56-4b29-bf60-bce41e6e914a.mp4




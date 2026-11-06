---
id: WAS-C13-002
title: Code Injection
source_pages: "183-186"
chapter: 13
concepts: [code-injection, cli-injection, interpreter-injection, imagemin, filename-collision, input-sanitization, command-line-options, injection-vs-command-injection]
related: [WAS-C13-001, WAS-C13-003, WAS-C25-005]
time_sensitive: false
---
# Code Injection
(Source: PDF pp. 183-186, tail page 187)

## What the section covers
How injection generalizes beyond databases to any command-line tool or interpreter that an API endpoint drives, illustrated with MegaBank's image and video media server: a filename-collision weakness in an image upload, and a video converter whose options string accepts extra commands.

## Meaning
- SQL injection is only a subset of injection-style attacks. It counts as injection because an interpreter (the SQL interpreter) is targeted by a payload that gets read into it through improper sanitization; only specific user parameters should ever reach the interpreter (PDF p. 183).
- In the general case a CLI called by an API endpoint receives unexpected extra commands because the input was not sanitized, and those commands are run against the CLI (PDF p. 183).
- Figure 13-2 (PDF p. 183) is a flow: a user tampers with an HTTP request, adding custom commands; the API runs commands in a local CLI and the custom text lands in the command string; the CLI interprets and executes it; the CLI performs unintended operations. The figure then splits. Worst case: the commands escape the CLI and permit raw code execution. Best case: they cannot escape but still alter the CLI's intended behaviour.
- SQL injection is therefore first an injection attack and second a code injection attack: the injected script runs under an interpreter or CLI rather than against the host operating system, which would be command injection (PDF p. 183).

## Why it matters
- Lesser-known code injection is less documented than SQL injection. Almost every complex web application uses a database, so database injection is the likelier find, and SQL injection is easy to research. Other code injection is often application specific, because not every application drives a CLI or interpreter through an API endpoint (PDF p. 184).

## How it works: the media server examples
- The scenario is MegaBank's media server at media.mega-bank.com for marketing images and video. It exposes four APIs: uploadImage (POST), uploadVideo (POST), getImage (GET) and getVideo (GET) (PDF p. 184).
- uploadImage is a Node.js endpoint using imagemin with a JPEG plug-in and the file-system module. It rejects unauthenticated callers, writes the raw upload to a raw-images folder named from the request's name field, compresses it to a compressed-images folder, and returns a URL to the compressed image on the media host (PDF pp. 184-185).
- It converts a PNG to a JPG and takes no parameter from the user except the filename (PDF p. 185).
- The first problem looks like a plain bug: filenames collide, so one user could cause the library to overwrite an existing image. The book's illustration is the main logo already used on the front page of the bank's site; uploading a file with that name overwrites it (PDF p. 185).
- The book then argues it is actually injection, because the imagemin library invokes a CLI (imagemin-cli), so an improperly sanitized CLI attached to an API is being made to perform unintended actions (PDF p. 185). The text calls this a very simple example with little exploitability beyond the filename case.
- The richer example is uploadVideo (PDF p. 186). The endpoint requires authentication, reads the video data, name and an options string from the body, prepends a default options value that sets the output size to 1280x720, and runs a shell command that calls a fictional "converter" tool with the video, name and options values interpolated into the command text.
- Assumption: the converter library runs a CLI in its own context, as many Unix tools do, so after the convert command starts, the caller is scoped to the converter's commands rather than the host operating system's (PDF p. 186).
- Valid user input would be a compression type and audio bit rate, such as a codec option and a 192k audio rate. Whether more can be added depends on the CLI. The book's injected options string appends a line break followed by a second convert invocation with a directory option and a 1x1 size (PDF p. 186).
- How extra commands are chained depends on the CLI's design: some accept several commands on one line, others do not, and many are separated by line breaks, spaces or ampersands. Here a line break added a second statement. That was not the developer's intent, and the added statement redirects the converter and lets the attacker change videos they do not own (PDF p. 186).

## Transition to command injection (on the tail page)
- If the CLI instead ran against the host OS rather than in its own environment, the same flaw would be command injection. The book shows a shell command line for the converter with a quoted options argument, then an attacker string that closes the quote with an apostrophe and chains a second, destructive command with the double-ampersand operator against the videos folder (PDF p. 187).
- Summary of the distinction: code injection is limited to an interpreter or CLI; command injection exposes the entire OS. When joining scripts and system-level commands, sanitization of the string before it reaches the host OS (Linux, Macintosh, Windows) or an interpreter (SQL, CLIs) is essential (PDF p. 187).

## When and how to apply
INTERPRETATION: when reviewing an endpoint, list every library it calls and ask whether any of them shell out to a CLI with caller-controlled values, including innocuous-looking fields such as a filename or an options string.

## Relations
Builds on SQL injection (WAS-C13-001); the host-OS version is the next section (WAS-C13-003). Defensive guidance on injection targets and whitelisting is in WAS-C25-005.

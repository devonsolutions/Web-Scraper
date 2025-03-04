# Building a Browser (Edge) Extension by Rohit Shirke

## Introduction

**Goal:** Build an extension that will allow us to quickly clear any cookies and browser cache for a website

**Why Edge?:** Edge has an extension store where you can publish the extensions free of cost

## Project Components

### manifest.json

**manifest.json:** core file that defines basic details, behavior, requested permissions, and icons for your extension

**manifest.json Details**
- **name:** name of extension, shown in app store and browser extension list
- **author:** name of author / org
- **version:** extension version number
- **manifest version:** integer specyfing version of manifest file format
- **permissions:** https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/developer-guide/api-support
- **background:** specifies the path to any service worker file we want to associate
- **action:** specifies default behavior of extension
- **icons:** specifies variety of icons used based on the system resolution
- **host permissions:** specify a pattern e.g. specific domain on which the extension will work

**background.js:** defines the script that you want to un in background (service worker) *optional

**scripts:** holds any extra script that your extension might use
s
**popup:** keeps files that extension might render

**images:** holds any images used

## originTypes

**originTypes:**
- property that allows you to specify which types of origins should be effected

chrome.browsingData.removeCache ({ originTypes: unprotectedWeb: true});
- covers websites that users visit w/o taking any special action

chrome.browsingData.removeCache ({ originTypes: });
- originTypes not specific: API defaults to removing data from unprotected web origins

chrome.browsingData.removeCache ({ originTypes: protectedWeb: true});
- covers web origins that have been installed as hosted applications
- installing Angry Birds protects the origin https://chrome.angrybirds.com and removes it from the unprotected category

## APIs

**Interface:** a set of rules for the point of interaction between two systems of components

Application Programming Interface (API): 

## Chromium

Chromium: free, open-source codebase that provides the code for Google Chrome Browser

Open-Source: software for which the original soruce code is freely available and may be redstributed and modified
- Open-Source Example: Linux OS led to Ubuntu (used in Virtual Machines)
- Close-Source Example: Adobe Reader
- distributed in direct opposition to close-source

## Miscellaneous

Markdown: markup language that formats text on web pages
- commonly used in GitHub projects

Additional Questions
- how are extensions updated?
- what is manifest?
- what does system resolution mean?
- "Action: This object specifies the default behaviour of our extension. Since we are using a seperate page for our extension we would set the default_popup property on this object with the path to the file we want to associate. (eg. popup.html). We will also set the default icon set to be used by the extenstion here."

## Sources

[Building a Browser Edge Extension by Rohit Shirke](https://rohit-shirke.medium.com/building-a-browser-edge-extension-a42d60c28137)

[API Support | Microsoft](https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/developer-guide/api-support)

[broswingdata | Chrome for Developers](https://developer.chrome.com/docs/extensions/mv2/reference/browsingData)

[What is a Web API?](https://www.geeksforgeeks.org/what-is-web-api-and-why-we-use-it/)

[Edge-dev-extension GitHub Repository by shirkerohit](https://github.com/shirkerohit/Edge-dev-extension/blob/main/popup.js)
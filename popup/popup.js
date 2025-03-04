// Flush any message on reload
clearMessage();

// Main function clear cookies
function clearCookies() {
    chrome.tabs.query
    ( {active: true, currentWindow: true}, function (tabs)
    { chrome.cookies.getAll({  url: tabs[0].url}, function (cookies) {
        for (var i = 0; i < cookies.length; i++) {
            chrome.cookies.remove({  url: tabs[0].url + cookies[i].path, name: cookies[i].name});
        }
        showMessage("Cookies cleared.");
    });
    });
}

// query: a request made by a user or application to retrive or manupulate data stored in a dataabse
// 1) chrome.tabs.query: returns list of tabs queried
// 2) filter 'active' checks if the tab is active
// 3) filter 'currentWindow' checks if we're on the current tab
//         - the entire section will return the result an array (list of tabs) and iterative over the tab array
// 4) chrome.cookies.getAll: retrives the cookies associated with the tab (site loaded in tab)
// 5) chrome.cookies.remove: specifies the URL and cookie name to be removed
// 6) showMessage: shows used a message about the result


// Main function clear cache
function clearCache() {
    chrome.tabs.query
    ( {active: true, currentWindow: true}, function (tabs)
    { chrome.browsingData.removeCache({ originTypes: {unprotectedWeb: true} }, function ()
    {
        showMessage('Cache cleared. ');
    });
    });
}

// 1) chrome.tabs.query: returns of tabs queried
// 2) filter 'active' checks if the tab is active
// 3) filter 'currentWindow' checks if we're on the current tab
// 4) chrome.browsingData.removeCache: 
// 5) originTypes: property that allows you to specficy which types of origins should be effected
// 6) unprotectedWeb: covers general case of websites that users visit w/o taking any special action

// Main function clear local and session storage

// Function to Show Message
function showMessage(message){
    if(message){
        document.getElementById('message').innerHTML = message;
    }
    else{
        clearMessage();
    }
}

// Function to Clear Message
function clearMessage() {
    document.getElementById('message').innerHMTL = " ";
}

// .innerHTML: sets or returns the HTML content of an element


// Event Listener
document.getElementById('clearCookiesBtn').addEventListener('click', clearCookies);
document.getElementById('clearCacheBtn').addEventListener('click', clearCache);
document.getElementById('clearStorageBtn').addEventListener('click', clearStorage);
document.getElementById('reloadBtn').addEventListener('click', reloadBtn);

// document.getElementByID: selects the button
// .addEventListener: a function that waits for an event to occur then responds to it

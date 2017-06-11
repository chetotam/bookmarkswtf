'use strict'
let searchbox = document.querySelector('#searchbox');
let bookmarks = document.querySelectorAll('#bookmarks-list li');
let addBookmarkButton = document.querySelector('#add-bookmark-button');
let addBookmarkForm = document.querySelector('#add-bookmark-form');
bookmarks.hide = function() {alert('hide')};

searchbox.addEventListener('keyup', (event) => {
    for (let i = 0; i < bookmarks.length; i++) {
        let bookmarkData = bookmarks[i].querySelectorAll('h2, p')
        let found = false;
        for (let j = 0; j < bookmarkData.length; j++) {
            if (bookmarkData[j].textContent.indexOf(event.target.value) >= 0 ||
                event.target.value == '') {
                found = true;
            }
        }
        if (!found) {
            bookmarks[i].setAttribute('hidden', true);
            bookmarks.hide();
        }
        else {
            bookmarks[i].removeAttribute('hidden');
        }
    }
});

addBookmarkButton.addEventListener('click', (event) => {
    addBookmarkForm.removeAttribute('hidden');
});

addBookmarkForm.submit.addEventListener('click', (event) => {
    if (addBookmarkForm.checkValidity()) {
        addBookmarkForm.setAttribute('hidden', true);
    }
});

addBookmarkForm.close.addEventListener('click', (event) => {
    addBookmarkForm.setAttribute('hidden', true);
});
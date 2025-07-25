
const titleElements = document.querySelectorAll('yt-formatted-string[title]');
titleElements.forEach(el => {
    console.log(el.getAttribute('title'));
});

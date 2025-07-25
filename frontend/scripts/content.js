function getVideoTitle() {
    const selectors = [
        'h1.ytd-watch-metadata yt-formatted-string',
        'h1.ytd-video-primary-info-renderer',
        '#title h1',
        '.ytd-watch-metadata h1',
        'h1[class*="title"]'
    ];
    
    for (const selector of selectors) {
        const titleElement = document.querySelector(selector);
        if (titleElement && titleElement.textContent.trim()) {
            return titleElement.textContent.trim();
        }
    }
    
    return null;
}

function waitForVideoTitle() {
    const title = getVideoTitle();
    if (title) {
        console.log(title);
    } else {
        setTimeout(waitForVideoTitle, 1000); 
    }
}

if (window.location.href.includes('/watch?v=')) {
    waitForVideoTitle();
}

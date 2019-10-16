setInterval(() => {
    const timeText = new Date().toLocaleDateString('ja-JP');
    document.querySelector('#currenttime').textContent = timeText;
}, 1000);
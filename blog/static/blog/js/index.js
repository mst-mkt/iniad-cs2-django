const callback = (json) => {
    const element = document.getElementById(`like${json.id}`);
    console.log(`like${json.id}`);
    element.textContent = json.like;
};

const like = (article_id) => {
    fetch(`/api/articles/${article_id}/like`)
        .then((res) => res.json())
        .then(callback);
};

import axios from 'axios';

const commentForm = document.getElementById("comment-form");
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
commentForm.addEventListener("submit", function (event) {
    axios({
        method: "POST",
        url: "articles/${event.target.dataset.articleId}/",
        headers: { "X-CSRFToken": csrftoken },
        data: new FormData(commentForm)
    })
    .then(response => {
        const comments = document.getElementById("comments");
        const 
    })
})
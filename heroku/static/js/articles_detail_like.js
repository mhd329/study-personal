import axios from 'axios';

const likeBtn = document.getElementById("like-btn");
const likeForm = document.getElementById("like-form");
const likeHeart = document.getElementById("like-heart");
const csrftoken = document.getElementById("[name=csrfmiddlewaretoken]").value;

likeForm.addEventListener("submit", function (event) {
    event.preventDefault();
    axios({
        method: 'post',
        url: "/articles/${event.target.dataset.articleId}/add-like/",
        headers: { 'X-CSRFToken': csrftoken },
        data: new FormData(likeForm)
    })
        .then(response => {
            if (response.data.isLiked === true) {
                likeBtn.classList.add("btn-danger")
                likeBtn.classList.remove("btn-outline-danger")
                likeHeart.classList.add("bi", "bi-suit-heart-fill")
                likeHeart.classList.remove("bi", "bi-suit-heart")
            } else {
                likeBtn.classList.add("btn-outline-danger")
                likeBtn.classList.remove("btn-danger")
                likeHeart.classList.add("bi", "bi-suit-heart")
                likeHeart.classList.remove("bi", "bi-suit-heart-fill")
            }
            const likeCount = document.getElementById("like-count")
            likeCount.innerText = response.data.likeCount
        });
});
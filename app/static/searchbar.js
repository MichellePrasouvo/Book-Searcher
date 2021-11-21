const f = document.getElementById('form');
const q = document.getElementById('query');
const google = 'https://www.google.com/search?q=site%3A+';
const site = 'pagedart.com';

function submitted(event) {
    event.preventDefault();
    book_name = q.value
    newurl = "https://findabook.herokuapp.com/search?name=" + book_name
        // fetch(newurl)
        //     .then(response => response.json())
        //     .then(data => console.log(data));
    window.open(newurl);

}

f.addEventListener('submit', submitted);
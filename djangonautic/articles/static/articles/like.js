const addLike = async (btn_id) => {
    const response = await fetch(`/articles/like/${btn_id}`);
    const json = await response.json();
    return json;
  }
  const articles = document.querySelector('.articles');
  articles.addEventListener('click', (e) => {
    if (e.target.tagName == 'BUTTON') {
      btn_id = parseInt(e.target.getAttribute('id'));
      btn_class = e.target.getAttribute('class');
      like_count = document.querySelector(`#span${btn_id}`);

      if (btn_class == 'Like') {
        e.target.innerHTML = '<i class="fas fa-heart"></i>  Liked';
        e.target.setAttribute('class', 'Liked');
      }

      else if (btn_class == 'Liked') {
        e.target.innerHTML = '<i class="fas fa-heart"></i>  Like';
        e.target.setAttribute('class', 'Like');
      }
      addLike(btn_id)
        .then(data => {
          like_count.textContent = data.likes;
          console.log('works');
        })
        .catch(err => {
          console.log(err);
        })
    }
  });
  
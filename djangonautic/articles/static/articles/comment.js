commentBlock=document.querySelector('.comments');

comment_form=document.querySelector('#comment-form');
comment_form.addEventListener('submit',(e)=>{
  e.preventDefault();
  new_comment=comment_form['comment'].value;
  fetch(`/articles/add_comment/${post_id}/${new_comment}/`)
  .then((data)=>{
    comment_form['comment'].value='';
    commentBlock.innerHTML+=`<p id="scrolltome"><b>${username}: </b> ${new_comment}</p>`;
    new_comment=document.querySelector('#scrolltome');
    new_comment.scrollIntoView();
  })

});

function deleteLetters(title) {
    if(document.cookie.split('=')[1]){
        $.ajax({
            type: 'POST',
            url: '/api/delete',
            data: {title_give: title},
            success: function (response) {
                alert(response['msg']);
                window.location.reload()
            }
        });
    }else{
        alert('로그인을 해주세요')
    }
    
}


function comment_insert(title,e) {
    
    const comment = e.previousElementSibling.value;
    
     if(document.cookie.split('=')[1]){
        $.ajax({
            type: 'POST',
            url: '/index/comment',
            data: {title, comment},
            success: function (response) {
                alert(response['msg']);
                window.location.reload()
            }
        });
    }else{
        alert('로그인을 해주세요')
    } 

}

function likeLetter(title, isLike){
    if(document.cookie.split('=')[1]){
        $.ajax({
            type: 'POST',
            url: '/api/like',
            data: {title, isLike},
            success: function (response) {
                alert(response['msg']);
                window.location.reload()
            }
        });
    }else{
        alert('로그인을 해주세요')
    }
}
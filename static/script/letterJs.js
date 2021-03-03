

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


function comment_insert(comment) {
    //뉴스레터제목을 가져오고있음
    console.log(comment)
    if(document.cookie.split('=')[1]){
        $.ajax({
            type: 'POST',
            url: '/api/comment',
            data: {comment_give: comment},
            success: function (response) {
                alert(response['msg']);
                window.location.reload()
            }
        });
    }else{
        alert('로그인을 해주세요')
    }

}
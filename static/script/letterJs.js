function deleteLetters(title) {
    $.ajax({
        type: 'POST',
        url: '/api/delete',
        data: {title_give: title},
        success: function (response) {
            alert(response['msg']);
            window.location.reload()
        }
    });
}




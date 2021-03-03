function new_newsletter() {
    let search_box = $('#search_insert')
    if (search_box.css("display") === "block") {
        search_box.hide();
    } else {
        search_box.show();
    }
}

function insert_newsletter() {
    let url = $('#letter-url').val()
    let title = $('#letter-title').val()
    let desc = $('#letter-desc').val()
    let category = $('#letter-category').val()

    $.ajax({
        type: "POST",
        url: "/index/insert",
        data: {
            title_give: title,
            category_give: category,
            url_give: url,
            desc_give: desc
        },
        success: function (response) { // 성공하면
            alert(response['msg']);
            window.location.reload()
        }
    })
}



//뉴스레터 추가버튼 클릭시
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
    console.log(url)

    $.ajax({
        type: "POST",
        url: "/index/insert",
        data: {url_give: url, title_give: title, desc_give: desc, category_give: category},
        success: function (response) { // 성공하면
            alert(response['msg']);
            window.location.reload();
        }
    })
}




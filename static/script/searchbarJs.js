//뉴스레터 추가버튼 클릭시
function new_newsletter() {
    let search_box = $('#search_insert')
    if (search_box.css("display") === "block") {
        search_box.hide();
    } else {
        search_box.show();
    }
}


//뉴스레터 추가 insert
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


//검색
function search_newsletter() {
      $.ajax({
          type: 'GET',
          url: '/index/search',
          data: {},
          success: function (response) {
              alert(response['msg']);
          }
      });
  }
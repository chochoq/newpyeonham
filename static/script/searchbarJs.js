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


/* function search_newsletter(){
    const keyword = $('#input-newsletter').val();
    

    const result = newslettersjson.filter(news=>
        news.title.includes(keyword))

    console.log('result',result)
} */

for (let i = 0; i < newsletter_list.length; i++) {                
    let letter = newsletter_list[i];
    
    if (letter.includes(newsletterVal)) {
        console.log('맞음',newsletter_list[i])
    } else {
        console.log(letter, newsletterVal)
        //console.log("없는 뉴스레터입니다 추가해주세요")
    }
}
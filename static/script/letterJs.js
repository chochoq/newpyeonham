 $(document).ready(function () {
            showLetter();
        });
        function showLetter() {
            $.ajax({
                type: "GET",
                url: "/memo",
                data: {},
                success: function (response) {
                    let letter = response['all_letters']
                    for (let i = 0; i < letter.length; i++) {
                        let title = letters[i]['title']
                        let image = letters[i]['image']
                        let url = letters[i]['url']
                        let desc = letters[i]['desc']


                        temp_html = `<div class="letter">
                    <img class="letter-img-top"
                         src="${image}"
                         alt="letter image cap">
                    <div class="leteer_body">
                        <a target="_blank" href="${url}" class="letter-title">${title}</a>
                        <p class="letter-text">${desc}</p>
                        <p class="letter-text comment">${comment}</p>
                    </div>
                </div>`
                        $('#cards-box').append(temp_html)
                    }
                }
            })
        }

        function deleteLetter(title) {
            $.ajax({
                type: 'post',
                url: '/api/delete',
                data: {title_give:title},
                success: function(response){
                    alert(response['msg']);
                    window.location.reload()
                }
            });
        }





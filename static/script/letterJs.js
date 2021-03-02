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
                        let title = articles[i]['title']
                        let image = articles[i]['image']
                        let url = articles[i]['url']
                        let desc = articles[i]['desc']


                        temp_html = `<div class="letter">
                    <img class="letter-img-top"
                         src="${image}"
                         alt="letter image cap">
                    <div class="leteer_body">
                        <a target="_blank" href="${url}" class="letter-title">${title}</a>
                        <p class="letter-text">${desc}</p>
                       </div>
                </div>`
                        $('#letter-box').append(temp_html)
                    }
                }
            })
        }



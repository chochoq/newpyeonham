function new_newsletter(){
    let search_box =$('#search_insert')
    if (search_box.css("display") === "block"){
        search_box.hide();
    }else {
        search_box.show();
    }
}
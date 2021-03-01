const signup_btn = document.querySelector('.signup_btn');
const login_btn = document.querySelector('.login_btn');
const signup_section = document.querySelector('.signup_section');
const login_section = document.querySelector('.login_section');

const toggle_login_show = ()=>{
    login_section.classList.toggle('show');
}

const toggle_signup_show = ()=>{
    signup_section.classList.toggle('show');
}

signup_btn.addEventListener('click',()=>{
    if(login_section.classList.contains('show')){
        toggle_login_show();
    }       
    toggle_signup_show();    
})

login_btn.addEventListener('click',()=>{    
    if(signup_section.classList.contains('show')){
        toggle_signup_show();
    }       
    toggle_login_show();
})
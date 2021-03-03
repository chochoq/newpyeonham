const open_signup_btn = document.querySelector('.open_signup_btn');
const open_login_btn = document.querySelector('.open_login_btn');
const signup_section = document.querySelector('.signup_section');
const login_section = document.querySelector('.login_section');
const login_email_input = document.querySelector('.login_email_input');
const login_pw_input = document.querySelector('.login_pw_input');

const login_btn = document.querySelector('.login_btn');


const toggle_login_show = ()=>{
    login_section.classList.toggle('show');
}

const toggle_signup_show = ()=>{
    signup_section.classList.toggle('show');
}

open_signup_btn.addEventListener('click',()=>{
    if(login_section.classList.contains('show')){
        toggle_login_show();
    }       
    toggle_signup_show();    
})

open_login_btn.addEventListener('click',()=>{    
    if(signup_section.classList.contains('show')){
        toggle_signup_show();
    }       
    toggle_login_show();
})

// 회원가입 기능
const onSignup = ()=>{
    const name = $('#myname').val();
    const email = $('#email').val();
    const password = $('#password').val();
    const password_check = $('#password_check').val();

    $.ajax({
        type: "POST",
        url: "/index/signup",
        data: {
            name,
            email,
            password
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert('회원가입이 완료되었습니다.')
                clearSignupComponent();
            } else {
                alert(response['msg'])
            }
        }
    })
}

const clearSignupComponent = ()=>{
    const name = $('#myname').val('');
    const email = $('#email').val('');
    const password = $('#password').val('');
    const password_check = $('#password_check').val('');
}

// 로그인 기능
login_btn.addEventListener('click',()=>{
    onLogin()
})

const onLogin = ()=>{
    const email = login_email_input.value;
    const password = login_pw_input.value;
    
    console.log(email, password)
}

const insertData = ()=>{
    console.log('dd')
    $.ajax({
        type: "POST",
        url: "/index/insertSample",
        data: {
            name:'gg'
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert('데이터 넣음')
                //clearSignupComponent();
            } else {
                alert(response['msg'])
            }
        }
    })
}
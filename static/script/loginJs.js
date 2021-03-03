

const open_signup_btn = document.querySelector('.open_signup_btn');
const open_login_btn = document.querySelector('.open_login_btn');
const logout_btn = document.querySelector('.logout_btn');
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
    
    // ['쿠키'라는 개념에 대해 알아봅시다]
    // 로그인을 구현하면, 반드시 쿠키라는 개념을 사용합니다.
    // 페이지에 관계없이 브라우저에 임시로 저장되는 정보입니다. 키:밸류 형태(딕셔너리 형태)로 저장됩니다.
    // 쿠키가 있기 때문에, 한번 로그인하면 네이버에서 다시 로그인할 필요가 없는 것입니다.
    // 브라우저를 닫으면 자동 삭제되게 하거나, 일정 시간이 지나면 삭제되게 할 수 있습니다.
    
    $.ajax({
        type: "POST",
        url: "/index/login",
        data: {
            email, password
        },
        success: function (response) {
            if (response['result'] == 'success') {
                // 로그인이 정상적으로 되면, 토큰을 받아옵니다.
                // 이 토큰을 mytoken이라는 키 값으로 쿠키에 저장합니다.
                
                document.cookie =  `mytoken=${response['token']}`
                
                alert('로그인 완료!')

            } else {
                // 로그인이 안되면 에러메시지를 띄웁니다.
                alert(response['msg'])
            }
        }
    })
}

// 로그아웃
logout_btn.addEventListener('click',e=>{
    document.cookie = 'token=';
})

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


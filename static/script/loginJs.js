const open_signup_btn = document.querySelector('.open_signup_btn');
const open_login_btn = document.querySelector('.open_login_btn');
const signup_section = document.querySelector('.signup_section');
const login_section = document.querySelector('.login_section');
const login_email_input = document.querySelector('.login_email_input');
const login_pw_input = document.querySelector('.login_pw_input');
const login_btn = document.querySelector('.login_btn');
const logout_btn = document.querySelector('.logout_btn');
const user_component = document.querySelectorAll('.user_component');
const open_btn = document.querySelectorAll('.open_btn');
// 로그인 확인

const paintButton = (isLogin)=>{
    if(isLogin){
        open_btn.forEach(b=>{
            b.classList.add('login');
        })
        
        user_component.forEach(b=>{
            b.classList.add('login');
        })
        
    }else{
        open_btn.forEach(b=>{
            b.classList.remove('login');
        })
        
        user_component.forEach(b=>{
            b.classList.remove('login');
        })
    }    
}



const checkLoginStatus = ()=>{    
    
    if(!status){    
        paintButton(false);
    }else if(status==="expire"){
        alert('로그인 토큰이 만료되었습니다')
        paintButton(false);
    }else{        
        paintButton(true);
    }    
}


checkLoginStatus();


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
    
    const user = {
        name, email, password
    }

    if(!(name && email && password && password_check)){
        alert('모든 정보를 입력해주세요');
        return;
    }

    if(checkEmail(email) && checkPassword(password, password_check)){
        createUser(user)
    }    
}

const createUser = (user)=>{
    
    $.ajax({
        type: "POST",
        url: "/index/signup",
        data: user,
        success: function (response) {
            if (response['result'] == 'success') {
                alert('회원가입이 완료되었습니다.')
                clearSignupComponent();
                toggle_signup_show();
                toggle_login_show();
            } else {
                alert(response['msg'])
            }
        }
    })
}


const checkEmail = (inputEmail)=>{
    var emailRule = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;//이메일 정규식
 
    if(!emailRule.test(inputEmail)) {                        
        alert('이메일 형식이 아닙니다')
        return false;
    }
    
    return true;
}

const checkPassword = (inputPw, inputPwChk)=>{
    if(inputPw != inputPwChk){
        alert('비밀번호가 다릅니다')
        return false;
    }
    return true;
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
    
    const user = {
        email, password
    }
    if(!(email && password)){
        alert('모든 정보를 입력해주세요')
        return;
    }

    getUser(user);
}
const getUser = (user)=>{
    $.ajax({
        type: "POST",
        url: "/index/login",
        data: user,
        success: function (response) {
            if (response['result'] == 'success') {
               
                document.cookie =  `mytoken=${response['token']}`                                
                location.reload();

            } else {                
                alert(response['msg'])
            }
        }
    })
}
// 로그아웃
logout_btn.addEventListener('click',e=>{    
    document.cookie = 'mytoken=';    
    location.reload();    
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


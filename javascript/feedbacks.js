

const btn = document.querySelector('.button');
const userName = document.querySelector('#name');
const userEmail = document.querySelector('#email');
const hiddenDiv = document.querySelector('.hidden-div');


btn.addEventListener('click', btnClicked);




function btnClicked(e){
    e.preventDefault();
    
    if (userName.value === '' || userEmail.value === ''){
        hiddenDiv.innerHTML = "<h2> Please fill out all the credentials! </h2>";
        setTimeout(() => hiddenDiv.remove(), 5000);
        

    }
    else{
        hiddenDiv.innerText = `Thank You   ${userName.value}. We will reach you via your email : ${userEmail.value}`;
        setTimeout(() => hiddenDiv.remove(), 5000);
    }

    //Clearing the fields
    userName.value = '';
    userEmail.value = '';
    
}
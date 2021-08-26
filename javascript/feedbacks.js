

const btn = document.querySelector('.button');
const userName = document.querySelector('#name');
const userEmail = document.querySelector('#email');

btn.addEventListener('click', feedbackGiven);




function feedbackGiven(e){
    e.preventDefault();
    console.log("Name :", userName.value);
    console.log("Email :", userEmail.value);
}
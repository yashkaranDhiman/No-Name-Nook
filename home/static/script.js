let welcomeModel = document.getElementById("welcome-model");
let continueBtn = document.getElementById("continue-btn");
let roomModel= document.getElementById("add-room-model");
// let addRoomBtn = document.getElementById("add-room");
let close = document.getElementById("close");

function welcome(){
    if(localStorage.getItem("NoNameNook") == null){
        setTimeout(function(){
            welcomeModel.style.scale = "1";
        },500)
    }   
    continueBtn.addEventListener("click",()=>{
        localStorage.setItem("NoNameNook","member")
        welcomeModel.style.scale = "0";
    })
}

// addRoomBtn.addEventListener("click",()=>{
//     roomModel.style.display = "block";
// })
// close.addEventListener("click",()=>{
//     roomModel.style.display = "none";
// })


welcome()
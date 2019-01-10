let socket = io('http://' + window.document.location.host)
let identity = "guest";

let bullets = [];
for (let i = 0; i< 6; i++){
    bullets.push({color:"black",location:[620+i*20,580],speed:[0,0],owner:null,status:"waiting"})
}

// speed multiplier
const sm=0.05;

let launchLine = false;
let canShoot = false;
const r = 10;//radius
const canvas = document.getElementById('canvas');
const context = canvas.getContext("2d");
const userName = document.getElementById("userNameInput")
const password = document.getElementById("passwordInput")

// the coordinates of mouse clicked on canvas
let canvasX, canvasY

// the bounding of canvas
let rect = canvas.getBoundingClientRect()

let returnObj={};
let returnJSON;

function logIn(){
    returnObj={};
    returnObj.userName = userName.value;
    returnObj.password = password.value;
    userName.value = '';
    password.value = '';
    returnJSON = JSON.stringify(returnObj);
    socket.emit("logIn",returnJSON);
}

socket.on("logIn",function (data){
    data = JSON.parse(data);
    if(data.result === "succeed"){
        identity = data.identity;
        document.getElementById("userName").innerHTML += identity;
        document.getElementById("userNameInput").style.visibility = "hidden";
        document.getElementById("password").style.visibility = "hidden";
        document.getElementById("passwordInput").style.visibility = "hidden";
        document.getElementById("logOut").style.visibility = "visible";
        document.getElementById("restart").style.visibility = "visible";
        document.getElementById("logIn").style.visibility = "hidden";
        document.getElementById("signUp").style.visibility = "hidden";
        document.getElementById("logOut").disabled= false;
        document.getElementById("restart").disabled= false;
    }else{
        window.alert(data.message);
    }
})

function logOut(){
    returnObj={};
    returnObj.identity = identity;
    returnJSON = JSON.stringify(returnObj);
    socket.emit("logOut",returnJSON);
}

socket.on("logOut",function (data){
    data = JSON.parse(data);
    if(data.result === "succeed"){
        let index = document.getElementById("userName").innerHTML.indexOf(identity);
        let newStr = document.getElementById("userName").innerHTML.substring(0,index);
        document.getElementById("userName").innerHTML = newStr;
        document.getElementById("userNameInput").style.visibility = "visible";
        document.getElementById("password").style.visibility = "visible";
        document.getElementById("passwordInput").style.visibility = "visible";
        document.getElementById("logOut").style.visibility = "hidden";
        document.getElementById("restart").style.visibility = "hidden";
        document.getElementById("logIn").style.visibility = "visible";
        document.getElementById("signUp").style.visibility = "visible";
        document.getElementById("logOut").disabled= true;
        document.getElementById("restart").disabled= true;
        canShoot = false;
        identity = data.identity;
    }
})

function signUp(){
    returnObj={};
    returnObj.userName = userName.value;
    returnObj.password = password.value;
    userName.value = '';
    password.value = '';
    returnJSON = JSON.stringify(returnObj);
    socket.emit("signUp",returnJSON);
}

socket.on("signUp",function (data){
    data = JSON.parse(data);
    if(data.result === "succeed"){
        window.alert("Success!");
    }else{
        window.alert(data.message);
    }
})

socket.on("updateUsers",function (data) {
    data = JSON.parse(data);
    let player1Name = document.getElementById("player1Name");
    let player2Name = document.getElementById("player2Name");
    let player1Graph = document.getElementById("player1Graph");
    let player2Graph = document.getElementById("player2Graph");
    let viewerCounter = document.getElementById("viewerCounter")

    player1Name.innerHTML = "Waiting";
    player2Name.innerHTML = "Waiting";
    player1Name.style.color = "black";
    player2Name.style.color = "black";
    player1Graph.style.background = "black";
    player2Graph.style.background = "black";

    switch (data.players.length) {
        case 2:
            player2Name.innerHTML = data.players[1];
            player2Name.style.color = "red";
            player2Graph.style.background = "red";
        case 1:
            player1Name.innerHTML = data.players[0];
            player1Name.style.color = "yellow";
            player1Graph.style.background = "yellow"
    }

    viewerCounter.innerHTML = data.viewers;
})


function firm1() {
    if(window.confirm("Do you want to restart the game? \nYour playmate will recieve a message about you requirement.")){
        returnObj = {};
        returnObj.identity = identity;
        returnJSON = JSON.stringify(returnObj);
        socket.emit("requireForRestart",returnJSON);
    }
}
function restart(){
    firm1();

}


function firm2() {
    if(window.confirm("Your playmate want to restart the game.\nDo you agree with that?")){
        returnObj = {};
        returnObj.identity = identity;
        returnJSON = JSON.stringify(returnObj);
        socket.emit("agreeToRestart",returnJSON);
    }
}
socket.on("requireForRestart",function (data){
    console.log("require for restart: ",data);
    data = JSON.parse(data);
    if (data.identity !== identity && identity !== "guest"){
        firm2();
    }
})

socket.on("waitToShoot",function (data) {
    launchLine = true;
    data = JSON.parse(data);
    console.log("wait to shoot = "+data)
    if(data === identity){
        document.addEventListener('mousedown',handleMouseDown);
        canShoot = true;
    }
});

socket.on("waitToStop",()=>{
    launchLine = false;
    canShoot = false;
})


socket.on("updateBullets",(data)=>{
    bullets = JSON.parse(data);
    drawCanvas();
})

function drawCanvas() {
    context.fillStyle = 'white';
    context.fillRect(0, 0, canvas.width, canvas.height)
    drawBackground();
    drawBullets();
    if(launchLine) drawLine();
}


function drawBackground() {
    context.beginPath()
    context.fillStyle = "blue";
    context.arc(700,100,80,0,2*Math.PI);
    context.fill();

    context.beginPath()
    context.fillStyle = "white";
    context.arc(700,100,60,0,2*Math.PI);
    context.fill();

    context.beginPath()
    context.fillStyle = "red";
    context.arc(700,100,40,0,2*Math.PI);
    context.fill();

    context.beginPath()
    context.fillStyle = "white";
    context.arc(700,100,20,0,2*Math.PI);
    context.fill();

    context.beginPath()
    context.fillStyle = "blue";
    context.arc(300,300,240,0,2*Math.PI);
    context.fill();

    context.beginPath()
    context.fillStyle = "white";
    context.arc(300,300,180,0,2*Math.PI);
    context.fill();

    context.beginPath()
    context.fillStyle = "red";
    context.arc(300,300,120,0,2*Math.PI);
    context.fill();

    context.beginPath()
    context.fillStyle = "white";
    context.arc(300,300,60,0,2*Math.PI);
    context.fill();

    context.strokeStyle = "black";
    context.lineWidth = 2;
    context.beginPath();
    context.moveTo(600,0);
    context.lineTo(600,600);
    context.closePath();
    context.stroke();
}


function drawLine() {
    var x1=600;
    var x2=800;
    var y1=y2=500;
    var x=y=0
    for(let bullet of bullets){
        if(bullet.status === "preparing"){
            x=bullet.location[0];
            y=bullet.location[1];
            break;
        }
    }
    if(x != 0 && y != 0){
        let distance = Math.sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1));
        let a = Math.asin(r/distance);
        let b = Math.atan((y-y1)/(x-x1))
        let degree1 = a+b;
        let degree2 = Math.PI/4-degree1
        let xd1 = x-Math.sin(degree1)*r;
        let yd1 = y+Math.cos(degree1)*r;
        let xd2 = x+Math.sin(degree2)*r;
        let yd2 = y+Math.cos(degree2)*r;
        context.strokeStyle = "black";
        context.lineWidth = 2;
        context.beginPath();
        context.moveTo(x1,y1);
        context.lineTo(xd1,yd1);
        context.moveTo(x2,y2);
        context.lineTo(xd2,yd2);
        context.closePath();
        context.stroke();
    }
}

function drawBullets(){
    for(let bullet of bullets){
        context.beginPath();
        context.strokeStyle = "black";
        context.fillStyle = "#778899";
        context.arc(bullet.location[0],bullet.location[1],r,0,2*Math.PI)
        context.fill();
        context.stroke();

        context.beginPath();
        context.fillStyle = bullet.color;
        context.arc(bullet.location[0],bullet.location[1],r/2,0,2*Math.PI)
        context.fill();


        context.beginPath();
        context.strokeStyle = "black";
        context.fillStyle = "#778899";
        context.arc((bullet.location[0]-600)*3,bullet.location[1]*3,r*3,0,2*Math.PI)
        context.fill();
        context.stroke();

        context.beginPath();
        context.fillStyle = bullet.color;
        context.arc((bullet.location[0]-600)*3,bullet.location[1]*3,r*3/2,0,2*Math.PI)
        context.fill();

    }
}

function checkClick(x,y) {
    if(700-10<=x && x<=700+10 && 500-10<=y && y<=500+10){
        return true;
    }
    return false;
}

function handleMouseDown(e){
    canvasX = e.clientX - rect.left;
    canvasY = e.clientY - rect.top;
    if(canShoot && checkClick(canvasX,canvasY)){
        canvas.addEventListener('mouseup',handleMouseUp)
        canvas.addEventListener('mousemove',handleMouseMove)
    }
}
function handleMouseMove(e){
    returnObj = {};
    let dx,dy;
    dx = e.clientX - rect.left - canvasX;
    dy = e.clientY - rect.top - canvasY;
    if (dy <0) dy = 0;
    if (dx*dx+dy*dy > 1600){
        dx = dx*Math.sqrt(1600/(dx*dx+dy*dy))
        dy = dy*Math.sqrt(1600/(dx*dx+dy*dy))
    }
    for(let bullet of bullets){
        if (bullet.status === "preparing"){
            bullet.location[0] = dx + canvasX;
            bullet.location[1] = dy + canvasY;
            returnObj.location = bullet.location;
            break;
        }
    }

    returnJSON = JSON.stringify(returnObj);
    socket.emit("dragBullet",returnJSON);
    e.stopPropagation()
}
function handleMouseUp(e){

    returnObj = {};
    for(let bullet of bullets){
        if (bullet.status === "preparing"){
            returnObj.location = bullet.location;
            returnObj.speed = [0,0];
            returnObj.speed[0] = (canvasX - bullet.location[0])*sm;
            returnObj.speed[1] = (canvasY - bullet.location[1])*sm;
            break;
        }
    }
    canvas.removeEventListener("mousemove",handleMouseMove);
    canvas.removeEventListener("mouseup",handleMouseUp)
    returnJSON = JSON.stringify(returnObj);
    socket.emit("shootBullet",returnJSON);
    e.stopPropagation()
}

document.addEventListener('DOMContentLoaded', () =>{
    drawCanvas();
})
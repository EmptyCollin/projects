const app = require("http").createServer(handler) // create server
app.listen(3000); // listen to 3000 port
const fs = require("fs"); //
const io = require("socket.io")(app);
const url = require("url"); //to parse url strings
const ROOT_DIR = "html";

const MIME_TYPES = {
    css: "text/css",
    gif: "image/gif",
    htm: "text/html",
    html: "text/html",
    ico: "image/x-icon",
    jpeg: "image/jpeg",
    jpg: "image/jpeg",
    js: "application/javascript",
    json: "application/json",
    png: "image/png",
    svg: "image/svg+xml",
    txt: "text/plain"
};

// hard-code the primary user list
let userList = {
    Arbor:"123",
    Bob:"456",
    Cate:"789"
};

let  isPlaying = false;

// the players in the game
let players = [];

// socketId - playerName
let playersSocketId = {};

// the number of audience
let viewer = 0;

// the list of stones have not been shot
let bullets = [];
reset();
// friction coefficient
const fc = 0.003;

// radius of each bullet
const r = 10;

// used for control the times of sending message
let postInform = true;

// reset the table
function reset() {
    bullets = [];
    for (let i = 0; i< 6; i++){
        bullets.push({color:"black",location:[620+i*20,580],speed:[0,0],owner:null,status:"waiting"})
    }
}

// when player joins the game, distributing the bullets to them
function distributeBullets() {
    let counter = 0;
    for(let player of players){
        for(let i = 0; i < 3; i++){
            if (counter < 3){
                bullets[counter].color = "yellow";
            }else{
                bullets[counter].color = "red";
            }
            bullets[counter].owner = player;
            counter++;
        }
    }

}

function updateUser() {
    let returnObj = {};
    returnObj.players = players;
    returnObj.viewers = viewer;
    io.emit("updateUsers",JSON.stringify(returnObj));
}

// ready to shot, put a bullet onto the place of launching
function readToShot(player) {
    for(let i = 0 ; i < bullets.length; i++){
        if (bullets[i].owner === player && bullets[i].status !== "shot"){
            bullets[i].location[0] = 700;
            bullets[i].location[1] = 500;
            bullets[i].status = "preparing";
            break;
        }
    }
}

function shotBullet(bullet,location,speed) {
    bullet.location[0] = location[0];
    bullet.location[1] = location[1];
    bullet.speed[0] = speed[0];
    bullet.speed[1] = speed[1];
    bullet.status = "shot";
}

function refreshTable() {
    for (let bullet of bullets){
        if (bullet.status === "waiting"){
            continue;
        }
        // check the interact with other bullets
        for(let anotherBullet of bullets){
            if (anotherBullet.status === "waiting" || anotherBullet == bullet){
                continue;
            }
            let distancePower2 = (Math.pow(bullet.location[0]-anotherBullet.location[0],2)
                               +  Math.pow(bullet.location[1]-anotherBullet.location[1],2));
            if (distancePower2 <= 4*r*r){
                interact(bullet,anotherBullet);
            }
        }

        // move the bullet and reduce speed
        bullet.location[0] += bullet.speed[0];
        bullet.location[1] += bullet.speed[1];
        if (Math.abs(bullet.speed[0])<=fc){
            bullet.speed[0] = 0;
        }else if (bullet.speed[0] > 0){
            bullet.speed[0] -= fc;
        }else if (bullet.speed[0] < 0){
            bullet.speed[0] += fc;
        }
        if (Math.abs(bullet.speed[1])<=fc){
            bullet.speed[1] = 0;
        }else if (bullet.speed[1] > 0){
            bullet.speed[1] -= fc;
        }else if (bullet.speed[1] < 0){
            bullet.speed[1] += fc;
        }


        // check the rebound on edges
        if (bullet.location[0]+r>=800 || bullet.location[0]-r<=600){
            bullet.speed[0] = -1* bullet.speed[0];
        }
        if (bullet.location[1]+r>=600 || bullet.location[1]-r<=0){
            bullet.speed[1] = -1* bullet.speed[1];
        }
    }
}

function interact(bullet,anotherBullet){
    /*
    let V1 = Math.sqrt(bullet.speed[0] * bullet.speed[0] + bullet.speed[1] * bullet.speed[1]);
    let V2 = Math.sqrt(anotherBullet.speed[0] * anotherBullet.speed[0] + anotherBullet.speed[1] * anotherBullet.speed[1]);
    let a, b, c, p, q, d;
    let U1, U2;
    if(V1 === 0 && V2 === 0){
        return;
    }else if(V1 === 0){
        p = Math.asin((bullet.location[1]-anotherBullet.location[1])/(2*r)) ;
        d = Math.asin(anotherBullet.speed[0]/V2);
        a = Math.PI/2 - p -d;
        U1 = V2*Math.sin(a)*Math.sin(a);
        U2 = V2*Math.cos(a)*Math.cos(a);
        c = p-a;
        anotherBullet.speed[0] = U1 * Math.cos(c);
        anotherBullet.speed[1] = U1 * Math.sin(c);
        bullet.speed[0] = U2 * Math.cos(p);
        bullet.speed[1] = U2 * Math.sin(p);

    }else if(V2 === 0) {
        p = Math.asin((anotherBullet.location[1] - bullet.location[1]) /(2*r));
        d = Math.asin(bullet.speed[0] / V1);
        a = Math.PI / 2 - p - d;
        U1 = V1*Math.sin(a)*Math.sin(a);
        U2 = V1*Math.cos(a)*Math.cos(a);
        c = p - a;
        bullet.speed[0] = U1 * Math.cos(c);
        bullet.speed[1] = U1 * Math.sin(c);
        anotherBullet.speed[0] = U2 * Math.cos(p);
        anotherBullet.speed[1] = U2 * Math.sin(p);
    }else{
        p = Math.asin((anotherBullet.location[1] - bullet.location[1]) / (2 * r));
        d = Math.asin(bullet.speed[0]/V1);
        a = Math.PI / 2 - p - d;
        q = Math.asin((bullet.location[1] - anotherBullet.location[1]) / (2 * r));
        d = Math.asin(anotherBullet.speed[0]/V2)
        b = Math.PI / 2 - q - d;
        U1 = V1 * Math.sin(a) + V2 * Math.cos(b);
        U2 = V2 * Math.sin(b) + V1 * Math.cos(a);

        bullet.speed[0] = U1 * Math.cos(p-a);
        bullet.speed[1] = U1 * Math.sin(p-a);
        anotherBullet.speed[0] = U2 * Math.cos(q-b);
        anotherBullet.speed[1] = U2 * Math.sin(q-b);
    }*/

    let theta1 = Math.atan2(bullet.speed[1],bullet.speed[0]);
    let theta2 = Math.atan2(anotherBullet.speed[1],anotherBullet.speed[0]);
    let phi = Math.atan2(anotherBullet.location[1] - bullet.location[1],anotherBullet.location[0] - bullet.location[0]);
    let v1 = Math.sqrt(Math.pow(bullet.speed[0],2)+Math.pow(bullet.speed[1],2));
    let v2 = Math.sqrt(Math.pow(anotherBullet.speed[0],2)+Math.pow(anotherBullet.speed[1],2));
    let m1=m2=1;

    bullet.speed[0] = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.cos(phi) + v1*Math.sin(theta1-phi) * Math.cos(phi+Math.PI/2);
    bullet.speed[1] = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.sin(phi) + v1*Math.sin(theta1-phi) * Math.sin(phi+Math.PI/2);
    anotherBullet.speed[0] = (v2 * Math.cos(theta2 - phi) * (m2-m1) + 2*m1*v1*Math.cos(theta1 - phi)) / (m1+m2) * Math.cos(phi) + v2*Math.sin(theta2-phi) * Math.cos(phi+Math.PI/2);
    anotherBullet.speed[1] = (v2 * Math.cos(theta2 - phi) * (m2-m1) + 2*m1*v1*Math.cos(theta1 - phi)) / (m1+m2) * Math.sin(phi) + v2*Math.sin(theta2-phi) * Math.sin(phi+Math.PI/2);
/*
    bullet.location[0] += bullet.speed[0];
    bullet.location[1] += bullet.speed[1];
    anotherBullet.location[0] += anotherBullet.speed[0];
    anotherBullet.location[1] += anotherBullet.speed[1];
*/}

function bulletsNotShot() {
    let counter =0;
    for (let bullet of bullets){
        if (bullet.status != "shot"){counter++;}
    }
    return counter;
}

function bulletsStopped() {
    for (let bullet of bullets){
        if (bullet.speed[0] != 0 || bullet.speed[1] != 0){return false;}
    }
    return true;
}

function get_mime(filename) {
    for (let ext in MIME_TYPES) {
        if (filename.indexOf(ext, filename.length - ext.length) !== -1) {
            return MIME_TYPES[ext]
        }
    }
    return MIME_TYPES['txt']
}

function  playerHasLogged(name){
    for(let player of players){
        if (player === name){
            return true;
        }
    }
    return false;
}

function handler(request, response) {
    let urlObj = url.parse(request.url, true, false)
    console.log('\n============================')
    console.log("PATHNAME: " + urlObj.pathname)
    console.log("REQUEST: " + ROOT_DIR + urlObj.pathname)
    console.log("METHOD: " + request.method)

    let filePath = ROOT_DIR + urlObj.pathname
    if (urlObj.pathname === '/') filePath = ROOT_DIR + '/Assignment3.html'

    fs.readFile(filePath, function(err, data) {
        if (err) {
            //report error to console
            console.log('ERROR: ' + JSON.stringify(err))
            //respond with not found 404 to client
            response.writeHead(404);
            response.end(JSON.stringify(err))
            return;
        }
        response.writeHead(200, {
            'Content-Type': get_mime(filePath)
        });
        response.end(data);
    })

}

io.on('connection', function(socket) {
    viewer++;
    updateUser();
    io.emit('updateBullets', JSON.stringify(bullets));
    let returnObj = {};
    let returnJSON;
    let bulletsJSON;
    socket.on('logIn', function (data) {
        returnObj = {};
        data = JSON.parse(data);
        returnObj.result = 'failed';
        returnObj.message = '';
        returnObj.identity = 'guest';
        if (players.length >= 2) {
            returnObj.message = 'There are already two players!';
        } else if (playerHasLogged(data.userName)) {
            returnObj.message = "This player has already logged in!";
        } else if (data.userName in userList && data.password === userList[data.userName]) {
            returnObj.result = 'succeed';
            viewer--;
            players.push(data.userName);
            let socketId = socket.id;
            playersSocketId.socketId = data.userName;
            updateUser();
            reset();
            distributeBullets();
            returnObj.identity = data.userName;
            if (players.length === 2) {
                isPlaying = true;
                postInform = true;
            }
        } else {
            returnObj.message = 'Incorrect Information! Please recheck or register!';
        }
        returnJSON = JSON.stringify(returnObj);
        socket.emit("logIn", returnJSON);
        io.emit('updateBullets', JSON.stringify(bullets));
    });
    socket.on('signUp', function (data) {
        data = JSON.parse(data);
        returnObj = {};
        returnObj.result = 'failed';
        returnObj.message = '';
        if (!(data.userName in userList)) {
            returnObj.result = 'succeed';
            returnObj.identity = data.userName;
            userList[data.userName] = data.password;
        } else {
            returnObj.message = 'The user name is already exist!';
        }
        returnJSON = JSON.stringify(returnObj);
        socket.emit("signUp", returnJSON);
        io.emit('updateBullets', JSON.stringify(bullets));
    });
    socket.on('logOut', function (data) {
        data = JSON.parse(data);
        returnObj = {};
        returnObj.result = 'succeed';
        viewer++;
        players.splice(players.indexOf(data.identity), 1);
        let socketId = socket.id;
        delete playersSocketId.socketId;
        updateUser();
        returnObj.identity = 'guest';
        reset();
        distributeBullets();
        returnJSON = JSON.stringify(returnObj);
        isPlaying = false;
        socket.emit("logOut", returnJSON);
        io.emit('updateBullets', JSON.stringify(bullets));
    });

    socket.on("requireForRestart", function (data) {
        if (players.length >= 2) {
            io.emit("requireForRestart", data);
        }
    });
    socket.on("agreeToRestart", function (data) {

        data = JSON.parse(data);
        if (data.identity === players[0] || data.identity === players[1]) {
            reset();
            distributeBullets();
            postInform = true
        }
    });


    socket.on('dragBullet', function (data) {
        data = JSON.parse(data);
        for (let bullet of bullets) {
            if (bullet.status == "preparing") {
                bullet.location = data.location;
                io.emit('updateBullets', JSON.stringify(bullets));
                break;
            }
        }
    });
    socket.on('shootBullet', function (data) {
        data = JSON.parse(data);
        for (let bullet of bullets) {
            if (bullet.status === "preparing") {
                shotBullet(bullet, data.location, data.speed);
                io.emit('updateBullets', JSON.stringify(bullets));
                postInform = true;
                break;
            }
        }
    });

    socket.on("disconnect", function () {
        let socketId = socket.id;
        if(playersSocketId.socketId){
            players.splice(players.indexOf(playersSocketId.socketId), 1);
            delete playersSocketId.socketId;
            reset();
            distributeBullets();
        }else{
            viewer--;
        }
        updateUser();
    })
})
setInterval(function () {
     if (isPlaying) {
        if(bulletsStopped() === false){
            io.emit('updateBullets', JSON.stringify(bullets));
            io.emit('waitToStop', "");
            refreshTable();
        }
        if (bulletsNotShot() > 0 && bulletsStopped() && postInform) {
            postInform = false;
            if (bulletsNotShot() % 2 === 0) {
                readToShot(players[0]);
                io.emit("waitToShoot", JSON.stringify(players[0]));
                io.emit('updateBullets', JSON.stringify(bullets));

            } else {
                readToShot(players[1]);
                io.emit("waitToShoot", JSON.stringify(players[1]));
                io.emit('updateBullets', JSON.stringify(bullets));
            }
        }

    }
},1000/60);


console.log(`Server Running at port 3000  CNTL-C to quit`)
console.log(`To Test:`)
console.log(`Open several browsers to: http://localhost:3000/Assignment3.html`)
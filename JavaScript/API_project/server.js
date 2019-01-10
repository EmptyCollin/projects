const API_KEY = "39f319898519f6bbf0b875bd4cb591e6";

const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;
const ROOT_DIR = '/html';

const https = require('https')
const url = require('url')
const qstring = require('querystring')

// the accessible url address
const addressNames = ['/Assignment4.html','/recipes.html','/recipes','/index.html','/',''];
let apiData;

app.use(function(req, res, next) {
    console.log('-------------------------------');
    console.log('req.path: ', req.path);
    console.log('serving:' + __dirname + ROOT_DIR + req.path);
    next();
});

// load static files
app.use(express.static(__dirname + ROOT_DIR));

// response the require from get method
// create and send a html page to the client based on the url and parameters
app.get('*',function (req, res) {
    console.log(JSON.stringify(req.query));
    let ingredients;
    if(addressNames.indexOf(req.params[0])>=0){
        console.log(req.query["ingredients"])
        if(req.query["ingredients"] !== undefined){
            ingredients = req.query["ingredients"];
            getRecipes(ingredients, res,"get");
        }else{
            let data={};
            data.count = 0;
            sendResponse(data,res);
        }
    }else{
        res.send("404  <br>  Page Not Found!");
        res.end();
    }
});

// response the post require
// send the data getting from f2f with form of JSON string
app.use(express.json());
app.post("/recipes",function (req,res) {
    let data = req.body;
    getRecipes(data.ingredients,res,"post");

});

// get recipes from f2f by using api
function getRecipes(ingredient, res,method) {
    const options = {
        host: 'www.food2fork.com',
        path: `/api/search?q=${ingredient}&key=${API_KEY}`
    };
    https.request(options, function (apiResponse) {
        parseData(apiResponse, res,method)
    }).end()
}

// according to the method, parse the data from f2f and send different content to client
// get method (namely submit the require with url address ) will be sent a html page;
// post method (submit the require by click the button) will receive the JSON string which records the recipes
function parseData(apiResponse, res,method) {
    apiData = ''
    apiResponse.on('data', function (chunk) {
        apiData += chunk;
    });
    apiResponse.on('end', function () {
        apiData = JSON.parse(apiData);
        if(method==="post"){
            res.send(JSON.stringify(apiData));
            res.end();
        }
        else{
            sendResponse(apiData,res);
        }
    });
}

// create and send a html page
function sendResponse(data, res){
    let page = "";
    let tableContent = "";
    page += '<!DOCTYPE html><html lang="en">'+
        '<head><meta charset="UTF-8"><title>Assignment_4</title>'+
        '<link rel="stylesheet" href="style.css"></head>'+
        '<body><br><div align="center">'+
        '<div style="display:inline-block;font-size:14px;size: 20px" >Please type in the Ingredient(s): </div>'+
        '<input type="text" value = "" id="ingredients" style="size: 20px">'+
        '<input type = "button" value = "Submit" onClick = "submit()"></input></div></br>'+
        '<div align="center"><table id="table">';
    for(let i = 0 ;i <data.count;){
        tableContent += '<tr>';
        for(let j = 0; j <3;j++,i++){
            if(i===data.count){
                break;
            }else{
                console.log(data.recipes[i].image_url)
                console.log(typeof  data.recipes[i].image_url)
                tableContent +=
                    '<td><a target="_blank" href=\"' + data.recipes[i].f2f_url +'\">' +
                    '<img class="picture" src="'+data.recipes[i].image_url+ '"></img>'+'</a><br>'+
                    '<a target="_blank" href=\"' + data.recipes[i].f2f_url +'\">' +data.recipes[i].title +'</a></td>'
            }
        }
        tableContent += '</tr>';
    }
    page += tableContent;
    page += '</table></div><script src="food.js"></script></body></html>'
    res.send(page);
    res.end();
}

//start server
app.listen(PORT, err => {
    if (err) console.log(err)
    else {
        console.log(`Server listening on port: ${PORT}`)
        console.log('To Test:')
        console.log('http://localhost:3000/Assignment4.html')
        console.log('http://localhost:3000/recipes.html')
        console.log('http://localhost:3000/recipes')
        console.log('http://localhost:3000/index.html')
        console.log('http://localhost:3000/')
        console.log('http://localhost:3000')
    }
})

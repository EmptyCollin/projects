const xhr = new XMLHttpRequest();
const url = "http://localhost:3000/recipes"

const table = document.getElementById("table");
const ingredients = document.getElementById("ingredients")

// submit handler
function submit() {
    if(ingredients.value=== ""){return;}
    let data = {};
    data.ingredients= ingredients.value;
    ingredients.value = "";
    let json = JSON.stringify(data);
    console.log(json)
    xhr.open("POST", url, true);

    xhr.setRequestHeader('Content-type','application/json; charset=utf-8');
    xhr.onload = function () {
        let tableContent = JSON.parse(xhr.responseText);
        if (xhr.readyState == 4 && xhr.status == "200") {
            redrawTable(tableContent);
        } else {
            console.log(tableContent);
        }
    }
    xhr.send(json);
}
// rewrite the content of table
function redrawTable(data) {
    let tableContent = '';
    for(let i = 0 ;i <data.count;){
        tableContent += '<tr>';
        for(let j = 0; j <3;j++,i++){
            if(i===data.count){
                break;
            }else{
                tableContent +=
                    '<td><a target="_blank" href="' + data.recipes[i].f2f_url +'">' +
                    '<img class="picture" src="'+data.recipes[i].image_url+ '"></img>'+'</a><br>'+
                    '<a target="_blank" href="' + data.recipes[i].f2f_url +'">' +data.recipes[i].title +'</a></td>'
            }
        }
        tableContent += '</tr>';
    }
    console.log(tableContent);
    table.innerHTML = tableContent;
}

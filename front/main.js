

async function count_up_gp (){
    // получаем введенные значения
    let summa_iska = document.getElementById("summa_iska").value;

        // теперь передаем значение в Python для обработки
    let value_cur = await eel.count_up_gp_py(summa_iska)();
        // выводим на экран полученное значение

    document.getElementById("gp").innerHTML = value_cur;

}

document.getElementById("btn-gp").onclick = count_up_gp;

async function fill_the_form (){
    // получаем введенные значения
    let summa_iska = document.getElementById("summa_iska").value;
    let otvetchik = document.getElementById("otvetchik").value;
    let court = document.getElementById("court").value;

        // теперь передаем значение в Python для обработки
    let array = await eel.fill_the_form_py(summa_iska, court, otvetchik)();
    document.getElementById("otvetchik").innerHTML = array;
    document.getElementById("court").innerHTML = array;


}


document.getElementById("btn-zayavka").onclick = fill_the_form;


async function open_url (){
    // получаем введенные значения
    let court = document.getElementById("court").value;
        // теперь передаем значение в Python для обработки
    await eel.open_url_py(court)();

}


document.getElementById("btn-url").onclick = open_url;
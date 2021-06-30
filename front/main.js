async function count_up_gp (){
    // получаем введенные значения
    let summa_iska = document.getElementById("summa_iska").value;
        // передаем значение в Python для обработки
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
        // передаем значение в Python для обработки
    let gp = await eel.fill_the_form_py(summa_iska, court, otvetchik)();
    document.getElementById("gp").innerHTML = gp[0];
    document.getElementById("court").value = gp[1];
    document.getElementById("otvetchik").value = gp[2];
}

document.getElementById("btn-zayavka").onclick = fill_the_form;

async function open_url (){
    // получаем введенные значения
    let court = document.getElementById("court").value;
        // передаем значение в Python для обработки
    await eel.open_url_py(court)();
}

document.getElementById("btn-url").onclick = open_url;
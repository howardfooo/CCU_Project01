// 錯誤
var fav_del_btn = document.getElementById("fav_del_btn")
var fav_add_btn = document.getElementById("fav_add_btn")

function fav_del(Rid, back) {
    const url = `../favorite/fav_del?Rid=${Rid}&back=${back}`;
    fetch(url)
    fav_del_btn.id = `fav_add_btn`
    fav_del_btn.className = `inline-flex justify-center items-center w-10 h-10 m-1 text-xl text-red-700 duration-200 hover:bg-white hover:text-gray-900 bg-gray-100 border border-gray-200 rounded-lg`
    fav_del_btn.innerHTML = `<i class="fa-regular fa-heart"></i>`
    // fav_add_btn.onclick = `fav_add('${Rid}', '${back}')`
    fav_add_btn.addEventListener('click', fav_add.bind(Rid, back))
}

function fav_add(Rid, back) {
    const url = `./fav_add?Rid=${Rid}`;
    fetch(url)
    fav_add_btn.id = `fav_del_btn`
    fav_add_btn.className = `inline-flex justify-center items-center w-10 h-10 m-1 text-xl text-red-700 duration-200 hover:bg-white hover:text-gray-900 bg-gray-100 border border-gray-200 rounded-lg`
    fav_add_btn.innerHTML = `<i class="fa-solid fa-heart"></i>`
    // fav_add_btn.onclick = `fav_del('${Rid}', '${back}')`
    fav_del_btn.addEventListener('click', fav_del.bind(Rid, back))
}

// document.getElementById('change-theme-btn').addEventListener('click', function () {
//     let darkThemeEnabled = document.body.classList.toggle('dark-theme');
//     localStorage.setItem('dark-theme-enabled', darkThemeEnabled);
// });
//
// if (JSON.parse(localStorage.getItem('dark-theme-enabled'))) {
//     document.body.classList.add('dark-theme');
// }
function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

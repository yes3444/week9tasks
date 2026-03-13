
{
    document.addEventListener("DOMContentLoaded", function() {
  
    fetch("https://huayan.pythonanywhere.com/animals")
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById("animalList");
            data.forEach(fruit => {
                list.innerHTML += "<li>" + fruit + "</li>";
            });
        });
});
}


function getStudentInfo(){
    const inputName = document.getElementById("inputName").value;
  
    fetch("https://huayan.pythonanywhere.com/studentInfo",{
        method: "POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({name:inputName})
    })
    .then(response => response.json())
    .then(data =>{
        document.getElementById("photo").src = data.photo;
            document.getElementById("name").textContent = data.name;
            document.getElementById("age").textContent = data.age;
            document.getElementById("course").textContent = data.course;
            document.getElementById("level").textContent = data.level;
            document.getElementById("department").textContent = data.department;
    });
}


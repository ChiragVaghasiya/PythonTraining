function submitFunc() {
    // debugger;
    alert("Your Data is Submitted!!!");
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let address = document.getElementById("address").value;
    let dob = document.getElementById("dob").value;
    let gender = document.getElementById("gender").value;

    console.log(email);

    // function readsaveData() {
    //     var saveData  = {}

    //    saveData["name"]=document.getElementById("name").value; 
    //    saveData["email"]=document.getElementById("email").value; 
    //    saveData["address"]=document.getElementById("address").value; 
    //    saveData["dob"]=document.getElementById("dob").value; 
    //    saveData["gender"]=document.getElementById("gender").value; 
    //    return saveData;
    //    console.log(saveData);
    //    
    // }

    const dataFetch = [];
    dataFetch.push({
       name : name
    })

    localStorage.setItem("data", JSON.stringify(dataFetch))
}
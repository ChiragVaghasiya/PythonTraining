var selectedRow = null;
listOfData = [];
function getItemss() {
      var formData;
      if (localStorage.getItem("formData") == null) {
          formData = [];
      }
      else {
        formData = JSON.parse(localStorage.getItem("formData"))
      }
  
}
document.getElementById("date").max = new Date().toISOString().split("T")[0];
window.onbeforeunload = onFormSubmit();
function onFormSubmit() {
    event.preventDefault();
  if (
    document.getElementById("fname").value == "" ){
     alert("Please Enter the  name")
    }
    // else if (document.getElementById("fname").value != isNaN(fname)){
      
    //   alert("Name should not contain a number!!!")
    // }
    else if(
      document.getElementById("address").value == "" 
      ){
      alert("Please Enter the address")
          }
    else if(
      document.getElementById("email").value == "" 
            ){
      alert("Please Enter the email")
      
    }
    else if(
            document.getElementById("date").value == "")
      {
      alert("Please Enter the date")
  
  } 
    else if(
            document.getElementById("gender").value == "")
      {
      alert("Please select the gender")
  
  } 
  else {
    var formData = readFormData();
    if (selectedRow == null) {
      insertNewRecord(formData);
    } else {
      updateRecord(formData);
    }
    resetForm();
  }
}

//Retrieve the data
function readFormData() {
  var formData = {};

  var fname = document.getElementById("fname").value;
  var address = document.getElementById("address").value;
  var email = document.getElementById("email").value;
  var date= document.getElementById("date").value;
  let selected = document.getElementsByName("child");    
  const radioo = Array.from(selected).find((ele) => ele.checked);
  var radio = radioo.value;
  
  getItemss()
  // Save the name in localStorage.
  listOfData.push({
    fname :fname,
    address :address,
    email: email,
    date: date,
    radio: radio,
  })
  localStorage.setItem("listOfData" , JSON.stringify(listOfData));
  formData["fname"] = fname
  formData["address"] = address
  formData["email"] = email
  formData["date"] = date
  formData["radio"] = radio
  
  return formData;
}

document.onload = listOfData[index];
//Insert the data
function insertNewRecord(data) {

  var table = document
    .getElementById("storeList")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.length);
  getItemss()
  cell1 = newRow.insertCell(0);
  cell1.innerHTML = data.fname;

  cell2 = newRow.insertCell(1);
  cell2.innerHTML = data.address;

  cell3 = newRow.insertCell(2);
  cell3.innerHTML = data.email;

  cell4 = newRow.insertCell(3);
  cell4.innerHTML = data.date;

  cell5 = newRow.insertCell(4);
  cell5.innerHTML = data.radio;

  cell6 = newRow.insertCell(5);
  cell6.innerHTML = `<button onClick="onEdit(this)">Edit</button> <button onClick="onDelete(this)">Delete</button>`;

}

//Edit the data
function onEdit(td) {
  getItemss()
  selectedRow = td.parentElement.parentElement;
  document.getElementById("fname").value = selectedRow.cells[0].innerHTML;
  document.getElementById("address").value = selectedRow.cells[1].innerHTML;
  document.getElementById("email").value = selectedRow.cells[2].innerHTML;
  document.getElementById("date").value = selectedRow.cells[3].innerHTML;
  document.getElementById("radio").value = selectedRow.cells[4].innerHTML;

  localStorage.setItem("listOfData" , JSON.stringify(listOfData));
  listOfData.push({
    fname :fname,
    address :address,
    email: email,
    date: date,
    radio: radio,
  })

  // editing data on local sorage

}
function updateRecord(formData) {
  selectedRow.cells[0].innerHTML = formData.fname;
  selectedRow.cells[1].innerHTML = formData.address;
  selectedRow.cells[2].innerHTML = formData.email;
  selectedRow.cells[3].innerHTML = formData.date;
  selectedRow.cells[4].innerHTML = formData.radio;


    listOfData.push({
    fname :fname,
    address :address,
    email: email,
    date: date,
    radio: radio,
  })

}

//Delete the data
function onDelete(td) {
  if (confirm("Do you want to delete this record?")) {
    row = td.parentElement.parentElement;
    console.log(row);
    
    document.getElementById("storeList").deleteRow(row.rowIndex);
    localStorage.remove("storeList");
    resetForm();
  }

}

//Reset the data
function resetForm() {
  document.getElementById("fname").value = "";
  document.getElementById("address").value = "";
  document.getElementById("email").value = "";
  document.getElementById("date").value = "";
  document.getElementById("radio").value = "";
  selectedRow = null;
}

function resetAllData(){
  localStorage.clear();
  document.getElementById("fname").value = "";
  document.getElementById("address").value = "";
  document.getElementById("email").value = "";
  document.getElementById("date").value = "";
  document.getElementById("radio").value = "";
  insertNewRecord = null;
  // insertNewRecord = Null;
  selectedRow = null;
}
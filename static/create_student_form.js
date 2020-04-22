//////////////// type phone number //////////////////

$(window).load(function()
{
   var phones = { "mask": "+38(0##) ###-##-##"};
    $('#inputPhone').inputmask({
        mask: phones,
        greedy: false,
        definitions: { '#': { validator: "[0-9]", cardinality: 1}} });
});


//////////////// add courses dropdown fields //////////////////

// temporary variable for storage last removed select div:
var removedBox;
// object that contain ID of chosen courses with appropriate div ID. e.g. {div_1: 1, div_2: 2, div_3: 3}:
var chosenCoursesID = new Object();

// add new input field with new id:
var counter = 1;
function addCourse() {
    // set max number of selectable courses:
    let max_courses_num = 3
    if (document.getElementsByClassName("box").length) {
        let total_element = document.getElementById("coursesList").childElementCount;
        // hide button 'add course' if number of selected fields reached max value:
        if (total_element == max_courses_num - 1) {
            document.getElementById("addCourseButton").style.display = "none";
        };
        // clone last added div select field:
        if (total_element < max_courses_num ) {
            let itm = document.getElementById("coursesList").lastElementChild;
            var copy = itm.cloneNode(true);
            copy.id = 'div_' + (++counter);
            document.getElementById("coursesList").appendChild(copy);
        };
        refreshDropdownList(copy.id)
    } else {
        // return the last removed div and clear his selected value:
        removedBox.getElementsByTagName("select").courses.selectedIndex = 0
        document.getElementById("coursesList").appendChild(removedBox);
        refreshDropdownList(removedBox.id)
    };
};


// delete input field with appropriate id:
function removeCourse(div_id) {
    // show button 'add course' again if select fields less than max value:
    if (document.getElementById("addCourseButton").style.display == "none") {
        document.getElementById("addCourseButton").style.display = "inline";
    };
    // remember the last div that need to delete:
    removedBox = document.getElementById(div_id);
    // and remove them:
    document.getElementById(div_id).remove();
    // delete course ID from the array:
    delete chosenCoursesID[div_id];

    // call refreshing function again:
    // find any select tag:
    if (document.getElementsByClassName('box').length) {
        let boxID = document.getElementsByClassName('box')[0].id
        // and put it's id like an argument to the refreshing function:
        refreshDropdownList(boxID)
    };
};


function addToChosenCourses(boxId) {
    // get last selected course ID:
    let courseID = document.getElementById(boxId).getElementsByTagName("select").courses.selectedIndex

    // add course ID to the array:
    chosenCoursesID[boxId] = courseID;

    // delete course ID from the array if it no longer selected:
    Object.keys(chosenCoursesID).forEach(function(key) {
        if (!document.getElementById(key)) {
            delete chosenCoursesID[key];
        }
    });
};


function refreshDropdownList(boxId) {
    // get array object with all values of options from select tag:
    if (document.getElementById(boxId)) {
        let options = document.getElementById(boxId).getElementsByTagName("option");

        // check if any option was selected before:
        for (const option of options) {
            if (Object.values(chosenCoursesID).includes(parseInt(option.value))) {
                option.disabled = true;
            } else {
                option.disabled = false;
            };
        };
    };
};


////////////////// form validation //////////////////////

function validateForm() {
    var name = document.forms["formStudentCreation"]["name"].value;
    var regexName = /^[a-zA-Z\s-]*$/;
    var email = document.forms["formStudentCreation"]["email"].value;
    var regexEmail = /^\S+@\S+\.\S+$/;
    var phone = document.forms["formStudentCreation"]["phone"].value;
    var regexPhone = /^\+38\(0\d{2}\) \d{3}-\d{2}-\d{2}$/;
    var statusName;
    var statusEmail;
    var statusPhone;

    // name field validation:
    if (name == "") {
        document.getElementById("inputName").style.borderColor = "red";
        document.getElementById("nameHint").style.color = "red";
        document.getElementById("nameHint").innerHTML = "This field can't be empty!";
        statusName = false;
    } else if (regexName.test(name) === false) {
        document.getElementById("inputName").style.borderColor = "red";
        document.getElementById("nameHint").style.color = "red";
        document.getElementById("nameHint").innerHTML = "The name should consist of only Latin letters, hyphens and spaces!";
        statusName = false;
    } else {
        document.getElementById("inputName").style.borderColor = "green";
        document.getElementById("nameHint").style.color = "green";
        document.getElementById("nameHint").innerHTML = "Name is valid";
        statusName = true;
    };

    // email field validation:
    if (email == "") {
        document.getElementById("inputEmail").style.borderColor = "red"
        document.getElementById("emailHint").style.color = "red";
        document.getElementById("emailHint").innerHTML = "This field can't be empty!";
        statusEmail = false;
    } else if (regexEmail.test(email) === false) {
        document.getElementById("inputEmail").style.borderColor = "red";
        document.getElementById("emailHint").style.color = "red";
        document.getElementById("emailHint").innerHTML = "E-mail is not valid!";
        statusEmail = false;
    } else {
        document.getElementById("inputEmail").style.borderColor = "green";
        document.getElementById("emailHint").style.color = "green";
        document.getElementById("emailHint").innerHTML = "E-mail is valid";
        statusEmail = true;
    };

    // phone field validation:
    if (phone == "" || regexPhone.test(phone)) {
        document.getElementById("inputPhone").style.borderColor = null;
        document.getElementById("phoneHint").innerHTML = null;
        statusPhone = true;
    } else {
        document.getElementById("inputPhone").style.borderColor = "red";
        document.getElementById("phoneHint").innerHTML = "Phone number is not valid!";
        statusPhone = false;
    };

//    document.getElementById("studentCreatedModal").showModal();
    return statusName && statusEmail && statusPhone;
}

//////////////// type phone number //////////////////

$(window).load(function()
{
   var phones = { "mask": "+38(0##) ###-##-##"};
    $('#phoneNumberField').inputmask({
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

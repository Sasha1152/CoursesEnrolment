var removedCourse;
var addCourseButton = document.getElementById("addCourseButton")

// add new input field with new id
var counter = 1;
function addCourse() {
    let max_courses_num = 3
    if (document.getElementsByClassName("box").length) {
        let total_element = document.getElementById("coursesList").childElementCount;
        if (total_element == max_courses_num - 1) {
            document.getElementById("addCourseButton").style.display = "none";
        };

        if (total_element < max_courses_num ) {
            let itm = document.getElementById("coursesList").lastElementChild;
            let copy = itm.cloneNode(true);
            copy.id = 'div_' + (++counter);
            document.getElementById("coursesList").appendChild(copy);
        }
    } else {
        document.getElementById("coursesList").appendChild(removedCourse);
    };
};


// delete input field with appropriate id
function removeCourse(div_id) {
    console.log(document.getElementById("addCourseButton"))
    if (document.getElementById("addCourseButton").style.display == "none") {
        document.getElementById("addCourseButton").style.display = "inline";
    }
    removedCourse = document.getElementById(div_id);
    var element = document.getElementById(div_id);
    element.parentNode.removeChild(element);
}

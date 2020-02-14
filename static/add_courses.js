var firstCourse

// add new input field with new id
var counter = 1;
function addCourse() {
    if (document.getElementsByClassName("box").length) {
        var total_element = document.getElementById("coursesList").childElementCount;

        if(total_element < 3 ){
            var itm = document.getElementById("coursesList").lastElementChild;
            var copy = itm.cloneNode(true);
            copy.id = 'div_' + (++counter);
            document.getElementById("coursesList").appendChild(copy);
        }
    } else {
        document.getElementById("coursesList").appendChild(removedCourse);
    }
}


// delete input field with appropriate id
function removeCourse(div_id) {
    removedCourse = document.getElementById(div_id)
    var element = document.getElementById(div_id);
    element.parentNode.removeChild(element);
}

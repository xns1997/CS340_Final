var tag_bar_tags = document.getElementsByClassName("tag-bar-tag");
var top_forms = document.getElementsByClassName("form");
var down_results = document.getElementsByClassName("app-result-list");
function top_form_change(index){
    console.log(tag_bar_tags[index]);
    for(var i = 0 ; i  < 6; i++){
        top_forms[i].classList.add("invisible");
        down_results[i].classList.add("invisible");
        tag_bar_tags[i].classList.remove("tag-choosed")
    }
    top_forms[index].classList.remove("invisible");
    tag_bar_tags[index].classList.add("tag-choosed");
    down_results[index].classList.remove("invisible");
}
var first = false;

console.log(tag_bar_tags[0])
tag_bar_tags[0].onclick = function(){top_form_change(0)};
tag_bar_tags[1].onclick = function(){console.log(tag_bar_tags[0]);top_form_change(1)};
tag_bar_tags[2].onclick = function(){top_form_change(2)};
tag_bar_tags[3].onclick = function(){top_form_change(3)};
tag_bar_tags[4].onclick = function(){top_form_change(4)};
tag_bar_tags[5].onclick = function(){top_form_change(5)};


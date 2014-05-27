function join(){
  $("#join").addClass("disabled");
  $("#quit").removeClass("disabled");
  $("#add_comment").removeClass("disabled");
}
function quit(){
  $("#quit").addClass("disabled");
  $("#add_comment").addClass("disabled");
  $("#join").removeClass("disabled");
}
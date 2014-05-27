window.onload=function(){
  //为导航条上的按钮添加active类
  var pageName = document.getElementsByTagName("title")[0].innerHTML;
  var navList = document.getElementById("navList").getElementsByTagName("li");
  for(var i = 0;i < navList.length;i ++){
    var btnName = navList[i].getElementsByTagName("a")[0];
	if(btnName.innerHTML == pageName) {
	  navList[i].setAttribute("class","active");
	  return;
	}
  }
}
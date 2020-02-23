jQuery(document).ready(function() {
	
	"use strict";
	var modalPhone = document.getElementById("modalPhone");
	var myBtnPhone = document.getElementById("myButtonPhone");
	var span = document.getElementsByClassName("close")[0];

	var modalPzu = document.getElementById("modalPzu");
	var myBtnPzu = document.getElementById("myBtnPzu");

	// When the user clicks the button, open the modal "CALL BACK"
	myBtnPhone.onclick = function() {
	  modalPhone.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span.onclick = function() {
	  modalPhone.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
	  if (event.target === modalPhone) {
		modalPhone.style.display = "none";
	  }
	}

	// // When the user clicks the button, open the modal "PZU"
	// myBtnPzu.onclick = function() {
	//   modalPzu.style.display = "block";
	// }
	//
	// // When the user clicks on <span> (x), close the modal
	// span.onclick = function() {
	//   modalPzu.style.display = "none";
	// }
	//
	// // When the user clicks anywhere outside of the modal, close it
	// window.onclick = function(event) {
	//   if (event.target === modal) {
	// 	modalPzu.style.display = "none";
	//   }
	// }

});
jQuery(document).ready(function() {
	
	"use strict";
	$("#phone").inputmask("(999) 999-99-99");
	$("#phone2").inputmask("(999) 999-99-99");

	var modalPhone = document.getElementById("modalPhone");
	var myBtnPhone = document.getElementById("myButtonPhone");
	var span = document.getElementsByClassName("close")[0];

	var modalPzu = document.getElementById("modalPzu");
	var myBtnPzu = document.getElementById("myBtnPzu");
	var spanPzu = document.getElementsByClassName("close")[1];

	// When the user clicks the button, open the modal "CALL BACK"
	myBtnPhone.onclick = function() {
	  modalPhone.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span.onclick = function() {
	  modalPhone.style.display = "none";
	}

	// When the user clicks the button, open the modal "PZU"
	myBtnPzu.onclick = function() {
	  modalPzu.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	spanPzu.onclick = function() {
	  modalPzu.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
	  if (event.target === modalPhone) {
		  modalPhone.style.display = "none";
	  }
	  else if (event.target === modalPzu) {
	      modalPzu.style.display = "none";
      }
	}

});
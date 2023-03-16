const close = document.getElementById('close');
const open = document.getElementById('open');
const myModal = document.getElementById('myModal');
const myForm = document.getElementById('form');
let inputFile = document.getElementById('file')

open.addEventListener('click', () => {
  console.log('open clicked');
  myModal.classList.add('show');
});

close.addEventListener('click', () => {
  myModal.classList.remove('show');
});


//Drag and drop section


document.querySelectorAll(".drop-zone__input").forEach(inputElement => {
  const dropZoneElement = inputElement.closest(".drop-zone");
  const myForm = document.getElementById('form');

  dropZoneElement.addEventListener("dragover", e => {
    e.preventDefault();
    console.log("dragover");
    dropZoneElement.classList.add("drop-zone--over");
  });

  ["dragleave", "dragend"].forEach(type => {
      dropZoneElement.addEventListener(type, e => {
          dropZoneElement.classList.remove("drop-zone--over");
      });
  });



  window.addEventListener('paste', e => {
      inputFile.files = e.clipboardData.files;
      document.getElementById('form').submit();
      document.getElementById('myModal').classList.add('show');
  });


  dropZoneElement.addEventListener("drop", e => {
    e.preventDefault();
    let files = e.dataTransfer.files;
    inputFile.files = files;
    dropZoneElement.classList.add("drop-zone--over");
    document.getElementById('form').submit();
    document.getElementById('myModal').classList.add('show');
    });

    dropZoneElement.addEventListener('change', () => {
      document.getElementById('form').submit();
    });
   //  dropZoneElement.classList.remove("drop-zone-over");
});


//menu on smaller devices

menu_icon = document.querySelector(".hamb");
navbar = document.querySelector(".othernav");

menu_icon.addEventListener('click', () => {
  navbar.classList.toggle('active');
});




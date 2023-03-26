document.querySelectorAll('.card-image').forEach( card_image_element => {
    card_image_element.addEventListener('click', function(event){
        event.preventDefault();
        const NOTE_CARD_ELEMENT = card_image_element.parentElement;
        NOTE_CARD_ELEMENT.classList.toggle('show-description');
    });
});
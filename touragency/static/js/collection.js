"use strict";
function slide(event) {
    const slidesNodes = document.querySelectorAll('.slide-img');
    let idx = 0;
    for (let i of slidesNodes) {
        if (i.style.display === 'block') {
            idx = +i.dataset.id;
        }
    }
    console.log(idx);
    if (event.target.classList.contains('left')) {
        if (idx === 1) {
            idx = slidesNodes.length;
        } else {
            idx--
        }
    } else {
        if (idx === slidesNodes.length) {
            idx = 1
        } else {
            idx ++
        }
    }
    slidesNodes.forEach(node => {
        if (node.dataset.id === idx.toString()) {
            node.style.display = 'block';
        } else {
            node.style.display = 'none';
        }
    });
}

window.addEventListener('load', () => {
    const arrows = document.querySelectorAll('.slider-arrow');
    arrows.forEach(arrow => {
        arrow.addEventListener('click', event => slide(event))
    })
});
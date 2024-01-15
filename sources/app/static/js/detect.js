
function detect_img(input_img) {
    // 1 : tái chế
    // 2 : hữu cơ
    // 3: vô cơ
    switch (input_img) {
        case 'battery':
        case 'brown-glass': 
        case 'cardboard':
        case 'clothes': 
        case 'green-glass':
        case 'metal':
        case 'paper':
            console.log(input_img)
            return render_trash('1')
        case 'biological':
            return render_trash('2')
        default:
            // 'plastic': 8,
            // 'shoes': 9,
            // 'trash': 10,
            // 'white-glass': 11
            return render_trash('3')
    }
}

function render_trash(input_str) {
    var newImage = document.createElement("img");
    
    switch (input_str) {
        case '1':
            newImage.src = "static/imgs/01_tai_che.png";
            break;
        case '2':
            newImage.src = "static/imgs/02_huu_co.png";
            break;
        default:
            newImage.src = "static/imgs/03_vo_co.png";
            break;
    }
    return newImage;
}
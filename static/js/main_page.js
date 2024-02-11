$(document).ready(function () {
    $('a[href^="#"]').on('click', function (event) {
        event.preventDefault();
        var target = this.hash;
        var $target = $(target);
        $('html, body').animate({
            scrollTop: $target.offset().top
        }, 1000, function () {
            window.location.hash = target;
        });
    });

    document.querySelectorAll('.presentation-item').forEach(function (element) {
        element.addEventListener('mouseover', function () {
            // Находим элемент .learn-more-container внутри текущего .presentation-item
            const infoElement = this.querySelector('.learn-more-container');
            // Получаем значение data-bgcolor
            const bgColor = infoElement.getAttribute('data-bgcolor');
            // Применяем фоновый цвет к элементу .learn-more-container
            infoElement.style.backgroundColor = bgColor;
        });

        element.addEventListener('mouseout', function () {
            // Сбрасываем фоновый цвет элемента .learn-more-container
            const infoElement = this.querySelector('.learn-more-container');
            infoElement.style.backgroundColor = ''; // или можно указать другой цвет
        });
    });
});
//
// document.querySelectorAll('.tilt').forEach(item => {
//         item.addEventListener('mousemove', function (e) {
//             const rect = this.getBoundingClientRect();
//             const x = e.clientX - rect.left; // X координата курсора относительно изображения
//             const y = e.clientY - rect.top; // Y координата курсора относительно изображения
//
//             const centerX = rect.width / 2;
//             const centerY = rect.height / 2;
//
//             // Вычисляем расстояние от центра до курсора
//             const deltaX = (x - centerX) / centerX;
//             const deltaY = (y - centerY) / centerY;
//
//             // Динамически изменяем угол на основе расстояния курсора от центра
//             const rotateX = deltaY * 20; // Увеличиваем максимальный угол наклона
//             const rotateY = deltaX * -20;
//
//             const scale = 1.05; // Увеличение элемента
//
//             this.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(${scale})`;
//         });
//
//         item.addEventListener('mouseout', function () {
//             this.style.transform = 'rotateX(0deg) rotateY(0deg) scale(1)'; // Сбрасываем наклон и масштаб
//         });
//
//     });
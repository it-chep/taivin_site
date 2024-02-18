document.addEventListener('DOMContentLoaded', function () {
    const slides = document.querySelectorAll('.slide');
    const modal = document.querySelectorAll('.modal');

    slides.forEach(function (slide) {
        slide.addEventListener('click', function () {
            const modalId = this.dataset['modal'];
            const $modal = $(`#${modalId}`);
            $modal.fadeIn(500);
            $modal.css('display', 'flex');
        });
    });

    modal.forEach(function (modal) {
        modal.addEventListener('click', function () {
            $(this).fadeOut(500);
        });
    });

    function applyFont(fontId, elementId, fontFamilyName) {
        fetch(`/get_font/${fontId}/`)
            .then(response => response.json())
            .then(data => {
                const fontUrl = data.font_url;
                const font = new FontFace(fontFamilyName, `url(${fontUrl})`);
                return font.load();
            })
            .then(loadedFont => {
                document.fonts.add(loadedFont);
                document.getElementById(elementId).style.fontFamily = `'${fontFamilyName}', sans-serif`;
            })
            .catch(error => {
                console.error('Error fetching font:', error);
            });
    }


// Example usage:
    const fonts = $('.fonts-item');
    fonts.each(function () {
        const fontID = $(this).data('font-id');
        const fontFamilyName = $(this).find('.font-name').text();
        applyFont(fontID, `font_${fontID}`, fontFamilyName);
    });

    const presentationLink = $('.presentation_company-link');
    presentationLink.css('color', presentationLink.data()['color']);

    const counterContainer = $('.article-counter');
    const articleCircle = $('.article-circle');
    articleCircle.css('background-color', counterContainer.data()['color']);
    counterContainer.css('background-color', counterContainer.data()['color']);
    counterContainer.css('color', counterContainer.data()['textColor'])

    const aboutCustomer = $('.about_customer');
    aboutCustomer.css('color', aboutCustomer.data()['color']);

    const articleLine = $('.article-line');
    articleLine.css('background-color', articleLine.data()['color']);

    const fontColorBlock = $('.font-color-block');
    fontColorBlock.css('border', `${fontColorBlock.data()['color']} 1px solid`);

    const fontName = $('.font-name');
    fontName.css('color', fontName.data()['color'])
});
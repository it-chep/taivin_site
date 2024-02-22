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
                let nameFontUrl = data.description_font_url;
                if (!data.description_font_url) {
                    nameFontUrl = fontUrl
                }
                const font = new FontFace(fontFamilyName, `url(${fontUrl})`);
                const nameFont = new FontFace(`${fontFamilyName}_name`, `url(${nameFontUrl})`);
                return Promise.all([font.load(), nameFont.load()]);
            })
            .then(([loadedFont, descriptionFont]) => {
                document.fonts.add(loadedFont);
                document.getElementById(elementId).style.fontFamily = `'${fontFamilyName}', sans-serif`;
                document.fonts.add(descriptionFont);
                document.getElementById(`${elementId}_name`).style.fontFamily = `'${fontFamilyName}_name', sans-serif`;
            })
            .catch(error => {
                return
            });
    }

    const fonts = $('.fonts-item');
    fonts.each(function () {
        const fontID = $(this).data('font-id');
        const fontFamilyName = $(this).find('.font-name').text();
        applyFont(fontID, `font_${fontID}`, fontFamilyName);
    });

    const presentationLink = $('.presentation_company-link');
    if (presentationLink.data()) {
        presentationLink.css('color', presentationLink.data()['color']);
    }

    const counterContainer = $('.article-counter');
    const articleCircle = $('.article-circle');
    articleCircle.css('background-color', counterContainer.data()['color']);
    counterContainer.css('background-color', counterContainer.data()['color']);
    counterContainer.css('color', counterContainer.data()['textColor'])

    const aboutCustomer = $('.about_customer');
    if (aboutCustomer.data()) {
        aboutCustomer.css('color', aboutCustomer.data()['color']);
    }

    const articleLine = $('.article-line');
    if (articleLine.data()) {
        articleLine.css('background-color', articleLine.data()['color']);
    }

    const fontColorBlock = $('.font-color-block');
    if (fontColorBlock.data()) {
        fontColorBlock.css('border', `${fontColorBlock.data()['color']} 1px solid`);
    }

    const fontName = $('.font-name');
    if (fontName.data()) {
        fontName.css('color', fontName.data()['color'])
    }

    let colors = document.querySelectorAll('.color-item-container-beautiful')
    let previousZIndex = 500
    let previousMarginLeft = 0;

    colors.forEach(function (color, index) {
        if (index > 0) {
            let zIndex = previousZIndex - 1;
            let marginLeft = previousMarginLeft + parseInt(color.offsetWidth || 0) - 30;
            color.style.width = color.offsetWidth + 10 + 'px'
            color.style.zIndex = zIndex;
            color.style.marginLeft = marginLeft + 'px';

            previousZIndex = zIndex;
            previousMarginLeft = marginLeft;
        }
    });

    let articleContentTexts = document.querySelectorAll('.article-content-text');

    articleContentTexts.forEach(function (articleContentText, index) {
        let articleLine = articleContentText.closest('.article-item').querySelector('.article-line');
        let header = articleContentText.closest('.article-item').querySelector('.article-content-header');
        let headerHeight = 0;
        const infoLine = articleContentText.closest('.info-line')
        let fontColors = document.querySelector('.font-color-block');
        if (articleLine) {

            let lineSize = infoLine.offsetHeight - (parseFloat(getComputedStyle(articleLine).marginTop))
            articleLine.style.height = lineSize + 'px';
            if (index === 0 && fontColors.offsetHeight === infoLine.offsetHeight) {
                articleLine.style.height = lineSize - 2.5 * (parseFloat(getComputedStyle(infoLine).marginTop)) + 'px'
            } else if (index === 0 && fontColors.offsetHeight < infoLine.offsetHeight) {
                articleLine.style.height = infoLine.offsetHeight - (parseFloat(getComputedStyle(articleLine).marginTop))/1.5 + 'px' ;
            }

            // if (header.clientHeight > 60) {
            //     headerHeight = header.clientHeight - 40;
            // }
            //
            // let lineHeight = articleContentText.offsetHeight + 60 + headerHeight;
            // articleLine.style.height = lineHeight + 'px';
            //
            // if (index === 0 && font_colors){
            //     articleLine.style.height = font_colors.offsetHeight + articleContentText - 60 + 'px'
            // }
        }
    });
});
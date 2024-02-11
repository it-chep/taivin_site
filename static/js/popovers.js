$(window).click(function() {
    $('.api_show_order_items').next('[role=popover]').hide();
});
$(function(){
    $('.api_show_order_items').click(function(event) {
        event.stopPropagation();
        var e = $(this);

        // Скрываем все открытые поповеры, кроме текущего
        $('.api_show_order_items').next('[role=popover]').not(e.next('[role=popover]')).hide()

        // Запрещаем удаление поповера чтобы избежать повторных запросов
        // на время текущей работы со страницей
        $(e).on('hide.bs.popover', function () {
            return false;
        });

        if (e.next('.popover').length) {
            if (e.next('.popover').is(':visible')) {
                e.next('.popover').hide()
            } else {
                e.popover('show');
            }
        } else {
            e.hide();
            e.after($('.cssload-container').first().clone().show())
            var token = this.dataset.token;
            var header = this.dataset.header;
            $.post(e.attr('href'), {'csrfmiddlewaretoken': token}, function(data) {
                e.next('.cssload-container').remove();
                e.show();
                e.popover({
                    content: data,
                    html: true,
                    placement: 'left',
                    title: header,
                    template: '<div class="popover" role="popover" style="min-width:400px; max-width: 600px;">'
                                +'<div class="arrow"></div>'
                                +'<h3 class="popover-title"></h3>'
                                +'<div class="popover-content"><div class="data-content"></div></div>'
                              +'</div>'
                }).popover('show');
            });
        }
        return false;
    });
})

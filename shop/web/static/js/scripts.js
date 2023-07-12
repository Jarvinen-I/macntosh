$(document).ready(function(){
    let form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        let nmb = $('#number').val();
        console.log(nmb);
        let submit_btn = $('#submit_btn');
        let product_id = submit_btn.data('product_id');
        let product_name =submit_btn.data('name');
        let product_price =submit_btn.data('price');
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

            let data = {};
            data.product_id = product_id;
            data.nmb = nmb;
            let csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;
            let url = form.attr('action');

        console.log(data)
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    console.log('OK');
                    console.log(data.products_total_nmb);
                    if (data.products_total_nmb) {
                        $('#basket-total-nmb').text('('+data.products_total_nmb+')');
                        console.log(data.products);
                        $('ul.basket-items').html('');
                        $.each(data.products, function () {
                            $('ul.basket-items').append('<li>' +
                                '<a style="text-transform: none;" href="">'+ product_name+' - ' + nmb + ' шт. '
                                + 'по ' + product_price + ' руб ' +
                                // '<span style="padding-left: 5px;" class="delete-item"> x </span>'+'</a>
                            '</li>');
                        })
                    }
                },
                error: function (){
                    console.log('error')
                }
            })
    });
    // function showingBasket(){
    //     $('.basket-items').toggleClass('hidden');
    // }
    //
    // $('.basket-container').on('click', function (e){
    //     e.preventDefault();
    //     showingBasket()
    // })
    //
    // $('.basket-container').mouseover(function (e){
    //     showingBasket()
    // })
    //
    // $('.basket-container').mouseout(function (e){
    //     showingBasket()
    // })
    $(document).on('click', '.delete-item', function (e){
        e.preventDefault();
        $(this).closest('li').remove();
    });

    function calculatingBasketAmount() {
        let total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function() {
            total_order_amount += parseInt($(this).text());
        });
        console.log(total_order_amount);
        $('#total_order_amount').text(total_order_amount);
    };
    $(document).on('change', '.product-in-basket-nmb', function () {
        let current_nmb = $(this).val();
        let current_tr = $(this).closest('tr');
        let current_price = parseInt(current_tr.find('.product-price').text());
        let total_amount = current_nmb * current_price;
        current_tr.find('.total-product-in-basket-amount').text(total_amount);

        calculatingBasketAmount();
    });

    calculatingBasketAmount();
});











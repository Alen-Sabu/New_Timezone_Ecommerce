$(document).ready(function() {
    $('#apply-coupon-btn').click(function(e) {
      e.preventDefault()


      
      var couponCode = $('#coupon-input').val();
      var token = $('input[name=csrfmiddlewaretoken]').val()

      console.log(couponCode)
      var message = $('#coupon-message');
      $.ajax({
        type: 'POST',
        url: '/shop/apply_coupon',
        data: {
            'coupon_code': couponCode,
            csrfmiddlewaretoken: token
    },
        dataType: 'json',
        success: function(response) {
          if (response.success) {
            $('#coupon-result-success').show()
            $('#coupon-result-success').html(response.message)
            $('#coupon-result').hide()
            console.log(response.message);
            $('.total-change').load(location.href + " .total-change" )
            
          } else {
            $('#coupon-result-success').hide()
            $('#coupon-result').html(response.message)
            $('#coupon-result').show()
            console.log(response.message)
            $('.total-change').load(location.href + " .total-change" )
            
          }
        },
        error: function(response) {
          console.log(response);
          $('#coupon-result').html(response);
        }
      });
    });


    $('#payWallet').click(function(e) {
      e.preventDefault()


      
      
      var token = $('input[name=csrfmiddlewaretoken]').val()

      
      $.ajax({
        type: 'POST',
        url: '/shop/wallet_payment',
        data: {

            
            csrfmiddlewaretoken: token
    },
        dataType: 'json',
        success: function(responsec){
          if(responsec.failure){
            swal("Failed!", responsec.status, "error")
            return
          }else{
          swal("Congratulations!", responsec.status,"success").then((value) =>{
              window.location.href = "/shop/confirmation"
          })
        }
          
      }
        
  });

  });
  
});
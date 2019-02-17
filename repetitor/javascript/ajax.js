//jquery

MainApp.functions.toViews() = function(data)    {
    return $ajax({
      'url' : 'requestApp/views/fromJs'
      'type': 'post',
      'data': data,
      'dataType': 'json',
      'success': function(result) {
        return window.location.reload();
      }

    })
}

$('.btn btn-succes').on('click', function() {
    data = {
        'field_label' : $('input.field_label').val(),
        'body' : $('input.body').val()
    }
    return MainApp.ajaxes.toViews(data)
})

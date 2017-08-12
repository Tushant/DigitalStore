$('.list-store-form').on('submit', function(event) {
	event.preventDefault(); // preventing from the brwoser default behavior for form submission
	var form = $(this);
	console.log(form);
	$.ajax({
		async: true,
		url: form.attr('action'),
		data: form.serialize(),
		type: 'POST',
		dataType: 'json',
		headers: {
			'X-CSRFToken': window.csrf_token
		},

		success: function(data) {
			$('.display').html(
				"<div class='ui floating message'> <i class='close icon'></i>" + data.result + '</div>'
			);
		},

		error: function(xhr, errmsg) {
			$('.display').html(
				"<div class='ui floating message'> <i class='close icon'></i> Oops! We have encountered an error: " +
					errmsg +
					'</div>'
			);
		}
	});
});

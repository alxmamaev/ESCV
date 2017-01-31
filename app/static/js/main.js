$(function() {
	console.log($('#start_date_input').val());
	new Calendar({
		element: $('.daterange--double'),
		earliest_date: '2000-01-1',
		latest_date: moment(),
		start_date: moment(),
		end_date: moment(),
		callback: function() {
			$('#start_date_input').val(moment(this.start_date).format('YY-MM-DD'));
			$('#start_date_input').val(moment(this.end_date).format('YY-MM-DD'));

			$('form').submit();
		}
	});
});
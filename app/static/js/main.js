$(function() {
	new Calendar({
		element: $('.daterange--double'),
		earliest_date: '2000-01-1',
		latest_date: moment(),
		start_date: '2000-01-1',
		end_date: moment(),
		callback: function() {
			$('#start_date_input').val(moment(this.start_date).format('YYYY-MM-DD'));
			$('#end_date_input').val(moment(this.end_date).format('YYYY-MM-DD'));

			$('form').submit();
		}
	});
});
const getFeed = () => {
  $.ajax({
    type: 'GET',
    dataType: 'json',
    url: 'http://localhost:7000/get_feed',
    success: data => {
      $('#cookie_counter').html(`This list has been refreshed ${data['cookies']} times today`)
      const headlines = $('<ul />')
      for (let i = 0; i < 10; i++) {
        headlines.append(`
          <li><a href="${data['data'][i]['link']}" target="_blank">${data['data'][i]['title']}</a>
            <ul>
              <li>Author: ${data['data'][i]['author']}</li>
              <li>Published: ${data['data'][i]['published']}</li>
              <li>${data['data'][i]['summary']}</li>
            </ul>
          </li>`)
      }
      $('#headlines').html(headlines)
    }
  })
}
getFeed()
$('#refresh').click(getFeed)

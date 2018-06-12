const getFeed = () => {
  $.ajax({
    type: 'GET',
    dataType: 'json',
    url: 'http://localhost:7000/get_feed',
    success: data => {
      console.log(data)
      for (let i in data) {
        $('#headlines').append(`
          <li><a href="${data[i]['link']}" target="_blank">${data[i]['title']}</a>
            <ul>
              <li>Author: ${data[i]['author']}</li>
              <li>Published: ${data[i]['published']}</li>
              <li>${data[i]['summary']}</li>
            </ul>
          </li>`)
      }
    }
  })
}
getFeed()

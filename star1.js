const getFeed = () => {
  $.ajax({
    type: 'GET',
    dataType: 'json',
    url: 'http://localhost:7000/get_feed',
    success: data => {
      console.log(data)
      for (let i in data) {
        $('#headlines').append(`<li><a href="${data[i]['link']}" target="_blank">${data[i]['title']}</a></li>`)
      }
    }
  })
}
getFeed()

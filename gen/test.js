result1 = {}
fetch('http://192.168.83.11:5000/dobryplan', {
    method : "POST",
    mode: "cors",
    headers: {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer a78a74466c7a4a689648c6c6c2c563fa",
    },
    body : JSON.stringify({
        'mtype' : 'initialization',
        'userid' : '',
        'user_info' : {
            'company_name' : 'SimpleCoffe',
            'business_type' : 'A coffeeshop', 
            'target market': 'Saint-Petersburg, Russia',
            'target audience': {"age":"all ages", "gender":"all genders", "location":"Saint-Petersburg", "interests":""},
            'project team': [{"name":"Daria Ivanova",  "expertise":"Barista"}, {"name":"Dmitry Petrov", "expertise": "accountant"}],
            'The project have already achieved': "monthly proffit of 25000 rubles, 30000 visitors per month",
            'information': "connect to us directly using the number 123456789", 
            'investment target': 'aquiring new equipment, making better product, doubbling our revenue',
            'investment amount': '10 million rubles', 
            'deadline on investment promises': '1 year',
            'length(symbols)': '200'
        }
    })
})
// .then((response) => response.json())
// .then((data) => result1 = data)
// .then((res) => console.log(res))


let app = new Vue({
    el: '#app',
    data: {
        lat: "",
        lon: "",
        unix_timestamp: 0,
        loading: true,
    },
    methods: {
        getWeather: async function() {
            const response = await axios({
                method: 'get',
                url: "https://api.openweathermap.org/data/2.5/onecall?",
                params: {
                    appid: api_key,
                    lat: this.lat,
                    lon: this.lon,
                }
            })
            this.unix_timestamp = response.data.current.dt
            let date = new Date(this.unix_timestamp*1000)
            console.log(date)
            console.log(response.data)
            console.log(response.data.current.dt)
        }
        // getLocation: function() {
        //     navigator.geolocation.getCurrentPosition(
        //         position => {
        //             this.lat = position.coords.latitude.toFixed(6);
        //             this.lon = position.coords.longitude.toFixed(6);
        //             // console.log(position.coords.latitude);
        //             // console.log(position.coords.longitude);
        //         },
        //         error => {
        //             console.log(error.message);
        //         },
        //     )
        // }
    },
    created: function() {
        navigator.geolocation.getCurrentPosition(position => {
                this.lat = position.coords.latitude.toFixed(6);
                this.lon = position.coords.longitude.toFixed(6);
                // console.log(position.coords.latitude);
                // console.log(position.coords.longitude);
            },
            error => {
                console.log(error.message);
            },
        )
        // setTimeout(this.getWeather(), 10000)
    },
    watch: {
        lat: function() {
            console.log(this.lat, this.lon);
            this.loading = false
        }
    }
})
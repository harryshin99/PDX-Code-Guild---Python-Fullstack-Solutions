let app = new Vue({
    el: '#app',
    data: {
        lat: "",
        lon: "",
        unix_timestamp: 0,
        loading: true,
        currentDate: '',
        currentTime: '',
        icon: '',
        iconUrl: ''
    },
    methods: {

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
    },
    watch: {
        lon: async function() {
            console.log(this.lat, this.lon);
            this.loading = false;
            const response = await axios({
                method: 'get',
                url: "https://api.openweathermap.org/data/2.5/onecall?",
                params: {
                    appid: api_key,
                    lat: this.lat,
                    lon: this.lon,
                    units: 'imperial',
                }
            })
            this.unix_timestamp = response.data.current.dt
            this.currentDate = new Date(this.unix_timestamp*1000).toLocaleDateString()
            this.currentTime = new Date(this.unix_timestamp*1000).toLocaleTimeString()
            this.icon = response.data.current.weather[0].icon
            this.iconUrl = "http://openweathermap.org/img/wn/" + this.icon + ".png"
            // console.log(this.current)
            console.log(response.data)
            // console.log(response.data.current.dt)
        }
    }
})